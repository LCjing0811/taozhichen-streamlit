import plotly.express as px
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="方案对比", page_icon="📊", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "方案对比",
    "将当前方案与保守方案、激进方案进行横向比较，突出系统在性能、风险与效率之间的综合权衡能力。",
    badges=["多方案比较", "性能-风险权衡", "决策辅助"],
)

results = get_latest_results()
compare_df = results["compare_df"]

best_density_plan = compare_df.loc[compare_df["预测致密度(%)"].idxmax(), "方案"]
lowest_risk_plan = compare_df.loc[compare_df["综合风险"].idxmin(), "方案"]
best_efficiency_plan = compare_df.loc[compare_df["成形效率"].idxmax(), "方案"]
current_row = compare_df[compare_df["方案"] == "当前方案"].iloc[0]

st.markdown("### 对比摘要")
c1, c2, c3, c4 = st.columns(4)
with c1:
    render_metric_card("最高致密度方案", best_density_plan)
with c2:
    render_metric_card("最低风险方案", lowest_risk_plan)
with c3:
    render_metric_card("最高效率方案", best_efficiency_plan)
with c4:
    render_metric_card("当前方案风险", f'{current_row["综合风险"]:.1f}')

st.markdown("### 多方案指标表")
st.dataframe(compare_df, use_container_width=True, hide_index=True)

left, right = st.columns(2)

with left:
    density_chart = px.bar(
        compare_df,
        x="方案",
        y="预测致密度(%)",
        color="方案",
        color_discrete_sequence=["#9ab3cb", "#3d6f96", "#27455f"],
        title="不同方案的预测致密度",
        text="预测致密度(%)",
    )
    density_chart.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    density_chart.update_traces(textposition="outside")
    st.plotly_chart(density_chart, use_container_width=True)

with right:
    balance_chart = px.scatter(
        compare_df,
        x="综合风险",
        y="成形效率",
        size="预测致密度(%)",
        color="方案",
        color_discrete_sequence=["#9ab3cb", "#3d6f96", "#27455f"],
        title="风险—效率—致密度综合分布",
        size_max=45,
    )
    balance_chart.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="综合风险",
        yaxis_title="成形效率",
    )
    st.plotly_chart(balance_chart, use_container_width=True)

st.markdown("### 对比分析解读")
a1, a2, a3 = st.columns(3)

with a1:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">保守方案</div>
            <p>更强调低风险与稳定性，适合作为初始试验或安全边界展示方案。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with a2:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">当前方案</div>
            <p>用于体现系统如何在性能、风险与效率之间进行折中，是最适合答辩讲解的核心方案。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with a3:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">激进方案</div>
            <p>更强调效率提升与工艺推进速度，但往往伴随更高的缺陷暴露概率。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

bottom_left, bottom_right = st.columns([1.1, 1])

with bottom_left:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">当前方案定位</div>
            <p><strong>预测致密度：</strong>{current_row["预测致密度(%)"]:.2f}%</p>
            <p><strong>综合风险：</strong>{current_row["综合风险"]:.1f}</p>
            <p><strong>成形效率：</strong>{current_row["成形效率"]:.1f}</p>
            <p>当前方案最适合用于答辩中说明：系统并不是单纯追求某一个指标最优，而是在多个目标之间寻找平衡解。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with bottom_right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">适合答辩的表达方式</div>
            <div class="timeline-item"><strong>先给出表格：</strong>让评委快速看到多方案并列比较。</div>
            <div class="timeline-item"><strong>再展示柱状图：</strong>突出致密度差异。</div>
            <div class="timeline-item"><strong>最后展示散点图：</strong>说明系统如何在风险、效率与性能之间做综合权衡。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
