import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_metric_card


st.set_page_config(
    page_title="陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统",
    layout="wide",
)

ensure_session_state()
apply_theme()

latest = get_latest_results()
params = st.session_state["input_params"]
max_risk = max(latest["crack_risk"], latest["pore_risk"], latest["warpage_risk"])

if max_risk >= 70:
    risk_tone = "high"
    risk_hint = "高风险窗口，建议优先降热梯度"
elif max_risk >= 45:
    risk_tone = "medium"
    risk_hint = "中风险窗口，可继续迭代优化"
else:
    risk_tone = "low"
    risk_hint = "低风险窗口，工艺稳定性较好"

st.markdown(
    f"""
    <div class="hero home-hero">
        <div class="hero-layout">
            <div>
                <h1 class="hero-title">陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统</h1>
                <p class="hero-subtitle">
                    面向中国研究生电子设计竞赛答辩展示，围绕“参数输入 → 热力预测 → 风险评估 → 方案对比 → 智能推荐”构建机理驱动决策闭环，
                    以可解释指标支撑工艺调参与方案选择。
                </p>
                <div class="hero-tags">
                    <span class="tag">机理驱动</span>
                    <span class="tag">热力预测</span>
                    <span class="tag">裂纹风险</span>
                    <span class="tag">可解释推荐</span>
                </div>
            </div>
            <div class="hero-state-grid">
                <div class="hero-state-card">
                    <p class="hero-state-title">机理驱动</p>
                    <p class="hero-state-value">规则库 + 模拟引擎协同</p>
                </div>
                <div class="hero-state-card">
                    <p class="hero-state-title">热力预测</p>
                    <p class="hero-state-value">峰值温度 {latest["peak_temp"]:.1f} ℃</p>
                </div>
                <div class="hero-state-card">
                    <p class="hero-state-title">裂纹风险</p>
                    <p class="hero-state-value">{latest["crack_risk"]:.1f} / 100</p>
                </div>
                <div class="hero-state-card">
                    <p class="hero-state-title">可解释推荐</p>
                    <p class="hero-state-value">推荐指数 {latest["recommendation_score"]:.1f}/100</p>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### 驾驶舱指标")
col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("当前方案", latest["plan_name"], "当前输入参数映射方案", icon="⌁")
with col2:
    render_metric_card(
        "预测致密度",
        f'{latest["density"]:.2f}%',
        "目标区间：95% 以上",
        tone="positive" if latest["density"] >= 95 else "medium",
        icon="◉",
    )
with col3:
    render_metric_card(
        "综合风险",
        f'{latest["risk_level"]} · {max_risk:.1f}',
        risk_hint,
        tone=risk_tone,
        icon="⚠",
    )
with col4:
    render_metric_card(
        "推荐指数",
        f'{latest["recommendation_score"]:.1f}/100',
        "综合致密度、风险与效率",
        tone="positive" if latest["recommendation_score"] >= 75 else "medium",
        icon="◎",
    )

left, right = st.columns([1.5, 1])
with left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">系统流程图</div>
            <div class="section-subtitle">参数输入 → 热力预测 → 风险评估 → 方案对比 → 智能推荐</div>
            <div class="flow-track">
                <div class="flow-step">
                    <span class="flow-index">STEP 01</span>
                    <span class="flow-title">参数输入</span>
                </div>
                <span class="flow-arrow">→</span>
                <div class="flow-step">
                    <span class="flow-index">STEP 02</span>
                    <span class="flow-title">热力预测</span>
                </div>
                <span class="flow-arrow">→</span>
                <div class="flow-step">
                    <span class="flow-index">STEP 03</span>
                    <span class="flow-title">风险评估</span>
                </div>
                <span class="flow-arrow">→</span>
                <div class="flow-step">
                    <span class="flow-index">STEP 04</span>
                    <span class="flow-title">方案对比</span>
                </div>
                <span class="flow-arrow">→</span>
                <div class="flow-step">
                    <span class="flow-index">STEP 05</span>
                    <span class="flow-title">智能推荐</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="card" style="margin-top: 0.9rem;">
            <div class="section-title">答辩演示路径建议</div>
            <div class="timeline-item"><strong>1.</strong> 参数输入页：录入打印、烧结与材料参数。</div>
            <div class="timeline-item"><strong>2.</strong> 热力预测页：展示温度场、热梯度与收缩率。</div>
            <div class="timeline-item"><strong>3.</strong> 风险评估页：聚焦裂纹、孔隙、翘曲三类风险。</div>
            <div class="timeline-item"><strong>4.</strong> 方案对比页：说明保守、均衡、激进策略差异。</div>
            <div class="timeline-item"><strong>5.</strong> 推荐结果页：输出推荐工艺与解释依据。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">当前输入摘要</div>
            <p>层厚：<strong>{params["layer_thickness"]:.0f} μm</strong></p>
            <p>打印速度：<strong>{params["print_speed"]:.0f} mm/s</strong></p>
            <p>激光功率：<strong>{params["laser_power"]:.0f} W</strong></p>
            <p>烧结温度：<strong>{params["sinter_temp"]:.0f} ℃</strong></p>
            <p>保温时间：<strong>{params["holding_time"]:.1f} h</strong></p>
            <p>浆料固含量：<strong>{params["solid_content"]:.0f}%</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="card" style="margin-top: 0.9rem;">
            <div class="section-title">展示焦点</div>
            <div class="timeline-item">机理驱动：规则与数据协同，形成可解释工艺决策链。</div>
            <div class="timeline-item">热力预测：从输入参数映射峰值温度与热梯度变化。</div>
            <div class="timeline-item">风险控制：突出裂纹风险与综合风险窗口判定逻辑。</div>
            <div class="timeline-item">智能推荐：以推荐指数支撑方案采纳与优化。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.info("请从左侧侧边栏依次进入各页面；如需更新分析结果，先在“参数输入页”点击“生成模拟结果”。")
