import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(
    page_title="陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统",
    layout="wide",
)

ensure_session_state()
apply_theme()

render_header(
    "陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统",
    "面向比赛答辩展示的多页面交互原理样机，基于模拟数据演示参数输入、热力预测、风险评估、方案对比与智能推荐的完整流程。",
)

latest = get_latest_results()

st.markdown("### 系统概览")
col1, col2, col3, col4 = st.columns(4)
with col1:
    render_metric_card("当前方案", latest["plan_name"])
with col2:
    render_metric_card("预测致密度", f'{latest["density"]:.2f}%')
with col3:
    render_metric_card("综合风险", latest["risk_level"])
with col4:
    render_metric_card("推荐指数", f'{latest["recommendation_score"]:.1f}/100')

left, right = st.columns([1.3, 1])
with left:
    st.markdown("### 演示路径")
    st.markdown(
        """
        <div class="card">
            <div class="section-title">建议演示顺序</div>
            <div class="timeline-item"><strong>1.</strong> 参数输入页：录入打印、烧结与材料参数</div>
            <div class="timeline-item"><strong>2.</strong> 热力预测结果页：查看温度场、收缩率与致密度预测</div>
            <div class="timeline-item"><strong>3.</strong> 风险评估页：识别裂纹、翘曲、孔隙等关键风险</div>
            <div class="timeline-item"><strong>4.</strong> 方案对比页：比较保守、均衡、激进三类工艺方案</div>
            <div class="timeline-item"><strong>5.</strong> 推荐结果页：输出推荐工艺与解释性决策依据</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown("### 当前输入摘要")
    params = st.session_state["input_params"]
    st.markdown(
        f"""
        <div class="card">
            <div class="section-title">核心参数</div>
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

st.info("请从左侧侧边栏依次进入各页面；如需更新分析结果，先在“参数输入页”点击“生成模拟结果”。")
