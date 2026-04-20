from __future__ import annotations

from copy import deepcopy

import numpy as np
import pandas as pd
import streamlit as st


DEFAULT_PARAMS = {
    "layer_thickness": 55.0,
    "print_speed": 42.0,
    "laser_power": 180.0,
    "scan_spacing": 0.11,
    "sinter_temp": 1580.0,
    "holding_time": 2.5,
    "solid_content": 58.0,
    "binder_ratio": 3.8,
}


def ensure_session_state() -> None:
    if "input_params" not in st.session_state:
        st.session_state["input_params"] = deepcopy(DEFAULT_PARAMS)
    if "analysis_results" not in st.session_state:
        st.session_state["analysis_results"] = simulate_results(st.session_state["input_params"])


def simulate_results(params: dict) -> dict:
    layer = params["layer_thickness"]
    speed = params["print_speed"]
    power = params["laser_power"]
    spacing = params["scan_spacing"]
    temp = params["sinter_temp"]
    hold = params["holding_time"]
    solid = params["solid_content"]
    binder = params["binder_ratio"]

    density = np.clip(
        90
        + 0.05 * (temp - 1500)
        + 0.12 * (solid - 55)
        + 0.03 * (power - 170)
        - 0.06 * (layer - 50),
        91,
        99.6,
    )
    shrinkage = np.clip(
        14 + 0.018 * (temp - 1500) + 0.4 * (solid - 56) / 4 - 0.02 * (hold - 2.0) * 10,
        12.5,
        19.8,
    )
    peak_temp = np.clip(710 + power * 1.35 - speed * 2.1 + spacing * 180, 760, 1080)
    thermal_gradient = np.clip(18 + power / 22 - speed / 16 + layer / 40, 14, 32)
    pore_risk = np.clip(62 - 1.1 * (solid - 55) - 0.08 * (temp - 1500), 8, 78)
    crack_risk = np.clip(18 + 0.8 * thermal_gradient + 0.14 * (temp - 1560) - 0.6 * hold, 6, 88)
    warpage_risk = np.clip(15 + 0.3 * speed + 35 * spacing - 0.04 * power, 8, 76)
    efficiency = np.clip(55 + speed * 0.8 - hold * 3.2 - layer * 0.06, 35, 92)
    recommendation_score = np.clip(
        density * 0.42 + efficiency * 0.25 + (100 - max(crack_risk, pore_risk, warpage_risk)) * 0.33,
        40,
        98,
    )

    risk_max = max(crack_risk, pore_risk, warpage_risk)
    if risk_max >= 70:
        risk_level = "高风险"
    elif risk_max >= 45:
        risk_level = "中风险"
    else:
        risk_level = "低风险"

    temp_curve = pd.DataFrame(
        {
            "时间(min)": [0, 20, 40, 60, 90, 120, 150, 180],
            "温度(℃)": [
                25,
                peak_temp * 0.42,
                peak_temp * 0.68,
                peak_temp,
                peak_temp * 0.88,
                peak_temp * 0.74,
                peak_temp * 0.58,
                220,
            ],
        }
    )

    positions = np.linspace(0, 100, 12)
    field_rows = []
    for x in positions:
        for y in positions:
            field_rows.append(
                {
                    "X": round(x, 1),
                    "Y": round(y, 1),
                    "温度场": round(
                        peak_temp
                        - abs(x - 50) * 2.7
                        - abs(y - 50) * 2.4
                        + np.sin(x / 15) * 8
                        + np.cos(y / 18) * 6,
                        2,
                    ),
                }
            )
    heatmap_df = pd.DataFrame(field_rows)

    compare_df = pd.DataFrame(
        [
            {
                "方案": "保守方案",
                "层厚(μm)": 45,
                "打印速度(mm/s)": 35,
                "烧结温度(℃)": 1560,
                "预测致密度(%)": 96.2,
                "综合风险": 28,
                "成形效率": 61,
            },
            {
                "方案": "当前方案",
                "层厚(μm)": round(layer, 1),
                "打印速度(mm/s)": round(speed, 1),
                "烧结温度(℃)": round(temp, 1),
                "预测致密度(%)": round(float(density), 2),
                "综合风险": round(float(risk_max), 1),
                "成形效率": round(float(efficiency), 1),
            },
            {
                "方案": "激进方案",
                "层厚(μm)": 70,
                "打印速度(mm/s)": 52,
                "烧结温度(℃)": 1605,
                "预测致密度(%)": 95.4,
                "综合风险": 67,
                "成形效率": 84,
            },
        ]
    )

    recommendations = []
    if crack_risk > 50:
        recommendations.append("适度降低热梯度，建议将激光功率下调 5% 或提高保温均匀性。")
    else:
        recommendations.append("当前热输入较平稳，具备较好的层间结合基础。")

    if pore_risk > 45:
        recommendations.append("建议提升浆料固含量或微调烧结温度，以降低孔隙残留概率。")
    else:
        recommendations.append("孔隙风险处于可控区间，致密化条件较为充分。")

    if warpage_risk > 45:
        recommendations.append("建议减小扫描间距或优化支撑策略，以抑制翘曲变形。")
    else:
        recommendations.append("翘曲风险较低，结构稳定性满足展示级验证需求。")

    return {
        "plan_name": "当前输入方案",
        "density": float(density),
        "shrinkage": float(shrinkage),
        "peak_temp": float(peak_temp),
        "thermal_gradient": float(thermal_gradient),
        "pore_risk": float(pore_risk),
        "crack_risk": float(crack_risk),
        "warpage_risk": float(warpage_risk),
        "efficiency": float(efficiency),
        "recommendation_score": float(recommendation_score),
        "risk_level": risk_level,
        "temp_curve": temp_curve,
        "heatmap_df": heatmap_df,
        "compare_df": compare_df,
        "recommendations": recommendations,
    }


def update_inputs(params: dict) -> None:
    st.session_state["input_params"] = deepcopy(params)
    st.session_state["analysis_results"] = simulate_results(params)


def get_latest_results() -> dict:
    ensure_session_state()
    return st.session_state["analysis_results"]
