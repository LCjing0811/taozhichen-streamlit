import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="热力预测", page_icon="🌡️", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "热力预测",
    "基于当前工艺输入生成模拟温度场、热历程曲线与关键热学指标，用于演示系统的热力耦合预测展示能力。",
    badges=["温度场可视化", "热历程曲线", "热学指标解读"],
)

results = get_latest_results()

uniformity_score = max(
    0,
    min(100, 100 - results["thermal_gradient"] * 2.1 - abs(results["shrinkage"] - 16) * 5.5),
)
heat_input_index = max(
    0,
    min(100, 0.38 * results["peak_temp"] / 10 + 0.8 * results["thermal_gradient"]),
)

st.markdown("### 热学核心指标")
c1, c2, c3, c4 = st.columns(4)
with c1:
    render_metric_card("峰值温度", f'{results["peak_temp"]:.1f} ℃')
with c2:
    render_metric_card("热梯度指数", f'{results["thermal_gradient"]:.1f}')
with c3:
    render_metric_card("预测收缩率", f'{results["shrinkage"]:.2f}%')
with c4:
    render_metric_card("热均匀性评分", f"{uniformity_score:.1f}/100")

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
        coloraxis_colorbar=dict(title="温度"),
    )
    st.plotly_chart(heatmap, use_container_width=True)

with right:
    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=results["thermal_gradient"],
            title={"text": "热梯度状态"},
            number={"suffix": ""},
            gauge={
                "axis": {"range": [0, 35]},
                "bar": {"color": "#3d6f96"},
                "steps": [
                    {"range": [0, 16], "color": "#dce8f2"},
                    {"range": [16, 24], "color": "#b8cfe1"},
                    {"range": [24, 35], "color": "#8da9c4"},
                ],
            },
        )
    )
    gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
        height=340,
    )
    st.plotly_chart(gauge, use_container_width=True)

tabs = st.tabs(["热历程曲线", "热学指标解读", "展示说明"])

with tabs[0]:
    temp_curve = results["temp_curve"]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=temp_curve["时间(min)"],
            y=temp_curve["温度(℃)"],
            mode="lines+markers",
            line=dict(color="#3d6f96", width=4),
            marker=dict(size=8, color="#27455f"),
            fill="tozeroy",
            fillcolor="rgba(61,111,150,0.12)",
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

with tabs[1]:
    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown(
            f"""
            <div class="card">
                <div class="section-title">热输入指数</div>
                <p style="font-size:1.6rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{heat_input_index:.1f}</p>
                <p style="margin:0;">综合反映峰值温度与热梯度水平，数值越高表示局部热作用越强。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k2:
        st.markdown(
            f"""
            <div class="card">
                <div class="section-title">热稳定性判断</div>
                <p style="font-size:1.6rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{"较优" if uniformity_score >= 70 else "一般" if uniformity_score >= 50 else "偏弱"}</p>
                <p style="margin:0;">用于辅助解释温度场是否均匀，是否容易在后续阶段诱发热应力集中。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with k3:
        st.markdown(
            f"""
            <div class="card">
                <div class="section-title">收缩行为特征</div>
                <p style="font-size:1.6rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{"可控" if 14 <= results["shrinkage"] <= 18 else "需关注"}</p>
                <p style="margin:0;">收缩率过高或过低都可能影响致密化一致性与尺寸稳定性。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tabs[2]:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">页面展示建议</div>
            <div class="timeline-item"><strong>先看温度场：</strong>用于说明局部热输入分布和区域差异。</div>
            <div class="timeline-item"><strong>再看热历程：</strong>用于说明烧结过程中温度上升与回落的整体趋势。</div>
            <div class="timeline-item"><strong>最后看指标解读：</strong>把抽象热学结果转成便于答辩表达的语言。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

bottom_left, bottom_right = st.columns([1.15, 1])

with bottom_left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">结果解读</div>
            <p>系统将工艺输入映射为热输入强度、烧结热历程和局部温度分布。当前版本采用模拟逻辑，但页面结构已经能够承载未来接入有限元仿真或机器学习代理模型后的真实结果展示。</p>
            <p>在比赛答辩中，这一页的作用是证明系统不仅能给出推荐结果，还能展示推荐背后的热学依据。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with bottom_right:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">当前热学结论</div>
            <p><strong>峰值温度：</strong>{results["peak_temp"]:.1f} ℃，表明当前热输入处于{"较高" if results["peak_temp"] >= 950 else "适中"}水平。</p>
            <p><strong>热梯度指数：</strong>{results["thermal_gradient"]:.1f}，说明局部温差{"较明显" if results["thermal_gradient"] >= 24 else "相对可控"}。</p>
            <p><strong>预测收缩率：</strong>{results["shrinkage"]:.2f}%，用于辅助判断后续尺寸收敛与烧结稳定性。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
