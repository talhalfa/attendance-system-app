import streamlit as st

st.set_page_config(page_title='Attendance System')

st.header('Attendance System using Face Recognition')
with st.spinner('Loading Model and connecting to Redis db ...'):
    import face_rec
st.success('Model Loaded successfully')
st.success('Redis db successfully connected')