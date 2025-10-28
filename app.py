import random
import streamlit as st

st.title("🎯 Number Guessing Game by Om Gulsom Naimi")
st.write("Guess a number between 1 and 10")

# Generate a random number (store it using session state)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input("Your guess:", min_value=1, max_value=10, step=1)
if st.button("Check"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
        st.session_state.number = random.randint(1, 10)  # reset
    else:
        st.warning("❌ Wrong! Try again!")
