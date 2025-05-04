import streamlit as st

st.title("User Feedback Form")

# Form container
with st.form(key="feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    age = st.number_input("Your Age", min_value=0, max_value=120)
    rating = st.slider("How would you rate us?", 1, 10)
    feedback = st.text_area("Any comments?")
    
    # Submit button
    submit = st.form_submit_button("Submit")

if submit:
    st.success("Thank you for your feedback!")
    st.write("**Name:**", name)
    st.write("**Email:**", email)
    st.write("**Age:**", age)
    st.write("**Rating:**", rating)
    st.write("**Comments:**", feedback)


import pandas as pd
import os

data = {
    "name": name,
    "email": email,
    "age": age,
    "rating": rating,
    "feedback": feedback
}

df = pd.DataFrame([data])

if os.path.exists("responses.csv"):
    df.to_csv("responses.csv", mode="a", header=False, index=False)
else:
    df.to_csv("responses.csv", index=False)
