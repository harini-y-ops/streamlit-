import streamlit as st 
st.title("CodeX4000")
st.write("Please enter your name and details and enter SEND to send the message")
user_name=st.text_input("Please enter your name: ")
user_message=st.text_input("Please enter the message you want to send: ")
if st.button("SEND"):
  if user_name.strip()=="":
    st.error("Please provide a name")
  elif user_message.strip()=="":
    st.warning("Please enter a message to proceed")
  else:
    st.success(
      f"Transaction successful! {user_name}."
      f"we received your message - {user_message}"
    )
    total_characters=len(user_message)
    token_count=total_characters/4
    st.info(
    f" System Check: your message will consume {token_count:.2f} tokens."
    )

