import streamlit as st
import random

st.title("🧠 Word Guessing Game 🧩")

words = ["apple", "banana", "orange", "grapes", "mango","jackfruit","pineapple","tomato","potato","onion","chilli","beans","soyabeans"]
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.shuffled = "".join(random.sample(st.session_state.word, len(st.session_state.word)))

st.write("Guess this word:", st.session_state.shuffled)

guess = st.text_input("Enter your guess:")

if st.button("Check"):
    if guess.lower() == st.session_state.word:
        st.success("🎉 Correct!")
    else:
        st.error(f"❌ Wrong! It was: {st.session_state.word}")

if st.button("Next Word"):
    st.session_state.word = random.choice(words)
    st.session_state.shuffled = "".join(random.sample(st.session_state.word, len(st.session_state.word)))
    st.experimental_rerun()
