import streamlit as st 
st.title('THE MULTIVERSE OF CHATBOTS')
personality=st.sidebar.selectbox("Who do you want to talk to?",[
  "Hermione Granger","Sheldon Cooper","Mad Max","Voldemort","Doraemon"
])
intensity=st.sidebar.slider("INTENSITY",min_value=1,max_value=100)
from google import genai
import os 
from dotenv import load_dotenv 
load_dotenv()
client=genai.Client(api_key= os.getenv("GEMINI_API_KEY"))
user_message=st.text_input("Enter anything: ")
if st.button("SEND"):
  if user_message:
    ai_instructions=f"You are acting as {personality}.Respond to the message sent by the user,staying completely in character:{user_message}."
    with st.spinner("CONNECTING TO THE MULTIVERSE....."):
      response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=ai_instructions
        
      )
      st.success("Message received!")
      st.write(response.text)
  else:
    st.warning("Please type a message first")
      


