import streamlit as st
st.set_page_config(layout="wide")   
text = st.text_input('Your link',max_chars = 50, help='To put a YouTube link the right way, start with https://www.youtube.com/watch?v=, then add a special mix of letters and numbers that\'s 11 long. For example, a link can look like this: https://www.youtube.com/watch?v=Yw6u6YkTgQ4.', placeholder='Please put your Youtube Link here')
st.button('Click here')
colpos, colneg = st.columns(2)
with colpos:
    st.header('Positive Comments')
    st.write('Hello world')
with colneg:
    st.header('Negative Comments')
    st.write('Hello bạn, mình là Vịt')