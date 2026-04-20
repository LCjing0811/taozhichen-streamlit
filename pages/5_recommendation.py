import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="推荐结果页", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "推荐结果页",
    "基于模拟预测与风险结果给出当前工艺的推荐等级、优化建议与可解释决策理由。",
)

results = get_latest_results()
params = st.session_state["input_params"]

col1, col2, col3 = st.columns(3)
with col1:
    render_metric_card("推荐指数", f'{results["recommendation_score"]:.1f}/100')
with col2:
    render_metric_card("预测致密度", f'{results["density"]:.2f}%')
with col3:
    render_metric_card("推荐结论", "建议采用" if results["recommendation_score"] >= 75 else "建议优化后采用")

left, right = st.columns([1.1, 1])
with left:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">推荐工艺摘要</div>
            <p>层厚：<strong>{params["layer_thickness"]:.0f} μm</strong></p>
            <p>打印速度：<strong>{params["print_speed"]:.0f} mm/s</strong></p>
            <p>激光功率：<strong>{params["laser_power"]:.0f} W</strong></p>
            <p>烧结温度：<strong>{params["sinter_temp"]:.0f} ℃</strong></p>
            <p>保温时间：<strong>{params["holding_time"]:.1f} h</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">可解释决策逻辑</div>
            <p>系统综合考虑三类目标：</p>
            <p>1. 致密度与热稳定性是否达到展示目标。</p>
            <p>2. 裂纹、孔隙、翘曲风险是否处于可接受窗口。</p>
            <p>3. 工艺效率是否满足增材制造场景下的实际应用需求。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### 优化建议")
for tip in results["recommendations"]:
    st.markdown(
        f"""
        <div class="card" style="margin-bottom: 0.8rem;">
            <p style="margin: 0;">{tip}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.success("当前页面适合作为答辩展示的收束页，用于输出系统推荐结论与解释依据。")
