# -*- coding: utf-8 -*-
# 라이브러리 불러오기
import streamlit as st

# 기타 사용자 정의 함수를 정의

# main()
def main():

    # title
    st.title('Hello World!')

    # header
    st.header('This is header')

    # subheader
    st.subheader('This is sub header')

    # MarkDown
    st.markdown('# This is Heading1')
    st.markdown('## This is Heading2')
    st.markdown('### This is Heading3')

    # Colored Text
    st.success('성공')
    st.warning("경고")
    st.info('정보')
    st.error("에러")
    st.exception('예외처리')

    # Superfunction
    st.write('텍스트')
    st.write(2)
    st.write(2 + 5)
    st.write(dir(str))
    


if __name__ == "__main__":
    main()