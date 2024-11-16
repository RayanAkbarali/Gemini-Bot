import os
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY=os.getenv("API_Key")
genai.configure(api_key=os.environ["API_Key"])
model=genai.GenerativeModel("gemini-1.5-pro")
st.title("Gemini API Bot")
user_input = st.text_input("Enter Your Query:")
if st.button("Submit"):
    st.write("You: "+user_input)
    response = model.generate_content(user_input)
    print(response)
    st.write("Gemini: "+response.text)
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="#" target="_blank"> Rayan </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
