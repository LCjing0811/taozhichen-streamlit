import streamlit as st


THEME_CSS = """
<style>
:root {
    --bg-main: #eef3f8;
    --bg-card: rgba(255, 255, 255, 0.92);
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

.hero {
    padding: 1.4rem 1.6rem;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(33, 62, 89, 0.95), rgba(71, 112, 145, 0.88));
    color: #f6fbff;
    box-shadow: 0 16px 40px rgba(36, 64, 87, 0.18);
    margin-bottom: 1.2rem;
}

.hero h1 {
    margin: 0 0 0.6rem 0;
    font-size: 2rem;
}

.hero p {
    margin: 0;
    color: rgba(244, 248, 252, 0.86);
    line-height: 1.6;
}

.card {
    background: var(--bg-card);
    border: 1px solid var(--line-soft);
    border-radius: 18px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 10px 28px rgba(32, 56, 77, 0.08);
    backdrop-filter: blur(8px);
}

.metric-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(236,242,247,0.92));
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
}

.section-title {
    font-size: 1.02rem;
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
</style>
"""


def apply_theme() -> None:
    st.markdown(THEME_CSS, unsafe_allow_html=True)


def render_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
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
