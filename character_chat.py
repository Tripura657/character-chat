import streamlit as st
import google.generativeai as genai

# -------- Configuration --------
st.set_page_config(page_title="Talk to Your Favorite Character", page_icon="🎭", layout="centered")
st.title("🎭 Talk with Your Favorite Character")

# -------- Set up Gemini API --------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"]) 
# -------- Load the model --------
model = genai.GenerativeModel("gemini-1.5-flash")
# -------- Character selection --------
character = st.selectbox("Choose a character:", ["Harry Potter", "Iron Man", "Doraemon", "Naruto", "Elsa"])
# -------- Chat input --------
character_prompt = st.chat_input(f"What do you want to tell {character}?")
# -------- Response generation --------
if character_prompt:
    with st.spinner("Summoning your character..."):
        try:
            char_response = model.generate_content(
                f"You are roleplaying as {character}. Reply in the tone and style of this character. The user says: '{character_prompt}'"
            )
            st.markdown(f"**{character}**: {char_response.text}")
        except Exception as e:
            st.error("Oops! The character is taking a break. Try again later.")
