import streamlit as st
import google.generativeai as genai

# -------- Configuration --------
st.set_page_config(page_title="Talk to Your Favorite Character", page_icon="🎭", layout="centered")
st.title("🎭 Talk with Your Favorite Character")

# -------- Set up Gemini API --------
genai.configure(api_key="AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E")  # Replace with your Gemini API key

# -------- Load the model --------
model = genai.GenerativeModel("gemini-1.5-flash")

# -------- Character GIF Mapping --------
character_gifs = {
    "Harry Potter": "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
    "Iron Man": "https://media.giphy.com/media/11ZSwQNWba4YF2/giphy.gif",
    "Doraemon": "https://media.giphy.com/media/j0kQJxo5MzGYbo8PMZ/giphy.gif",
    "Naruto": "https://media.giphy.com/media/Nx0rz3jtxtEre/giphy.gif",
    "Elsa": "https://media.giphy.com/media/QZkpIdieotn3i/giphy.gif"
}

# -------- Character selection --------
character = st.selectbox("Choose a character:", list(character_gifs.keys()))

# -------- Chat input --------
character_prompt = st.chat_input(f"What do you want to tell {character}?")

# -------- Response generation --------
if character_prompt:
    with st.spinner("Summoning your character..."):
        try:
            char_response = model.generate_content(
                f"You are roleplaying as {character}. Reply in the tone and style of this character. The user says: '{character_prompt}'"
            )

            # 👇 Show matching character GIF
            st.image(character_gifs[character], use_column_width=True)

            st.markdown(f"**{character}**: {char_response.text}")
        except Exception as e:
            st.error("Oops! The character is taking a break. Try again later.")
