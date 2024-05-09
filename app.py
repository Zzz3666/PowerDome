""" app 入口"""
import streamlit as st
import graphviz as gv
from app.page_header import page_header

page_header(title="主页")

digital_power_supply_design_flow = gv.Digraph()
st.graphviz_chart(digital_power_supply_design_flow)
