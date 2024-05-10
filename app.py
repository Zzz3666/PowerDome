""" app 入口"""

import streamlit as st
import graphviz as gz  # type: ignore
from app.page_header import page_header

page_header(title="主页")

digital_power_supply_design_flow_data = [
    "需求分析",
    "拓扑选择",
    "系统设计",
    "硬件设计",
    "软件开发",
    "仿真分析",
    "原型制作",
    "测试调试",
    "优化改进",
    "认证标准",
    "生产准备",
    "质量控制",
]

digital_power_supply_design_flow = gz.Digraph()
digital_power_supply_design_flow.attr("node", shape="box")
for index, digital_power_supply_design_flow_name in enumerate(
    digital_power_supply_design_flow_data
):
    digital_power_supply_design_flow.node(
        digital_power_supply_design_flow_name, width="2.0", height="0.5"
    )
for index in range(len(digital_power_supply_design_flow_data) - 1):
    digital_power_supply_design_flow.edge(
        digital_power_supply_design_flow_data[index],
        digital_power_supply_design_flow_data[index + 1],
    )
st.graphviz_chart(digital_power_supply_design_flow)
