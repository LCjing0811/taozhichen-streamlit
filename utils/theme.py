    color: var(--text-sub);
    line-height: 1.55;
}

.timeline-item:last-child {
    border-bottom: none;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid rgba(110, 156, 232, 0.3);
    background: rgba(12, 32, 60, 0.58);
}

div[data-testid="stAlert"] p {
    color: #cbe2ff;
}

div[data-testid="stButton"] > button,
div[data-testid="stFormSubmitButton"] > button {
    border-radius: 12px;
    border: 1px solid rgba(107, 176, 255, 0.46);
    color: #e9f5ff;
    font-weight: 700;
    background: linear-gradient(135deg, rgba(43, 119, 201, 0.95), rgba(38, 86, 156, 0.95));
    box-shadow: 0 9px 22px rgba(6, 19, 37, 0.45);
}

div[data-testid="stButton"] > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    border-color: rgba(107, 214, 255, 0.72);
    background: linear-gradient(135deg, rgba(55, 134, 219, 0.98), rgba(45, 99, 173, 0.98));
}

[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border-radius: 14px;
    overflow: hidden;
}

@media (max-width: 1150px) {
    .hero-layout {
        grid-template-columns: 1fr;
    }

    .hero-state-grid {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 780px) {
    .home-hero {
        padding: 1.28rem 1.15rem;
    }

    .hero-state-grid {
        grid-template-columns: 1fr;
    }

    .metric-card {
        min-height: 116px;
    }
}
</style>
"""


def _render_sidebar_branding() -> None:
    st.sidebar.markdown(
        """
        <div class="sidebar-system">
            <div class="sys-title">陶智沉 决策系统</div>
            <div class="sys-sub">氧化铝陶瓷增材制造 · 答辩演示版</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_sidebar_navigation() -> None:
    if not hasattr(st, "page_link"):
        return

    with st.sidebar:
        st.markdown('<div class="sidebar-group-label">系统总览</div>', unsafe_allow_html=True)
        st.page_link("app.py", label="首页总览", icon=":material/home:")

        st.markdown('<div class="sidebar-group-label">工艺建模链路</div>', unsafe_allow_html=True)
        st.page_link("pages/1_parameter_input.py", label="参数输入", icon=":material/tune:")
        st.page_link("pages/2_thermal_prediction.py", label="热力预测", icon=":material/device_thermostat:")
        st.page_link("pages/3_risk_assessment.py", label="风险评估", icon=":material/shield:")
        st.page_link("pages/4_scheme_comparison.py", label="方案对比", icon=":material/table_chart:")

        st.markdown('<div class="sidebar-group-label">决策输出</div>', unsafe_allow_html=True)
        st.page_link("pages/5_recommendation.py", label="智能推荐", icon=":material/psychology:")


def apply_theme() -> None:
    st.markdown(THEME_CSS, unsafe_allow_html=True)
    _render_sidebar_branding()
    if hasattr(st, "page_link"):
        _render_sidebar_navigation()
    else:
        st.markdown(
            '<style>div[data-testid="stSidebarNav"] { display: block !important; }</style>',
            unsafe_allow_html=True,
        )


def render_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero">
            <h1>{escape(title)}</h1>
            <p>{escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(
    label: str,
    value: str,
    hint: str = "",
    tone: str = "",
    icon: str = "◈",
) -> None:
    tone_class = f"tone-{escape(tone)}" if tone else ""
    hint_block = f'<div class="metric-hint">{escape(hint)}</div>' if hint else ""

    st.markdown(
        f"""
        <div class="metric-card {tone_class}">
            <div class="metric-head">
                <span class="metric-icon">{escape(icon)}</span>
                <div class="metric-label">{escape(label)}</div>
            </div>
            <div class="metric-value">{escape(value)}</div>
            {hint_block}
        </div>
        """,
        unsafe_allow_html=True,
    )
