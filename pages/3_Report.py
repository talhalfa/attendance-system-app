import streamlit as st
from Home import face_rec
st.set_page_config(page_title='Reporting',layout='wide')
st.subheader('Reporting')


#Retrive logs data and show in Report.py
#extract data from redis list
name='attendance:logs'
def load_logs(name,end=-1):
    logs_list=face_rec.r.lrange(name,start=0,end=end)#extract all data from the redis database
    return logs_list

#tabs to show the info
tad1,tab2 = st.tabs(['Registered Data','Logs'])
with tad1:
    if st.button('Refresh Logs'):
        st.write(load_logs(name=name,end=-1))


with tab2:
    if st.button('Refresh Data'):
        #Retrieve the data from Redis Database
        with st.spinner('Retriving data from Redis db ...'):
            redis_face_db=face_rec.retrive_data('academy:register')
            st.dataframe(redis_face_db[['Name','Role']])