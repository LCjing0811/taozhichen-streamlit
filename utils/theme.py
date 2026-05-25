# utils/theme.py
from html import escape

import streamlit as st


THEME_CSS = """
<style>
:root {
    --bg-deep-0: #030a18;
    --bg-deep-1: #091833;
    --bg-deep-2: #10284f;
    --text-main: #e7f1ff;
    --text-sub: #95abcf;
    --text-weak: #6f87ac;
    --accent-cyan: #3fd9ff;
    --accent-blue: #5f8dff;
    --accent-green: #4dd7a1;
    --accent-amber: #ffb767;
    --line-soft: rgba(142, 181, 255, 0.26);
    --glass-bg: rgba(11, 22, 44, 0.64);
    --glass-bg-strong: rgba(9, 17, 36, 0.78);
    --shadow-soft: 0 16px 38px rgba(4, 10, 24, 0.45);
}

.stApp {
    font-family: "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
    color: var(--text-main);
    background:
        radial-gradient(circle at 8% 10%, rgba(64, 122, 255, 0.25), transparent 32%),
        radial-gradient(circle at 88% 18%, rgba(67, 215, 255, 0.18), transparent 33%),
        radial-gradient(circle at 32% 82%, rgba(91, 92, 255, 0.15), transparent 35%),
        linear-gradient(165deg, var(--bg-deep-0) 0%, var(--bg-deep-1) 46%, var(--bg-deep-2) 100%);
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stAppViewContainer"] > .main {
    background: transparent;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 1.15rem;
    padding-bottom: 1.8rem;
}

h1,
h2,
h3,
h4 {
    color: var(--text-main);
    letter-spacing: 0.01em;
}

p,
li,
label {
    color: var(--text-sub);
}

[data-testid="stSidebar"] > div:first-child {
    background:
        radial-gradient(circle at top, rgba(78, 153, 255, 0.22), transparent 36%),
        linear-gradient(180deg, rgba(8, 19, 38, 0.96) 0%, rgba(6, 14, 29, 0.98) 100%);
    border-right: 1px solid rgba(111, 156, 240, 0.26);
}

.sidebar-system {
    margin: 0.25rem 0.45rem 0.95rem;
    border-radius: 14px;
    padding: 0.78rem 0.88rem;
    border: 1px solid rgba(133, 175, 255, 0.26);
    background: rgba(12, 28, 54, 0.56);
    box-shadow: inset 0 0 0 1px rgba(64, 204, 255, 0.08);
}

.sidebar-system .sys-title {
    font-size: 0.88rem;
    color: #d8e6ff;
    font-weight: 700;
    margin-bottom: 0.2rem;
}

.sidebar-system .sys-sub {
    font-size: 0.74rem;
    color: #7e97bd;
}

div[data-testid="stSidebarNav"] {
    margin-top: 0.2rem;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] {
    padding: 0 0.36rem 0.6rem;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li {
    list-style: none;
    margin: 0 0 0.26rem;
    position: relative;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(1)::before,
div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(2)::before,
div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(6)::before {
    display: block;
    padding: 0.44rem 0.3rem 0.3rem;
    font-size: 0.72rem;
    font-weight: 700;
    color: rgba(126, 151, 189, 0.92);
    letter-spacing: 0.06em;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(1)::before {
    content: "系统总览";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(2)::before {
    content: "工艺建模链路";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(6)::before {
    content: "决策输出";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li a[data-testid="stSidebarNavLink"] {
    min-height: 40px;
    border-radius: 12px;
    border: 1px solid transparent;
    padding: 0.46rem 0.62rem;
    color: rgba(216, 233, 255, 0.92);
    font-size: 0.9rem;
    background: rgba(17, 34, 63, 0.38);
    transition: all 0.18s ease;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li a[data-testid="stSidebarNavLink"] > div {
    gap: 0.55rem;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li a[data-testid="stSidebarNavLink"]::before {
    content: "◦";
    font-size: 0.96rem;
    color: #7db5ff;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(1) a[data-testid="stSidebarNavLink"]::before {
    content: "⌂";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(2) a[data-testid="stSidebarNavLink"]::before {
    content: "◧";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(3) a[data-testid="stSidebarNavLink"]::before {
    content: "◨";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(4) a[data-testid="stSidebarNavLink"]::before {
    content: "◩";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(5) a[data-testid="stSidebarNavLink"]::before {
    content: "◫";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li:nth-child(6) a[data-testid="stSidebarNavLink"]::before {
    content: "◎";
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li a[data-testid="stSidebarNavLink"]:hover {
    border: 1px solid rgba(111, 188, 255, 0.42);
    background: rgba(30, 59, 103, 0.68);
    box-shadow: 0 0 0 1px rgba(66, 212, 255, 0.2) inset;
}

div[data-testid="stSidebarNav"] ul[data-testid="stSidebarNavItems"] li a[data-testid="stSidebarNavLink"][aria-current="page"] {
    border: 1px solid rgba(98, 186, 255, 0.7);
    background: linear-gradient(135deg, rgba(27, 75, 142, 0.9), rgba(23, 56, 103, 0.95));
    box-shadow:
        0 0 0 1px rgba(90, 214, 255, 0.32) inset,
        0 10px 26px rgba(10, 23, 46, 0.5);
}

.hero {
    padding: 1.3rem 1.5rem;
    border-radius: 22px;
    border: 1px solid var(--line-soft);
    background:
        radial-gradient(circle at 12% 12%, rgba(75, 168, 255, 0.2), transparent 35%),
        linear-gradient(145deg, rgba(12, 27, 54, 0.82), rgba(11, 22, 45, 0.68));
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(6px);
    margin-bottom: 1.08rem;
}

.hero h1 {
    margin: 0 0 0.55rem;
    font-size: clamp(1.7rem, 2vw, 2.1rem);
    color: var(--text-main);
}

.hero p {
    margin: 0;
    color: var(--text-sub);
    line-height: 1.62;
}

.home-hero {
    padding: 1.7rem 1.75rem;
}

.hero-layout {
    display: grid;
    gap: 1rem;
    grid-template-columns: minmax(300px, 1.4fr) minmax(240px, 1fr);
}

.hero-title {
    margin: 0;
    font-size: clamp(2rem, 2.6vw, 2.7rem);
    line-height: 1.16;
    color: #f2f7ff;
}

.hero-subtitle {
    margin: 0.72rem 0 1.05rem;
    max-width: 48rem;
    color: #a9bfdf;
    font-size: 1rem;
    line-height: 1.72;
}

.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag {
    display: inline-flex;
    align-items: center;
    padding: 0.34rem 0.74rem;
    border-radius: 999px;
    border: 1px solid rgba(123, 174, 255, 0.3);
    background: rgba(21, 47, 84, 0.58);
    color: #d4e8ff;
    font-size: 0.78rem;
    letter-spacing: 0.03em;
}

.hero-state-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.55rem;
}

.hero-state-card {
    border-radius: 14px;
    border: 1px solid rgba(132, 179, 255, 0.26);
    padding: 0.7rem 0.72rem;
    background: rgba(14, 33, 63, 0.65);
    box-shadow: inset 0 0 0 1px rgba(70, 213, 255, 0.12);
}

.hero-state-title {
    margin: 0;
    color: #95acd1;
    font-size: 0.76rem;
}

.hero-state-value {
    margin: 0.34rem 0 0;
    color: #e8f4ff;
    font-size: 0.94rem;
    font-weight: 700;
}

.card {
    background: var(--glass-bg);
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1.02rem 1.1rem;
    box-shadow: var(--shadow-soft);
    backdrop-filter: blur(8px);
}

.section-title {
    margin: 0 0 0.76rem;
    font-size: 1.02rem;
    font-weight: 700;
    color: #e4eeff;
}

.section-subtitle {
    margin: 0 0 0.85rem;
    color: var(--text-sub);
    font-size: 0.84rem;
}

.metric-card {
    height: 100%;
    min-height: 132px;
    border-radius: 18px;
    border: 1px solid rgba(137, 177, 249, 0.32);
    padding: 0.92rem 1rem;
    background:
        radial-gradient(circle at top right, rgba(97, 202, 255, 0.16), transparent 45%),
        linear-gradient(160deg, rgba(13, 29, 56, 0.88), rgba(11, 23, 45, 0.76));
    box-shadow: var(--shadow-soft);
}

.metric-head {
    display: flex;
    align-items: center;
    gap: 0.42rem;
    margin-bottom: 0.5rem;
}

.metric-icon {
    width: 1.28rem;
    color: #6bc0ff;
    font-size: 0.95rem;
}

.metric-label {
    color: #9ab3d8;
    font-size: 0.82rem;
    letter-spacing: 0.03em;
}

.metric-value {
    font-size: clamp(1.34rem, 1.7vw, 1.95rem);
    font-weight: 800;
    line-height: 1.24;
    color: #f2f8ff;
}

.metric-hint {
    margin-top: 0.42rem;
    color: #85a2cb;
    font-size: 0.78rem;
}

.metric-card.tone-high .metric-value {
    color: #ff9f9f;
}

.metric-card.tone-medium .metric-value {
    color: #ffd38d;
}

.metric-card.tone-low .metric-value,
.metric-card.tone-positive .metric-value {
    color: #85f0ca;
}

.flow-track {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.56rem;
}

.flow-step {
    min-width: 128px;
    border-radius: 14px;
    border: 1px solid rgba(126, 169, 245, 0.3);
    background: rgba(16, 37, 69, 0.68);
    padding: 0.58rem 0.72rem;
}

.flow-index {
    display: block;
    font-size: 0.72rem;
    color: #7f9fd0;
    margin-bottom: 0.2rem;
}

.flow-title {
    display: block;
    font-size: 0.9rem;
    font-weight: 700;
    color: #e6f2ff;
}

.flow-arrow {
    color: #71c9ff;
    font-size: 1.15rem;
    font-weight: 700;
}

.timeline-item {
    padding: 0.64rem 0;
    border-bottom: 1px dashed rgba(110, 149, 211, 0.35);
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


def apply_theme() -> None:
    st.markdown(THEME_CSS, unsafe_allow_html=True)
    _render_sidebar_branding()


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
