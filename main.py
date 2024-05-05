import streamlit as st

st.set_page_config(
    page_title="소상공인을 위한 AI",
    page_icon="🤗",
)

st.write("# 소상공인을 위한 AI 🤗")

st.sidebar.success("Select a menu above.")
st.sidebar.markdown(""" - [BIGHUG Website](https://karc.bighug.org/) """)
st.sidebar.markdown(""" - [BIGHUG Youtube Channel](https://www.youtube.com/@bighugorg) """)

st.write("")
st.write("")

st.markdown(
    """
    이곳은 BIGHUG에서 진행한 워싱턴주의 한인 소상공인들을 위한 AI 강좌 내용을 정리해 놓았습니다.
    \n해당 강좌를 못 들으셨거나 다시 듣고 싶은 분들은 왼쪽 메뉴를 선택해서 보시면 도움이 되실 겁니다.
"""
)
st.write("")
st.image('./images/bighug.png', caption='BIGHUG')
st.write("")
st.write("")


st.markdown(
    """
    아래 링크들은 제가 AI 관련해서 작업하고 있는 내용들입니다.
    - [Catchup AI Youtube Channel](https://www.youtube.com/@catchupai)
    - [Catchup LangChain Streamlit Web App](https://catchuplangchain.streamlit.app/)
    - [Catchup AI Streamlit Web App](https://catchupai.streamlit.app/)
    - [Catchup AI Tistory Blog](https://coronasdk.tistory.com/)
    - [Deep Learning Fundamental PPT (Eng. Ver.)](https://docs.google.com/presentation/d/1F4qxSAv9g13de99rS8fcp4e1LCfrILq8QaahXCPx1Pw/edit?usp=sharing)
    - [Deep Learning Fundamental PPT (Kor. Ver.)](https://docs.google.com/presentation/d/15KNzGnSnJx_4ToSBM2MrHiC2q5MiVe0plOs7f3NJuWM/edit?usp=sharing)
    - [AI Web App Development 101 PPT](https://docs.google.com/presentation/d/18_6z05tmR_loTPWFHj8PCY3-uCNKuoy-IvE0g5ms8YM/edit?usp=sharing)
"""
)

