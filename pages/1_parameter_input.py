import streamlit as st

from utils.mock_engine import ensure_session_state, update_inputs
from utils.theme import apply_theme, render_header


st.set_page_config(page_title="参数输入页", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "参数输入页",
    "录入氧化铝陶瓷增材制造的关键工艺参数，系统将基于模拟规则生成后续预测、风险与推荐结果。",
)

params = st.session_state["input_params"].copy()

with st.form("parameter_form"):
    col1, col2 = st.columns(2)
    with col1:
        layer_thickness = st.slider("铺层厚度 (μm)", 30, 90, int(params["layer_thickness"]), 1)
        print_speed = st.slider("打印速度 (mm/s)", 20, 70, int(params["print_speed"]), 1)
        laser_power = st.slider("激光功率 (W)", 120, 260, int(params["laser_power"]), 1)
        scan_spacing = st.slider("扫描间距 (mm)", 0.08, 0.20, float(params["scan_spacing"]), 0.01)
    with col2:
        sinter_temp = st.slider("烧结温度 (℃)", 1500, 1650, int(params["sinter_temp"]), 5)
        holding_time = st.slider("保温时间 (h)", 1.0, 4.5, float(params["holding_time"]), 0.1)
        solid_content = st.slider("浆料固含量 (%)", 50, 68, int(params["solid_content"]), 1)
        binder_ratio = st.slider("粘结剂比例 (%)", 2.0, 6.5, float(params["binder_ratio"]), 0.1)

    submitted = st.form_submit_button("生成模拟结果", use_container_width=True)

if submitted:
    update_inputs(
        {
            "layer_thickness": float(layer_thickness),
            "print_speed": float(print_speed),
            "laser_power": float(laser_power),
            "scan_spacing": float(scan_spacing),
            "sinter_temp": float(sinter_temp),
            "holding_time": float(holding_time),
            "solid_content": float(solid_content),
            "binder_ratio": float(binder_ratio),
        }
    )
    st.success("参数已更新，后续页面会自动读取最新模拟结果。")

st.markdown("### 当前参数说明")
left, right = st.columns(2)
with left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">输入变量</div>
            <span class="tag">打印段参数</span>
            <span class="tag">烧结段参数</span>
            <span class="tag">浆料配方参数</span>
            <p>当前原型通过工艺经验规则模拟材料成形表现，用于展示“输入 - 预测 - 评估 - 推荐”的解释性决策链路。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">答辩展示建议</div>
            <p>可优先展示当前默认参数，再手动调整层厚、烧结温度或固含量，观察后续页面中的预测热图、风险等级与推荐方案如何联动变化。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
