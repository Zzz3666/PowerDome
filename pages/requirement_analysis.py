""" 需求分析页面 """

import streamlit as st
from app.page_header import page_header

page_header(title="需求分析")

st.header("用户交互需求")
st.divider()

st.subheader("WEB APP 交互需求")
st.divider()
st.write(
    """
 - 更好展示电压设计细节和设计流程
 - 丰富的控制内容
"""
)
