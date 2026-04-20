import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(
    page_title="陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

ensure_session_state()
apply_theme()


def render_homepage() -> None:
    latest = get_latest_results()
    params = st.session_state["input_params"]

    render_header(
        "陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统",
        "面向创新创业与学科竞赛答辩场景的交互式原型系统，围绕参数输入、热力预测、风险评估、方案对比与智能推荐，构建可解释的工艺决策展示链路。",
        badges=["竞赛答辩样机", "中文交互界面", "可解释推荐", "蓝灰科技风"],
    )

    st.markdown("### 项目总览")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("当前方案", latest["plan_name"])
    with col2:
        render_metric_card("预测致密度", f'{latest["density"]:.2f}%')
    with col3:
        render_metric_card("综合风险", latest["risk_level"])
    with col4:
        render_metric_card("推荐指数", f'{latest["recommendation_score"]:.1f}/100')

    st.markdown("### 展示亮点")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">项目定位</div>
                <div class="section-title">聚焦氧化铝陶瓷增材制造工艺决策</div>
                <p>系统将工艺参数、热力预测、缺陷风险与推荐结论贯通为一条连续的展示主线，适合用于比赛答辩、课程汇报与项目路演。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">核心能力</div>
                <div class="section-title">从输入到推荐的全流程联动</div>
                <p>支持通过 session_state 在多个页面之间共享参数与模拟结果，体现系统级决策逻辑，而不是单页静态展示。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">答辩价值</div>
                <div class="section-title">同时展示技术逻辑与应用价值</div>
                <p>既能体现可解释智能决策框架，也能直观呈现制造场景下的可视化表达能力，适合作为竞赛展示原型。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 系统流程")
    flow_cols = st.columns(5)
    flow_data = [
        ("01", "参数输入", "录入铺层厚度、打印速度、激光功率、烧结温度等关键参数。"),
        ("02", "热力预测", "展示温度场、热历程、热梯度与收缩率等热学结果。"),
        ("03", "风险评估", "识别裂纹、孔隙、翘曲等缺陷风险，形成风险画像。"),
        ("04", "方案对比", "横向比较保守、均衡、激进三类工艺路径的差异。"),
        ("05", "智能推荐", "输出推荐结论、优化建议与可解释决策依据。"),
    ]
    for col, (idx, title, desc) in zip(flow_cols, flow_data):
        with col:
            st.markdown(
                f"""
                <div class="flow-step">
                    <div class="flow-index">{idx}</div>
                    <div class="flow-title">{title}</div>
                    <div class="flow-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    left, right = st.columns([1.15, 1])
    with left:
        st.markdown("### 当前参数快照")
        st.markdown(
            f"""
            <div class="card">
                <div class="section-title">核心工艺参数</div>
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
    with right:
        st.markdown("### 答辩讲解重点")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">推荐讲述顺序</div>
                <ul class="compact-list">
                    <li>先说明系统服务对象：氧化铝陶瓷增材制造工艺优化与展示决策。</li>
                    <li>再强调系统价值：把“输入—预测—评估—推荐”做成完整闭环。</li>
                    <li>演示中可修改参数，突出不同页面结果会实时联动变化。</li>
                    <li>最后用推荐页收束，突出可解释性与应用落地价值。</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="note-callout">
            建议答辩演示顺序：先进入“参数输入”修改关键参数，再依次展示“热力预测”“风险评估”“方案对比”“智能推荐”，形成完整叙事链路。
        </div>
        """,
        unsafe_allow_html=True,
    )


pages = {
    "系统导航": [
        st.Page(render_homepage, title="首页", icon="🏠", default=True),
        st.Page("pages/1_parameter_input.py", title="参数输入", icon="🧪"),
        st.Page("pages/2_thermal_prediction.py", title="热力预测", icon="🌡️"),
        st.Page("pages/3_risk_assessment.py", title="风险评估", icon="⚠️"),
        st.Page("pages/4_scheme_comparison.py", title="方案对比", icon="📊"),
        st.Page("pages/5_recommendation.py", title="智能推荐", icon="🎯"),
    ]
}

current_page = st.navigation(pages, position="sidebar", expanded=True)
current_page.run()
