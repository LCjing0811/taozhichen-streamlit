import plotly.graph_objects as go
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="风险评估", page_icon="⚠️", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "风险评估",
    "对裂纹、孔隙、翘曲等关键失效模式进行模拟评估，形成风险画像与解释性判读结果。",
    badges=["缺陷风险识别", "风险画像", "解释性预警"],
)

results = get_latest_results()
risk_max = max(results["crack_risk"], results["pore_risk"], results["warpage_risk"])

st.markdown("### 风险总览")
c1, c2, c3, c4 = st.columns(4)
with c1:
    render_metric_card("综合风险等级", results["risk_level"])
with c2:
    render_metric_card("裂纹风险", f'{results["crack_risk"]:.1f}')
with c3:
    render_metric_card("孔隙风险", f'{results["pore_risk"]:.1f}')
with c4:
    render_metric_card("翘曲风险", f'{results["warpage_risk"]:.1f}')

left, right = st.columns([1.1, 1])

with left:
    radar = go.Figure()
    radar.add_trace(
        go.Scatterpolar(
            r=[
                results["crack_risk"],
                results["pore_risk"],
                results["warpage_risk"],
                results["thermal_gradient"],
            ],
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
    st.plotly_chart(radar, use_container_width=True)

with right:
    bar = go.Figure()
    bar.add_trace(
        go.Bar(
            x=["裂纹风险", "孔隙风险", "翘曲风险"],
            y=[results["crack_risk"], results["pore_risk"], results["warpage_risk"]],
            marker=dict(color=["#3d6f96", "#5c84a5", "#8da9c4"]),
            text=[
                f'{results["crack_risk"]:.1f}',
                f'{results["pore_risk"]:.1f}',
                f'{results["warpage_risk"]:.1f}',
            ],
            textposition="outside",
        )
    )
    bar.update_layout(
        title="三类缺陷风险对比",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="风险值",
        margin=dict(l=20, r=20, t=60, b=20),
    )
    st.plotly_chart(bar, use_container_width=True)

st.markdown("### 风险判读面板")
r1, r2, r3 = st.columns(3)

with r1:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">裂纹风险解释</div>
            <p style="font-size:1.55rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{results["crack_risk"]:.1f}</p>
            <p style="margin:0;">主要受热梯度、烧结温度与保温时间影响。当前状态为
            <strong>{"高关注" if results["crack_risk"] >= 60 else "中等关注" if results["crack_risk"] >= 40 else "较稳健"}</strong>。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with r2:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">孔隙风险解释</div>
            <p style="font-size:1.55rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{results["pore_risk"]:.1f}</p>
            <p style="margin:0;">主要受浆料固含量与烧结致密化能力影响。当前状态为
            <strong>{"高关注" if results["pore_risk"] >= 60 else "中等关注" if results["pore_risk"] >= 40 else "较稳健"}</strong>。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with r3:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">翘曲风险解释</div>
            <p style="font-size:1.55rem;font-weight:700;color:#284a66;margin:0 0 0.4rem 0;">{results["warpage_risk"]:.1f}</p>
            <p style="margin:0;">主要受扫描间距、打印速度和局部热输入均匀性影响。当前状态为
            <strong>{"高关注" if results["warpage_risk"] >= 60 else "中等关注" if results["warpage_risk"] >= 40 else "较稳健"}</strong>。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

bottom_left, bottom_right = st.columns([1.15, 1])

risk_text = {
    "高风险": "当前参数组合存在较明显的缺陷暴露概率，建议优先调整热输入与烧结制度，再进入推荐页面查看优化路径。",
    "中风险": "当前方案可用于演示与试验验证，但仍建议结合方案对比与推荐页给出的修正策略进一步收窄风险窗口。",
    "低风险": "当前参数窗口较稳健，适合作为答辩中的优选或基准方案，能够体现系统对风险可控性的判断能力。",
}

with bottom_left:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">综合风险结论</div>
            <p>{risk_text[results["risk_level"]]}</p>
            <p><strong>当前最高风险值：</strong>{risk_max:.1f}，因此系统将本方案判定为<strong>{results["risk_level"]}</strong>。</p>
            <p>这一页适合在答辩中说明：系统不仅会“推荐”，还会先识别缺陷风险，再给出推荐依据。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with bottom_right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">建议讲解逻辑</div>
            <div class="timeline-item"><strong>先展示雷达图：</strong>快速说明风险分布轮廓。</div>
            <div class="timeline-item"><strong>再展示柱状图：</strong>对比三类缺陷谁最突出。</div>
            <div class="timeline-item"><strong>最后展示解释面板：</strong>说明每类风险分别由哪些工艺因素触发。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
