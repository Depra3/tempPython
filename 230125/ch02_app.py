# -*- coding: utf-8 -*-
# 라이브러리 불러오기
import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv('data/iris.csv')
    # print(data)
    st.title('데이터 확인')
    st.dataframe(data, 400, 500)

    # 색상 입히기
    st.title("Adding Color")
    st.dataframe(data.style.highlight_max(axis=0)) # 최댓값 
    # axis=1일 때 문자 숫자 비교가 되지 않아 에러 발생

    # table() 활용
    st.title('table() 활용')
    st.table(data.head())

    # 샘플 코드 보여주기
    mycode = """
    def hello():
        print("Hello World!!")
    end
    """
    # end 생략 가능

    st.code(mycode, language='python')

if __name__ == "__main__":
    main()