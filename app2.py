import streamlit as st 
personality=st.sidebar.selectbox("Who do you want to talk to?",[
  "Hermione Granger","Sheldon Cooper","Mad Max","Voldemort","Doraemon"
])
avatars = {
  "Hermione Granger": "📚",
  "Sheldon Cooper" : "🤓",
  "Mad Max" : "🚗",
  "Voldemort" : "🐍",
  "Doraemon": "🐱"
}
avatar = avatars[personality]

st.title(f"{avatar}THE MULTIVERSE OF CHATBOTS")


intensity=st.sidebar.slider("INTENSITY",min_value=1,max_value=100)
if intensity <=20:
  intensity_prompt="Be very subtle and occasionally show character"
elif intensity <=40:
  intensity_prompt="Stay mostly in character and quote a few lines"
elif intensity<=60:
  intensity_prompt="Clearly act like the character and make it realistic"
elif intensity<=80:
  intensity_prompt="Strongly act like the character and Use their catchphrases, mannerisms, and speaking style."
else:
  intensity_prompt="Fully become the character. Never break character. Use their emotions, vocabulary, humor, and personality to the maximum."
from google import genai
import os 
from dotenv import load_dotenv 
load_dotenv()
client=genai.Client(api_key= os.getenv("GEMINI_API_KEY"))
user_message=st.text_input("Enter anything: ")
if st.button("SEND"):
  if user_message:
    ai_instructions=f""" You are {personality}.
     Character Intensity = {intensity}/100
     Instructions:
{intensity_prompt}

Respond to the user's message while staying completely in character.

User: {user_message}
"""
    with st.spinner("CONNECTING TO THE MULTIVERSE....."):
      response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=ai_instructions
        
      )
      st.success("Message received!")
      st.write(response.text)
  else:
    st.warning("Please type a message first")
      
      


