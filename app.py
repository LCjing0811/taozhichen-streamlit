from pathlib import Path

import streamlit as st

from utils.mock_engine import ensure_session_state, get_latest_results
from utils.theme import apply_theme, render_metric_card


SYSTEM_TITLE = "陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统"
COMPETITION_NAME = "第二十一届中国研究生电子设计竞赛"
TEAM_NAME = "陶智沉研队"
TEAM_SLOGAN = "以机理驱动决策，以智能赋能制造"
TEAM_MEMBERS = "团队成员：刘心蕊、刘成景、马金涛"
ADVISOR_INFO = "指导教师：刘保平"
LOGO_PATH = Path("assets/logo.png")

st.set_page_config(
    page_title=SYSTEM_TITLE,
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

ensure_session_state()
apply_theme()


def render_sidebar_branding() -> None:
    with st.sidebar:
        st.markdown('<div class="sidebar-brand-wrap">', unsafe_allow_html=True)

        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), width=92)
        else:
            st.markdown(
                """
                <div class="logo-shell">
                    <div class="logo-fallback">陶智沉</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="sidebar-brand-title">{SYSTEM_TITLE}</div>
            <div class="sidebar-brand-subtitle">竞赛展示型交互原型系统</div>

            <div class="sidebar-info-card">
                <div class="sidebar-info-label">比赛名称</div>
                <div class="sidebar-info-value">{COMPETITION_NAME}</div>
            </div>

            <div class="sidebar-info-card">
                <div class="sidebar-info-label">团队名称</div>
                <div class="sidebar-info-value">{TEAM_NAME}</div>
                <div class="sidebar-info-desc">{TEAM_SLOGAN}</div>
            </div>

            <div class="sidebar-info-card">
                <div class="sidebar-info-label">团队成员</div>
                <div class="sidebar-info-desc">{TEAM_MEMBERS}</div>
                <div class="sidebar-info-desc">{ADVISOR_INFO}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)


def render_homepage() -> None:
    latest = get_latest_results()
    params = st.session_state["input_params"]

    hero_left, hero_right = st.columns([4.3, 1.2])

    with hero_left:
        st.markdown(
            f"""
            <div class="hero">
                <h1>{SYSTEM_TITLE}</h1>
                <p>
                    面向{COMPETITION_NAME}展示场景构建的交互式原型系统，
                    围绕氧化铝陶瓷增材制造过程中的参数输入、热力预测、风险评估、
                    方案对比与智能推荐，形成可解释、可交互、可展示的工艺决策闭环。
                </p>
                <div class="hero-badges">
                    <span class="hero-badge">机理驱动决策</span>
                    <span class="hero-badge">多页面联动</span>
                    <span class="hero-badge">可解释推荐</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with hero_right:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)
        else:
            st.markdown(
                """
                <div class="card" style="text-align:center;padding:1.4rem 1rem;">
                    <div class="logo-shell" style="margin:0 auto 0.9rem auto;">
                        <div class="logo-fallback">陶智沉</div>
                    </div>
                    <p style="margin:0;color:#5f7285;">系统首页</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### 赛事与项目概览")
    g1, g2, g3 = st.columns(3)

    with g1:
        st.markdown(
            f"""
            <div class="meta-box">
                <div class="meta-label">比赛名称</div>
                <div class="meta-value">{COMPETITION_NAME}</div>
                <div class="meta-desc">面向竞赛答辩、成果展示与项目汇报</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with g2:
        st.markdown(
            f"""
            <div class="meta-box">
                <div class="meta-label">团队名称</div>
                <div class="meta-value">{TEAM_NAME}</div>
                <div class="meta-desc">{TEAM_SLOGAN}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with g3:
        st.markdown(
            """
            <div class="meta-box">
                <div class="meta-label">项目定位</div>
                <div class="meta-value">机理驱动的智能工艺决策原型</div>
                <div class="meta-desc">服务氧化铝陶瓷增材制造过程优化</div>
            </div>
            """,
            unsafe_allow_html=True,
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

    st.markdown("### 项目核心创新")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">创新点一</div>
                <div class="section-title">面向复杂工艺场景的问题抽象</div>
                <p>针对氧化铝陶瓷增材制造过程中参数耦合复杂、试错成本高、缺陷风险难以直观判断等问题，构建从参数到推荐的一体化展示原型。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">创新点二</div>
                <div class="section-title">机理逻辑与智能推荐相结合</div>
                <p>系统围绕热行为、缺陷风险与工艺性能之间的关联逻辑展开，融合参数联动、风险评估与推荐输出，形成可解释的智能工艺决策框架。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="showcase-card">
                <div class="section-kicker">创新点三</div>
                <div class="section-title">兼顾技术深度与竞赛呈现</div>
                <p>该系统不仅体现工艺理解与决策思维，也通过统一界面、完整链路和直观可视化增强答辩表现力，提升项目完成度与说服力。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 系统功能闭环")
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

    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("### 系统能力矩阵")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">三类核心能力</div>
                <div class="timeline-item"><strong>技术能力：</strong>体现热力预测、风险判读与参数联动分析逻辑。</div>
                <div class="timeline-item"><strong>系统能力：</strong>体现多页面组织、交互逻辑与统一视觉风格。</div>
                <div class="timeline-item"><strong>应用能力：</strong>体现面向制造场景的辅助决策与成果转化潜力。</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown("### 讲解逻辑")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">讲述顺序</div>
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

    bottom_left, bottom_right = st.columns([1.15, 1])

    with bottom_left:
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

    with bottom_right:
        st.markdown("### 展示关键词")
        st.markdown(
            """
            <div class="card">
                <div class="section-title">重点</div>
                <span class="tag">机理驱动决策</span>
                <span class="tag">智能工艺优化</span>
                <span class="tag">陶瓷增材制造</span>
                <span class="tag">热力预测分析</span>
                <span class="tag">缺陷风险预警</span>
                <span class="tag">交互式展示系统</span>
                <p style="margin-top:0.8rem;">建议围绕“技术原理清晰、系统架构完整、应用场景明确、展示表达直观”四点展开答辩。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
  st.markdown(
        """
        <div class="note-callout">
            聚焦氧化铝陶瓷激光增材制造中的热力预测、风险评估与工艺优选，致力于将已验证的科研成果转化为可展示、可交互、可解释的智能工艺决策原理系统。
        </div>
        """,
        unsafe_allow_html=True,
    )

render_sidebar_branding()

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
