# -*- coding: utf-8 -*-
# 라이브러리 불러오기
import streamlit as st

def main():
    # text input
    fname = st.text_input('이름 입력')
    st.title(fname) # Enter

    # Text Area
    msg = st.text_area('입력', height=100)
    st.write(msg) # Ctrl + Enter

    # numbers
    number = st.number_input('숫자 입력')
    st.write(number)

    # Date Input
    myDate = st.date_input('날짜')
    st.write(myDate)

    # Time Input
    myTime = st.time_input('시간')
    st.write(myTime)

    # Color Picker
    color = st.color_picker('색상 선택')
    st.write(color)

if __name__ == "__main__":
    main()