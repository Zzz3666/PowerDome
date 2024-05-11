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
 - 更好展示电源设计细节和设计流程
 - 丰富的用户控制内容

#### 需求分析

##### 框架选择

Streamlit

##### 框架环境

Python

##### 环境依赖

Petalinux

##### Petalinux 平台

xczu3eg-sfvc784-1-e

"""
)
