import streamlit as st

from utils.mock_engine import ensure_session_state, update_inputs
from utils.theme import apply_theme, render_header, render_metric_card


st.set_page_config(page_title="参数输入", page_icon="🧪", layout="wide")
ensure_session_state()
apply_theme()

render_header(
    "参数输入",
    "录入氧化铝陶瓷增材制造关键工艺参数，系统将自动驱动后续热力预测、风险评估、方案对比与智能推荐页面联动更新。",
    badges=["参数驱动", "多页面联动", "答辩演示入口"],
)

params = st.session_state["input_params"].copy()

st.markdown("### 当前输入状态")
m1, m2, m3, m4 = st.columns(4)
with m1:
    render_metric_card("当前层厚", f'{params["layer_thickness"]:.0f} μm')
with m2:
    render_metric_card("当前激光功率", f'{params["laser_power"]:.0f} W')
with m3:
    render_metric_card("当前烧结温度", f'{params["sinter_temp"]:.0f} ℃')
with m4:
    render_metric_card("当前固含量", f'{params["solid_content"]:.0f}%')

st.markdown("### 参数配置面板")

with st.form("parameter_form", clear_on_submit=False):
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card" style="margin-bottom:0.8rem;">
                <div class="section-title">打印成形参数</div>
                <p style="margin:0;color:#5f7285;">主要影响局部热输入强度、成形效率与层间结合质量。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        layer_thickness = st.slider("铺层厚度 (μm)", 30, 90, int(params["layer_thickness"]), 1)
        print_speed = st.slider("打印速度 (mm/s)", 20, 70, int(params["print_speed"]), 1)
        laser_power = st.slider("激光功率 (W)", 120, 260, int(params["laser_power"]), 1)
        scan_spacing = st.slider("扫描间距 (mm)", 0.08, 0.20, float(params["scan_spacing"]), 0.01)

    with c2:
        st.markdown(
            """
            <div class="card" style="margin-bottom:0.8rem;">
                <div class="section-title">烧结制度参数</div>
                <p style="margin:0;color:#5f7285;">主要影响致密化程度、收缩行为与缺陷释放窗口。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        sinter_temp = st.slider("烧结温度 (℃)", 1500, 1650, int(params["sinter_temp"]), 5)
        holding_time = st.slider("保温时间 (h)", 1.0, 4.5, float(params["holding_time"]), 0.1)

        st.markdown(
            """
            <div class="card" style="margin-top:0.8rem;">
                <div class="section-title">展示提示</div>
                <p style="margin:0;">答辩时可优先调整激光功率、烧结温度与层厚，这三个变量最容易在后续页面中形成明显联动变化。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="card" style="margin-bottom:0.8rem;">
                <div class="section-title">浆料配方参数</div>
                <p style="margin:0;color:#5f7285;">主要影响孔隙残留概率、成形稳定性与后续烧结致密化表现。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        solid_content = st.slider("浆料固含量 (%)", 50, 68, int(params["solid_content"]), 1)
        binder_ratio = st.slider("粘结剂比例 (%)", 2.0, 6.5, float(params["binder_ratio"]), 0.1)

        st.markdown(
            """
            <div class="card" style="margin-top:0.8rem;">
                <div class="section-title">推荐策略</div>
                <p style="margin:0;">若想展示“参数变化 → 风险变化”效果，建议适度提高层厚或扫描间距；若想展示“优化后变稳”，可提高固含量并延长保温时间。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 参数修改后的预览摘要")
    p1, p2, p3, p4 = st.columns(4)
    with p1:
        render_metric_card("预览层厚", f"{layer_thickness} μm")
    with p2:
        render_metric_card("预览速度", f"{print_speed} mm/s")
    with p3:
        render_metric_card("预览温度", f"{sinter_temp} ℃")
    with p4:
        render_metric_card("预览固含量", f"{solid_content}%")

    submitted = st.form_submit_button("生成模拟结果并同步到后续页面", use_container_width=True)

if submitted:
    update_inputs(
        {
            "layer_thickness": float(layer_thickness),
            "print_speed": float(print_speed),
            "laser_power": float(laser_power),
            "scan_spacing": float(scan_spacing),
            "sinter_temp": float(sinter_temp),
            "holding_time": float(holding_time),
            "solid_content": float(solid_content),
            "binder_ratio": float(binder_ratio),
        }
    )
    st.success("参数已更新。请继续进入“热力预测”“风险评估”“方案对比”“智能推荐”页面查看联动结果。")

st.markdown("### 参数逻辑说明")
left, right = st.columns([1.15, 1])

with left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">输入变量分组</div>
            <span class="tag">打印段参数</span>
            <span class="tag">烧结段参数</span>
            <span class="tag">配方段参数</span>
            <p style="margin-top:0.8rem;">本原型通过规则模拟方式，将不同阶段参数映射到热输入、致密化、缺陷风险与推荐结论，用于展示系统级工艺决策逻辑。</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">适合答辩的操作顺序</div>
            <div class="timeline-item"><strong>步骤 1：</strong>先展示默认参数作为基准方案。</div>
            <div class="timeline-item"><strong>步骤 2：</strong>调整 1-2 个关键参数，如激光功率、烧结温度。</div>
            <div class="timeline-item"><strong>步骤 3：</strong>点击生成模拟结果，进入后续页面展示联动变化。</div>
            <div class="timeline-item"><strong>步骤 4：</strong>用推荐页做收束，强调系统的解释能力。</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="note-callout">
        本页是整个系统的输入起点。建议在答辩中把这里作为“交互触发器”，强调系统不是静态展示，而是可联动更新的工艺决策原型。
    </div>
    """,
    unsafe_allow_html=True,
)
