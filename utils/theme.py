import streamlit as st


THEME_CSS = """
<style>
:root {
    --bg-main: #eef3f8;
    --bg-card: rgba(255, 255, 255, 0.94);
    --text-main: #163046;
    --text-sub: #5f7285;
    --line-soft: rgba(77, 106, 132, 0.16);
    --accent: #3d6f96;
    --accent-dark: #284a66;
    --accent-soft: rgba(61, 111, 150, 0.12);
    --shadow-soft: 0 10px 24px rgba(32, 56, 77, 0.08);
    --shadow-card: 0 12px 28px rgba(32, 56, 77, 0.08);
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(91, 129, 160, 0.16), transparent 28%),
        linear-gradient(180deg, #f4f8fc 0%, #eaf1f7 100%);
    color: var(--text-main);
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0);
}

[data-testid="stToolbar"] {
    right: 1rem;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 96%;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #dfe8f1 0%, #cfdbe8 100%);
    border-right: 1px solid rgba(59, 93, 120, 0.18);
}

[data-testid="stSidebarNav"] {
    padding-top: 0.45rem;
}

[data-testid="stSidebarNav"]::before {
    content: "系统导航";
    display: block;
    font-size: 1rem;
    font-weight: 700;
    color: #264662;
    margin: 0.25rem 0 0.85rem 0.2rem;
    letter-spacing: 0.02em;
}

.sidebar-brand-wrap {
    padding-bottom: 0.75rem;
    margin-bottom: 0.65rem;
    border-bottom: 1px solid rgba(59, 93, 120, 0.14);
}

.logo-shell {
    width: 92px;
    height: 92px;
    border-radius: 24px;
    background: linear-gradient(135deg, #2b4c68, #5f89ab);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 12px 24px rgba(36, 64, 87, 0.16);
    margin-bottom: 0.85rem;
}

.logo-fallback {
    color: #ffffff;
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: 0.04em;
}

.sidebar-profile-card {
    background: rgba(255, 255, 255, 0.58);
    border: 1px solid rgba(77, 106, 132, 0.12);
    border-radius: 18px;
    padding: 0.95rem 0.95rem 0.9rem 0.95rem;
    box-shadow: 0 8px 18px rgba(32, 56, 77, 0.06);
    backdrop-filter: blur(6px);
}

.sidebar-team-name {
    font-size: 0.98rem;
    font-weight: 800;
    color: #1f3f59;
    line-height: 1.45;
    margin-bottom: 0.45rem;
}

.sidebar-project-name {
    font-size: 0.9rem;
    font-weight: 700;
    color: #2a4c67;
    line-height: 1.65;
    margin-bottom: 0.55rem;
}

.sidebar-slogan {
    font-size: 0.84rem;
    color: #587083;
    line-height: 1.7;
    margin-bottom: 0.7rem;
}

.sidebar-divider {
    height: 1px;
    background: rgba(77, 106, 132, 0.14);
    margin: 0.65rem 0 0.75rem 0;
}

.sidebar-meta-item {
    margin-bottom: 0.58rem;
}

.sidebar-meta-item:last-child {
    margin-bottom: 0;
}

.sidebar-meta-label {
    display: block;
    font-size: 0.74rem;
    color: #6a7d8f;
    margin-bottom: 0.15rem;
}

.sidebar-meta-value {
    display: block;
    font-size: 0.84rem;
    color: #284a66;
    line-height: 1.6;
    font-weight: 600;
}

.hero {
    padding: 1.7rem 1.85rem;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(33, 62, 89, 0.97), rgba(71, 112, 145, 0.90));
    color: #f6fbff;
    box-shadow: 0 18px 42px rgba(36, 64, 87, 0.18);
    margin-bottom: 1.2rem;
}

.hero h1 {
    margin: 0 0 0.75rem 0;
    font-size: 2.15rem;
    line-height: 1.28;
    font-weight: 800;
}

.hero p {
    margin: 0;
    color: rgba(244, 248, 252, 0.88);
    line-height: 1.75;
    font-size: 1rem;
}

.hero-badges {
    margin-top: 1rem;
}

.hero-badge {
    display: inline-block;
    padding: 0.34rem 0.78rem;
    margin: 0 0.45rem 0.35rem 0;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.16);
    border: 1px solid rgba(255, 255, 255, 0.18);
    color: #f6fbff;
    font-size: 0.84rem;
    font-weight: 600;
}

.meta-box {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(239,245,249,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1rem 1.05rem;
    min-height: 136px;
    box-shadow: var(--shadow-soft);
}

.meta-label {
    font-size: 0.84rem;
    color: var(--text-sub);
    margin-bottom: 0.35rem;
}

.meta-value {
    font-size: 1.12rem;
    font-weight: 800;
    color: var(--accent-dark);
    line-height: 1.45;
    margin-bottom: 0.45rem;
}

.meta-desc {
    font-size: 0.88rem;
    color: var(--text-main);
    line-height: 1.62;
}

.card {
    background: var(--bg-card);
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1.1rem 1.2rem;
    box-shadow: var(--shadow-card);
    backdrop-filter: blur(8px);
}

.showcase-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(238,244,249,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 20px;
    padding: 1.15rem 1.2rem;
    min-height: 220px;
    box-shadow: var(--shadow-card);
}

.metric-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(236,242,247,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1rem 1.1rem;
    min-height: 110px;
    box-shadow: var(--shadow-soft);
}

.metric-label {
    font-size: 0.9rem;
    color: var(--text-sub);
    margin-bottom: 0.35rem;
}

.metric-value {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--accent-dark);
    word-break: break-word;
}

.section-kicker {
    display: inline-block;
    margin-bottom: 0.65rem;
    padding: 0.22rem 0.6rem;
    border-radius: 999px;
    background: var(--accent-soft);
    color: var(--accent-dark);
    font-size: 0.78rem;
    font-weight: 700;
}

.section-title {
    font-size: 1.04rem;
    font-weight: 800;
    color: var(--accent-dark);
    margin-bottom: 0.7rem;
}

.tag {
    display: inline-block;
    padding: 0.32rem 0.72rem;
    margin: 0 0.35rem 0.35rem 0;
    border-radius: 999px;
    background: var(--accent-soft);
    color: var(--accent-dark);
    font-size: 0.88rem;
    font-weight: 600;
}

.timeline-item {
    padding: 0.72rem 0;
    border-bottom: 1px dashed rgba(77, 106, 132, 0.2);
    color: var(--text-main);
    line-height: 1.7;
}

.timeline-item:last-child {
    border-bottom: none;
}

.flow-step {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(240,245,249,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1rem 0.95rem;
    min-height: 190px;
    box-shadow: var(--shadow-soft);
}

.flow-index {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(135deg, #3d6f96, #537c9d);
    color: white;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.85rem;
}

.flow-title {
    font-size: 1rem;
    font-weight: 800;
    color: var(--accent-dark);
    margin-bottom: 0.55rem;
}

.flow-desc {
    font-size: 0.9rem;
    line-height: 1.65;
    color: var(--text-main);
}

.two-col-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
    margin-top: 0.8rem;
}

.mini-stat {
    background: rgba(61, 111, 150, 0.06);
    border: 1px solid rgba(77, 106, 132, 0.14);
    border-radius: 14px;
    padding: 0.85rem 0.9rem;
}

.mini-stat span {
    display: block;
    font-size: 0.86rem;
    color: var(--text-sub);
    margin-bottom: 0.3rem;
}

.mini-stat strong {
    color: var(--accent-dark);
    font-size: 1rem;
    font-weight: 800;
}

.compact-list {
    margin: 0;
    padding-left: 1.2rem;
    line-height: 1.8;
}

.note-callout {
    margin-top: 1rem;
    padding: 1rem 1.1rem;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(61, 111, 150, 0.12), rgba(86, 124, 156, 0.08));
    border: 1px solid rgba(77, 106, 132, 0.16);
    color: var(--accent-dark);
    font-weight: 700;
    line-height: 1.75;
}

div[data-testid="stButton"] > button {
    border-radius: 12px;
    border: 1px solid rgba(45, 82, 111, 0.14);
    background: linear-gradient(135deg, #3d6f96, #557e9f);
    color: white;
    font-weight: 700;
}

div[data-testid="stButton"] > button:hover {
    border-color: rgba(45, 82, 111, 0.22);
    color: white;
}

div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

@media (max-width: 1100px) {
    .meta-box,
    .showcase-card,
    .flow-step {
        min-height: auto;
    }
}

@media (max-width: 900px) {
    .two-col-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 1.72rem;
    }

    .block-container {
        max-width: 100%;
    }
}
</style>
"""


def apply_theme() -> None:
    st.markdown(THEME_CSS, unsafe_allow_html=True)


def render_header(title: str, subtitle: str, badges=None) -> None:
    badges_html = ""
    if badges:
        badges_html = '<div class="hero-badges">' + "".join(
            [f'<span class="hero-badge">{badge}</span>' for badge in badges]
        ) + "</div>"

    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
            {badges_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    ) 
