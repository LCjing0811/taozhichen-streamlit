# 陶智沉——氧化铝陶瓷增材制造可解释智能工艺决策系统

这是一个基于 **Python + Streamlit** 构建的多页面交互原型系统，用于展示氧化铝陶瓷增材制造场景下的参数输入、热力预测、风险评估、方案对比和推荐决策流程。

当前版本使用**模拟数据与规则引擎**完成演示，不连接真实工业仿真软件，适合课程汇报、项目路演和比赛答辩场景。

## 项目结构

```text
taozhi_streamlit/
├─ app.py
├─ pages/
│  ├─ 1_parameter_input.py
│  ├─ 2_thermal_prediction.py
│  ├─ 3_risk_assessment.py
│  ├─ 4_scheme_comparison.py
│  └─ 5_recommendation.py
├─ utils/
│  ├─ __init__.py
│  ├─ mock_engine.py
│  └─ theme.py
├─ requirements.txt
└─ README.md
```

## 功能页面

- 参数输入页
- 热力预测结果页
- 风险评估页
- 方案对比页
- 推荐结果页

## 运行方式

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动项目

```bash
streamlit run app.py
```

### 3. 浏览器访问

启动后按终端提示打开本地地址，通常为：

```text
http://localhost:8501
```

## 页面说明

- `参数输入页`：设置层厚、打印速度、激光功率、烧结温度等核心参数。
- `热力预测结果页`：展示模拟温度场热图、温度历程曲线和热学指标。
- `风险评估页`：展示裂纹、孔隙、翘曲等风险画像与综合等级。
- `方案对比页`：对比保守方案、当前方案、激进方案的关键指标。
- `推荐结果页`：输出推荐工艺、评分和解释性建议。

## 技术说明

- 使用 `st.session_state` 在多页面之间传递参数与结果。
- 使用 `Plotly` 实现可交互图表展示。
- 使用统一 CSS 主题实现蓝灰色科技风界面。

## 适合展示的亮点

- 中文界面完整统一
- 多页面联动流程清晰
- 科技风视觉适合答辩展示
- 后续可平滑替换为真实仿真或机器学习模型
