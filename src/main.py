import streamlit as st
from src.crew import kickoff

st.title('Social Media Manager')
st.write('Welcome to your social media management tool. Select your platform and enter a topic to create posts about.')

platform = st.selectbox('Choose your social media platform:', ['Instagram', 'Facebook'])
topic = st.text_input('Enter the topic:', '')

if st.button('Create Post'):
    if topic and platform:
        result = kickoff(topic, platform)
        st.success('Process started successfully!')
        st.write(result)
    else:
        st.error('Please enter a topic and choose a platform to proceed.')

st.write('Session and Authentication Details:')
st.write(kickoff(topic, platform) if topic and platform else "No session started.")
