""" 页面标题显示及必备模块 """

import os
import streamlit as st
import pandas as pd


def page_header(title):
    """页面顶端显示"""
    st.title(title)
    st.divider()

    page_root_path = "pages/"

    if os.path.exists("data/page.csv"):
        page_data = pd.read_csv("data/page.csv")
        for i in range(len(page_data)):
            page_path = page_root_path + str(page_data.iloc[i, 0]) + ".py"
            st.sidebar.page_link(page_path, label=str(page_data.iloc[i, 1]))
