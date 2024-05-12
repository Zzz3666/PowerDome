""" 软件开发页面 """

import streamlit as st
from app.page_header import page_header

page_header(title="软件开发")

st.header("开发环境")
st.divider()

st.header("虚拟机")
st.divider()
st.write("VMware Workstation 17.5.1")

st.header("宿主机")
st.divider()
st.write("Deepin 20.9")
st.write("Windows 11 Home 21H2")

st.header("Petalinux")
st.divider()
st.code(""" bash
sudo apt-get update
sudo apt-get install libncurses5-dev 
sudo apt-get install tftpd
sudo apt-get install xterm
sudo apt-get install autoconf
sudo apt-get install libtool
chmod 755 ./petalinux-v<petalinux-version>-final-installer.run
./petalinux-v<petalinux-version>-final-installer.run 
""")

st.header("Petalinux 配置")
st.divider()
