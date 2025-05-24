import streamlit as st
import pandas as pd

# Custom Styling
st.markdown("<h2 style='text-align: center; color: #4CAF50;'>User Information Form</h2>", unsafe_allow_html=True)

# Create a layout with columns
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name", placeholder="Enter your full name")
    age = st.number_input("Age", min_value=1, max_value=100)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    interests = st.multiselect("Interests", ["Cybersecurity", "Networking", "AI", "Cloud Computing", "Embedded Systems", "Robotics"])

# Checkbox (Full Width)
newsletter = st.checkbox("Subscribe to our newsletter?")

# Help Section using Expander
with st.expander("Need Help?"):
    st.write("Fill in your details and click submit to store your data.")
    st.write("Your information will be used for analytics or processing.")

# Submit Button (Centered)
col_btn = st.columns([1,2,1])
with col_btn[1]:
    submitted = st.button("Submit", help="Click to submit your details.")

# Validation & Data Storage
if submitted:
    if not name:
        st.error("⚠ Name is required!")
    else:
        user_data = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Interests": interests,
            "Subscribed": newsletter
        }
        
        # Save to CSV
        df = pd.DataFrame([user_data])
        df.to_csv("user_data.csv", mode='a', index=False, header=False)

        st.success("✅ Form submitted successfully!")
        st.write("📋 Here’s your data:")
        st.json(user_data)
