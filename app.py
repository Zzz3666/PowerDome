""" app 入口"""
import streamlit as st
import graphviz as gz # type: ignore
from app.page_header import page_header

page_header(title="主页")

digital_power_supply_design_flow = gz.Digraph()
digital_power_supply_design_flow.edge("1", "2")
digital_power_supply_design_flow.edge("2", "3")
st.graphviz_chart(digital_power_supply_design_flow)
