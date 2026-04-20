import plotly.graph_objects as go
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="风险评估页", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "风险评估页",
    "对裂纹、孔隙、翘曲等关键失效模式进行模拟评估，帮助展示可解释风险预警机制。",
)

results = get_latest_results()

col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("综合风险等级", results["risk_level"])
with col2:
    render_metric_card("裂纹风险", f'{results["crack_risk"]:.1f}')
with col3:
    render_metric_card("孔隙风险", f'{results["pore_risk"]:.1f}')
with col4:
    render_metric_card("翘曲风险", f'{results["warpage_risk"]:.1f}')

radar = go.Figure()
radar.add_trace(
    go.Scatterpolar(
        r=[results["crack_risk"], results["pore_risk"], results["warpage_risk"], results["thermal_gradient"]],
        theta=["裂纹倾向", "孔隙倾向", "翘曲倾向", "热梯度敏感性"],
        fill="toself",
        line=dict(color="#3d6f96", width=3),
        fillcolor="rgba(61, 111, 150, 0.25)",
        name="风险画像",
    )
)
radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=20, r=20, t=40, b=20),
)

left, right = st.columns([1.15, 1])
with left:
    st.plotly_chart(radar, use_container_width=True)

with right:
    risk_text = {
        "高风险": "当前参数组合存在较明显的缺陷暴露概率，建议优先调整热输入与烧结制度。",
        "中风险": "当前方案可用于试验验证，但建议结合推荐页给出的修正策略优化窗口。",
        "低风险": "当前参数窗口较稳健，适合用作演示中的优选或基准方案。",
    }
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">风险判读</div>
            <p>{risk_text[results["risk_level"]]}</p>
            <p>裂纹风险主要受热梯度、烧结温度和保温时间影响。</p>
            <p>孔隙风险主要受固含量和烧结致密化能力影响。</p>
            <p>翘曲风险主要受扫描间距、打印速度和局部热输入均匀性影响。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
