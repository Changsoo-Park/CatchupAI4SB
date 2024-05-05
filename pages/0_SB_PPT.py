import streamlit as st
import streamlit.components.v1 as components

st.title('BIGHUG - 소상공인들을 위한 AI')
st.write('')
st.write('For bigger screen, click the link below.')
st.markdown(""" - [Google Slide Src](https://docs.google.com/presentation/d/1_7_ZBwNCADRoEvgfaemsTd7Pdt6dt3OEuJG4JUPnfsk/edit?usp=sharing) """)
st.write('')

# embed streamlit docs in a streamlit app
components.iframe("https://docs.google.com/presentation/d/1_7_ZBwNCADRoEvgfaemsTd7Pdt6dt3OEuJG4JUPnfsk/edit?usp=sharing", height =1000, width = 1500)

