import streamlit as st
import random

# Initialize session state for the number and feedback
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.feedback = ""
    st.session_state.success = False

st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Input guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Guess button
if st.button("Guess"):
    if guess < st.session_state.number_to_guess:
        st.session_state.feedback = "📉 Too low!"
    elif guess > st.session_state.number_to_guess:
        st.session_state.feedback = "📈 Too high!"
    else:
        st.session_state.feedback = "🎉 Congratulations! You guessed the number."
        st.session_state.success = True

# Show feedback
if st.session_state.feedback:
    if st.session_state.success:
        st.success(st.session_state.feedback)
    else:
        st.info(st.session_state.feedback)

# Play again button
if st.button("🔄 Play Again"):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.feedback = ""
    st.session_state.success = False
    st.rerun()
