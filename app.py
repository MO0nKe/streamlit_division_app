import streamlit as st

st.write("""
# Arithmetic Division Application
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    numerator = st.number_input("Numerator")
    denominator = st.number_input("Denominator", min_value=0.0000001)
    data = {"Numerator": numerator, "Denominator": denominator}
    return data
df = user_input_features()

# Displaying output

output = df["Numerator"]/df["Denominator"]

st.header("Output")
st.write(output)