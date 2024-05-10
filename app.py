""" app 入口"""

import os
import streamlit as st
import graphviz as gz  # type: ignore
import pandas as pd
from app.page_header import page_header

page_header(title="主页")

st.header("目的")
st.divider()
st.write(
    """
 - 从零设计开关电源流程
 - 设计电源控制演示平台
 - 利用工具简化开发流程
 - 更好的提高个人技能水平
 - 增加公司的技术积累
"""
)


st.header("数字电源设计流程")
st.divider()
digital_power_supply_design_flow = gz.Digraph()
digital_power_supply_design_flow.attr("node", shape="box")
if os.path.exists("data/page.csv"):
    page_data = pd.read_csv("data/page.csv")
    for index, digital_power_supply_design_flow_name in enumerate(page_data.iloc[:, 1]):
        digital_power_supply_design_flow.node(
            digital_power_supply_design_flow_name, width="2.0", height="0.5"
        )
    for index in range(len(page_data) - 1):
        digital_power_supply_design_flow.edge(
            str(page_data.iloc[index, 1]),
            str(page_data.iloc[index + 1, 1]),
        )
    st.graphviz_chart(digital_power_supply_design_flow)

st.header("更多功能")
st.divider()
st.write("通过侧边栏选择更多功能")
