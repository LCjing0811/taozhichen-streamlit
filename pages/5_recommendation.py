import plotly.graph_objects as go
import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="智能推荐", page_icon="🎯", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "智能推荐",
    "基于模拟预测与风险评估结果，输出当前工艺方案的推荐等级、优化建议与可解释决策依据。",
    badges=["推荐结论", "优化建议", "可解释逻辑"],
)

results = get_latest_results()
params = st.session_state["input_params"]

score = results["recommendation_score"]
risk_level = results["risk_level"]

if score >= 85 and risk_level == "低风险":
    verdict = "优先推荐采用"
    verdict_desc = "当前方案在性能、风险与效率之间形成了较优平衡，适合用作展示中的主推方案。"
elif score >= 75:
    verdict = "建议采用"
    verdict_desc = "当前方案总体表现较好，可作为展示中的核心方案，并结合优化建议进一步增强说服力。"
else:
    verdict = "建议优化后采用"
    verdict_desc = "当前方案仍具备展示价值，但建议先根据系统提示进行参数修正，再作为最终推荐结果输出。"

st.markdown("### 推荐结果总览")
c1, c2, c3, c4 = st.columns(4)
with c1:
    render_metric_card("推荐指数", f"{score:.1f}/100")
with c2:
    render_metric_card("预测致密度", f'{results["density"]:.2f}%')
with c3:
    render_metric_card("综合风险", risk_level)
with c4:
    render_metric_card("推荐结论", verdict)

left, right = st.columns([1.2, 1])

with left:
    st.markdown(
        f"""
        <div class="card" style="padding:1.35rem 1.35rem;">
            <div class="section-kicker">最终输出</div>
            <div class="section-title" style="font-size:1.28rem;">{verdict}</div>
            <p style="font-size:1rem;line-height:1.8;margin-bottom:0.6rem;">{verdict_desc}</p>
            <p style="margin:0;"><strong>系统判断依据：</strong>综合考虑预测致密度、成形效率以及裂纹/孔隙/翘曲等缺陷风险后，形成当前推荐分数与结论。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "推荐指数"},
            number={"suffix": "/100"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#3d6f96"},
                "steps": [
                    {"range": [0, 60], "color": "#dce8f2"},
                    {"range": [60, 80], "color": "#b8cfe1"},
                    {"range": [80, 100], "color": "#8da9c4"},
                ],
            },
        )
    )
    gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=60, b=20),
        height=320,
    )
    st.plotly_chart(gauge, use_container_width=True)

st.markdown("### 推荐工艺摘要")
g1, g2 = st.columns([1.1, 1])

with g1:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">当前工艺参数</div>
            <div class="two-col-grid">
                <div class="mini-stat"><span>层厚</span><strong>{params["layer_thickness"]:.0f} μm</strong></div>
                <div class="mini-stat"><span>打印速度</span><strong>{params["print_speed"]:.0f} mm/s</strong></div>
                <div class="mini-stat"><span>激光功率</span><strong>{params["laser_power"]:.0f} W</strong></div>
                <div class="mini-stat"><span>扫描间距</span><strong>{params["scan_spacing"]:.2f} mm</strong></div>
                <div class="mini-stat"><span>烧结温度</span><strong>{params["sinter_temp"]:.0f} ℃</strong></div>
                <div class="mini-stat"><span>保温时间</span><strong>{params["holding_time"]:.1f} h</strong></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with g2:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">可解释决策逻辑</div>
            <p><strong>1. 性能目标：</strong>预测致密度与热稳定性是否达到展示要求。</p>
            <p><strong>2. 风险约束：</strong>裂纹、孔隙、翘曲是否处于可接受窗口。</p>
            <p><strong>3. 效率目标：</strong>工艺效率是否满足增材制造场景下的应用预期。</p>
            <p><strong>4. 综合平衡：</strong>系统并非单点最优，而是追求多目标综合最优。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### 优化建议")
for i, tip in enumerate(results["recommendations"], start=1):
    st.markdown(
        f"""
        <div class="card" style="margin-bottom:0.8rem;">
            <div class="section-title" style="margin-bottom:0.45rem;">建议 {i}</div>
            <p style="margin:0;">{tip}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

bottom_left, bottom_right = st.columns([1.15, 1])

with bottom_left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">答辩收束建议</div>
            <div class="timeline-item"><strong>先给结论：</strong>明确当前方案是否推荐采用。</div>
            <div class="timeline-item"><strong>再给依据：</strong>说明推荐指数、风险等级和性能指标如何共同支持这个结论。</div>
            <div class="timeline-item"><strong>最后给优化路径：</strong>体现系统不仅会判断，还能指导后续改进。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with bottom_right:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">本页展示价值</div>
            <p>这一页适合作为整套系统展示的收束页。</p>
            <p><strong>推荐指数：</strong>{score:.1f}/100</p>
            <p><strong>风险等级：</strong>{risk_level}</p>
            <p><strong>核心意义：</strong>把前面多个页面中的预测、评估与对比结果，最终汇总为可解释、可表达、可展示的工艺推荐结论。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.success("当前页面适合作为比赛答辩的结尾页，用于输出最终推荐结论、优化建议与可解释依据。")
