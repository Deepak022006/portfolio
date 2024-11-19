import streamlit as st
st.title("Student Portfolio")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])
if page == "Home":
    st.header("Welcome to My Portfolio!")
    st.write("Hello! I'm a college student pursuing a degree in Engineering. "
             "This is my personal portfolio showcasing my skills, projects, and contact information.")
elif page == "About Me":
    st.header("About Me")
    st.write(''''Hello i am deepak iam currently pursuving my under graduation in BTECH AIDS
,my hobbies are watching movies and listening to music which help me to think in different way ''')
elif page == "Skills":
    st.header("Skills")
    st.write("Here are some of my skills:")
    st.write("- Programming Languages: Python")
    st.write("- Other: Problem-solving, Teamwork, Time management")
elif page == "Projects":
    st.header("Projects")
    st.write("Here are some of my recent projects:")
    st.write("1. Portfolio Website - A personal portfolio website created with Streamlit.")
    st.write("2. guessing game - in both user and program side .")
elif page == "Contact":
    st.header("Contact Me")
    st.write("moble no-9345528614")
    st.write("Email: deepakpri2006@gmail.com")import streamlit as st
import random
st.title("Number Guessing Game")
st.write("Guess a number between 1 and 10")
target_number = random.randint(1, 10)
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)
if 'target_number' not in st.session_state:
    st.session_state.target_number = target_number
if st.button("Submit Guess"):
    if guess == st.session_state.target_number:
        st.success(f"Congratulations! You guessed it right. The number was {st.session_state.target_number}.")
        st.session_state.target_number = random.randint(1, 10)
        st.write("New number generated. Try guessing again!")
    else:
        st.warning("Oops! Wrong guess. Try again.")