import streamlit as st

st.set_page_config(
    page_title="소상공인을 위한 AI",
    page_icon="🤗",
)

st.write("# 소상공인을 위한 AI 🤗")

st.sidebar.success("Select a menu above.")
st.sidebar.markdown(""" - [BIGHUG Website](https://karc.bighug.org/) """)
st.sidebar.markdown(""" - [BIGHUG Youtube Channel](https://www.youtube.com/@bighugorg) """)
st.sidebar.markdown(""" - [Catch Up AI Youtube Channel](https://www.youtube.com/@catchupai) """)

st.write("")
st.write("")

st.markdown(
    """
    이곳은 BIGHUG에서 진행한 워싱턴주의 한인 소상공인들을 위한 AI 강좌 내용을 정리해 놓았습니다.
    \n해당 강좌를 못 들으셨거나 다시 듣고 싶은 분들은 왼쪽 메뉴를 선택해서 보시면 도움이 되실 겁니다.
"""
)

st.write("왼쪽 메뉴에서 SB PPT 를 선택하시면 강좌에서 사용했던 프리젠테이션 파일을 보실 수 있습니다.")
st.write("그 외 Youtube로 시작하는 메뉴를 선택하시면 위 프리젠테이션 내용을 설명하는 유투브 강좌를 보실 수 있습니다.")
st.write("유투브 비디오는 계속 업로드 될 예정입니다. 채널을 Subscribe 하시면 업로드 될 때마다 보실 수 있습니다.")

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

