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
        "面向竞赛答辩、项目路演与课程汇报场景的交互式原型系统，围绕参数输入、热力预测、风险评估、方案对比与智能推荐，构建可解释的工艺决策展示闭环。",
        badges=["竞赛展示原型", "中文交互", "多页面联动", "可解释推荐", "蓝灰科技风"],
    )

    st.markdown("### 核心指标总览")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("当前方案", latest["plan_name"])
    with col2:
        render_metric_card("预测致密度", f'{latest["density"]:.2f}%')
    with col3:
        render_metric_card("综合风险", latest["risk_level"])
    with col4:
        render_metric_card("推荐指数", f'{latest["recommendation_score"]:.1f}/100')

    st.markdown("### 项目展示亮点")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">项目定位</div>
                <div class="section-title">服务陶瓷增材制造工艺决策展示</div>
                <p>围绕氧化铝陶瓷成形与烧结过程，构建“输入—预测—评估—推荐”的完整演示链路，使抽象工艺优化过程具备可视化与可讲解性。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">核心创新</div>
                <div class="section-title">多页面联动与可解释推荐结合</div>
                <p>通过 session_state 实现输入参数在多个页面间联动传递，形成系统级交互原型，而非单一页面静态展示，突出“决策系统”特征。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">展示价值</div>
                <div class="section-title">同时体现技术逻辑与应用价值</div>
                <p>既能够说明工艺参数如何影响热行为与缺陷风险，也能展示推荐结论如何服务制造场景，适合作为比赛答辩首页与项目封面页。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 系统流程闭环")
    flow_cols = st.columns(5)
    flow_data = [
        ("01", "参数输入", "录入铺层厚度、打印速度、激光功率、烧结温度等关键工艺参数。"),
        ("02", "热力预测", "展示温度场、热历程、热梯度与收缩率等核心热学结果。"),
        ("03", "风险评估", "识别裂纹、孔隙、翘曲等关键缺陷风险并形成风险画像。"),
        ("04", "方案对比", "横向比较保守、均衡、激进三类工艺路径的综合表现。"),
        ("05", "智能推荐", "输出推荐工艺、优化建议与可解释决策依据。"),
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
                    <div class="mini-stat"><span>浆料固含量</span><strong>{params["solid_content"]:.0f}%</strong></div>
                    <div class="mini-stat"><span>粘结剂比例</span><strong>{params["binder_ratio"]:.1f}%</strong></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 系统定位说明")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">原型系统说明</div>
                <p>当前系统基于模拟规则与演示数据构建，重点用于呈现未来“真实工艺数据 + 热力模型 + 智能推荐算法”接入后的可视化承载形式。</p>
                <p>因此，它既是一个答辩展示样机，也可作为后续算法系统开发的前端原型基础。</p>
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
                    <li>先说明项目背景：陶瓷增材制造工艺参数复杂、试错成本高。</li>
                    <li>再说明系统目标：构建可解释的工艺辅助决策展示平台。</li>
                    <li>随后演示参数输入变化如何驱动热力预测与风险评估联动。</li>
                    <li>最后通过推荐页收束，突出“智能推荐 + 可解释依据”。</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### 比赛展示价值")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">适合展示的三类能力</div>
                <p><strong>1. 技术能力：</strong>体现热力预测、风险判读与参数联动分析框架。</p>
                <p><strong>2. 系统能力：</strong>体现多页面组织、交互逻辑与统一视觉风格。</p>
                <p><strong>3. 应用能力：</strong>体现面向制造场景的辅助决策与成果转化潜力。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 页面使用建议")
    p1, p2 = st.columns(2)
    with p1:
        st.markdown(
            """
            <div class="card">
                <div class="section-title">建议演示路径</div>
                <div class="timeline-item"><strong>第一页：</strong>进入参数输入，调整激光功率、层厚、烧结温度。</div>
                <div class="timeline-item"><strong>第二页：</strong>展示热力预测结果如何随输入变化。</div>
                <div class="timeline-item"><strong>第三页：</strong>说明裂纹、孔隙、翘曲风险的来源。</div>
                <div class="timeline-item"><strong>第四页：</strong>横向比较不同方案之间的取舍关系。</div>
                <div class="timeline-item"><strong>第五页：</strong>给出推荐结论和优化建议，形成闭环。</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with p2:
        st.markdown(
            """
            <div class="card">
                <div class="section-title">适合答辩时强调的关键词</div>
                <span class="tag">可解释智能决策</span>
                <span class="tag">陶瓷增材制造</span>
                <span class="tag">热力耦合展示</span>
                <span class="tag">缺陷风险预警</span>
                <span class="tag">多方案对比</span>
                <span class="tag">交互式原型系统</span>
                <p style="margin-top:0.8rem;">可围绕“技术逻辑清晰、展示链路完整、应用场景明确”三点展开讲解。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="note-callout">
            建议答辩演示顺序：先进入“参数输入”修改关键参数，再依次展示“热力预测”“风险评估”“方案对比”“智能推荐”，形成完整叙事闭环。
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
