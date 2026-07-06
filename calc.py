import streamlit as st
st.title("Simple calculator")
col1,col2 = st.columns(2)
with col1: 
  num1=st.number_input("Enter the first num: ")
with col2: 
  num2=st.number_input("Enter the second num: ")
  operation=st.radio(
    "Operation",
    ["+","-","*","/"],
    horizontal= True
  )
  if st.button("Calculate", use_container_width=True):
    if operation == '+':
      ans=num1+num2
    elif operation == '-':
      ans=num1-num2
    elif operation == '*':
      ans=num1*num2
    elif operation == '/':
      if num2 ==0:
        st.error("Cannot divide by zero error")
        st.stop()
      ans=num1/num2
    st.metric("Answer", ans)