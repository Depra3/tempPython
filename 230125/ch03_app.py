# -*- coding: utf-8 -*-
# 라이브러리 불러오기
import streamlit as st

def main():
    
    name = 'evan'

    # 버튼
    if st.button('submit'):
        st.write(f'name : {name.upper()}')

    # Radio 버튼
    status = st.radio('Status', ('활성화', '비활성화'))

    if status == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # Check Box
    if st.checkbox('Show/Hide'):
        st.text('보여주세요!')

    # expander
    with st.expander('Python'):
        st.text('Hello Python')
        st.text('Hello Python!')
        st.text('Hello Python!!')

if __name__ == "__main__":
    main()