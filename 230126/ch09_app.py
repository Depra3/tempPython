# -*- coding: utf-8 -*-
# BMI 계산기 간단하게 만들어보기

# 라이브러리 불러오기
import streamlit as st

def main():
    # 제목
    st.title('BMI 계산기')

    # 몸무게 저장 변수
    weight = st.number_input('몸무게를 입력해주세요. (KG)')

    # 단위 선택
    h_format = st.radio('키 입력 단위 설정', ('cm', 'm', 'feet'))

    # 단위별 BMI계산기 입력
    if h_format == 'cm':
        height = st.number_input('키를 입력해주세요 (cm)')
        try:
            h_cm = height/100
            bmi_result = weight/(h_cm*h_cm)
        except:
            st.text('')
    elif h_format == 'm':
        height = st.number_input('키를 입력해주세요 (m)')
        try:
            h_m = height
            bmi_result = weight/(h_m*h_m)
        except:
            st.text('')
    else:
        height = st.number_input('키를 입력해주세요 (feet)')
        try:
            h_feet = height*0.3048
            bmi_result = weight/(h_feet*h_feet)
        except:
            st.text('')

    if (st.button('BMI 계산기')):
        try:
            st.text(bmi_result)

            # 표준 등급
            if bmi_result <= 18.5:
                st.warning('저체중')
            elif bmi_result < 23:
                st.success('정상')
            elif bmi_result < 25:
                st.warning('과체중')
            else:
                st.error('비만')
        except:
            st.text('키 또는 몸무게를 제대로 입력하십시오.')

if __name__ == "__main__":
    main()