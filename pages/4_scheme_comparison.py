import plotly.express as px
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header


st.set_page_config(page_title="方案对比页", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "方案对比页",
    "将当前方案与保守方案、激进方案进行横向对比，展示系统对多种工艺路径的辅助决策能力。",
)

results = get_latest_results()
compare_df = results["compare_df"]

st.markdown("### 多方案指标对比")
st.dataframe(compare_df, use_container_width=True, hide_index=True)

left, right = st.columns(2)
with left:
    density_chart = px.bar(
        compare_df,
        x="方案",
        y="预测致密度(%)",
        color="方案",
        color_discrete_sequence=["#8da9c4", "#3d6f96", "#27455f"],
        title="不同方案的预测致密度",
    )
    density_chart.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.plotly_chart(density_chart, use_container_width=True)

with right:
    risk_efficiency_chart = px.line(
        compare_df,
        x="方案",
        y=["综合风险", "成形效率"],
        markers=True,
        title="风险与效率平衡对比",
    )
    risk_efficiency_chart.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend_title_text="指标",
    )
    st.plotly_chart(risk_efficiency_chart, use_container_width=True)

st.markdown(
    """
    <div class="card">
        <div class="section-title">对比结论</div>
        <p>保守方案风险更低但效率偏弱，激进方案效率较高但稳定性不足。当前方案用于演示时能够体现系统如何在性能、风险与制造效率之间进行权衡。</p>
    </div>
    """,
    unsafe_allow_html=True,
)
