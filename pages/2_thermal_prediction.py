import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="热力预测结果页", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "热力预测结果页",
    "基于当前工艺输入生成模拟温度场、热历程曲线和关键热学指标，用于演示热力耦合预测能力。",
)

results = get_latest_results()

col1, col2, col3 = st.columns(3)
with col1:
    render_metric_card("峰值温度", f'{results["peak_temp"]:.1f} ℃')
with col2:
    render_metric_card("热梯度指数", f'{results["thermal_gradient"]:.1f}')
with col3:
    render_metric_card("预测收缩率", f'{results["shrinkage"]:.2f}%')

left, right = st.columns([1.2, 1])

with left:
    heatmap_df = results["heatmap_df"]
    heatmap = px.density_heatmap(
        heatmap_df,
        x="X",
        y="Y",
        z="温度场",
        histfunc="avg",
        nbinsx=12,
        nbinsy=12,
        color_continuous_scale="Blues",
        title="构件截面温度场分布（模拟）",
    )
    heatmap.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(heatmap, use_container_width=True)

with right:
    temp_curve = results["temp_curve"]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=temp_curve["时间(min)"],
            y=temp_curve["温度(℃)"],
            mode="lines+markers",
            line=dict(color="#3d6f96", width=4),
            marker=dict(size=8, color="#27455f"),
            name="热历程",
        )
    )
    fig.update_layout(
        title="烧结过程温度历程（模拟）",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="时间 (min)",
        yaxis_title="温度 (℃)",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    <div class="card">
        <div class="section-title">结果解读</div>
        <p>系统将工艺输入映射为热输入强度、烧结热历程和局部温度分布。该页面当前为模拟逻辑，但展示了后续接入真实有限元仿真或机器学习代理模型时的可视化承载方式。</p>
    </div>
    """,
    unsafe_allow_html=True,
)
