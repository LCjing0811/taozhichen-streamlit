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
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(91, 129, 160, 0.18), transparent 28%),
        linear-gradient(180deg, #f4f8fc 0%, #eaf1f7 100%);
    color: var(--text-main);
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #dfe8f1 0%, #cfdbe8 100%);
    border-right: 1px solid rgba(59, 93, 120, 0.18);
}

[data-testid="stSidebarNav"] {
    padding-top: 0.6rem;
}

[data-testid="stSidebarNav"]::before {
    content: "系统导航";
    display: block;
    font-size: 1rem;
    font-weight: 700;
    color: #264662;
    margin: 0.4rem 0 0.8rem 0.3rem;
    letter-spacing: 0.02em;
}

.hero {
    padding: 1.5rem 1.7rem;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(33, 62, 89, 0.96), rgba(71, 112, 145, 0.9));
    color: #f6fbff;
    box-shadow: 0 18px 42px rgba(36, 64, 87, 0.18);
    margin-bottom: 1.2rem;
}

.hero h1 {
    margin: 0 0 0.7rem 0;
    font-size: 2.15rem;
    line-height: 1.25;
}

.hero p {
    margin: 0;
    color: rgba(244, 248, 252, 0.88);
    line-height: 1.7;
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
}

.card {
    background: var(--bg-card);
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 10px 28px rgba(32, 56, 77, 0.08);
    backdrop-filter: blur(8px);
}

.showcase-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(238,244,249,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 20px;
    padding: 1.15rem 1.2rem;
    min-height: 220px;
    box-shadow: 0 12px 26px rgba(32, 56, 77, 0.08);
}

.metric-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(236,242,247,0.94));
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1rem 1.1rem;
    min-height: 110px;
    box-shadow: 0 10px 24px rgba(32, 56, 77, 0.08);
}

.metric-label {
    font-size: 0.9rem;
    color: var(--text-sub);
    margin-bottom: 0.35rem;
}

.metric-value {
    font-size: 1.6rem;
    font-weight: 700;
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
    font-weight: 600;
}

.section-title {
    font-size: 1.04rem;
    font-weight: 700;
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
}

.timeline-item {
    padding: 0.72rem 0;
    border-bottom: 1px dashed rgba(77, 106, 132, 0.2);
    color: var(--text-main);
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
    box-shadow: 0 10px 22px rgba(32, 56, 77, 0.07);
}

.flow-index {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: linear-gradient(135deg, #3d6f96, #537c9d);
    color: white;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0.85rem;
}

.flow-title {
    font-size: 1rem;
    font-weight: 700;
    color: var(--accent-dark);
    margin-bottom: 0.55rem;
}

.flow-desc {
    font-size: 0.9rem;
    line-height: 1.6;
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
    font-weight: 600;
}

div[data-testid="stButton"] > button {
    border-radius: 12px;
    border: 1px solid rgba(45, 82, 111, 0.14);
    background: linear-gradient(135deg, #3d6f96, #557e9f);
    color: white;
    font-weight: 600;
}

div[data-testid="stButton"] > button:hover {
    border-color: rgba(45, 82, 111, 0.22);
    color: white;
}

@media (max-width: 900px) {
    .two-col-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 1.7rem;
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
