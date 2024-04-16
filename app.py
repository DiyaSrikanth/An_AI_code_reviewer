from openai import OpenAI
import streamlit as st

f = open('.demo_key.txt')

open_ai_key = f.read()

client = OpenAI(api_key=open_ai_key)

st.title('🗨️ An AI Code Reviewer')
#st.subheader('Enter your code here....')

prompt = st.text_area('Enter your code here....')

if st.button('Generate')==True:
    response=client.chat.completions.create(
        model= 'gpt-3.5-turbo',
        messages=[
            {'role':'user', 'content':'Provide user-friendly,efficient, accurate bug reports and fixed code snippets.'},
            {'role':'user', 'content':prompt}
        ]
    )
    st.write(response.choices[0].message.content)
    