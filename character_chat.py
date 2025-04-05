import streamlit as st
import google.generativeai as genai

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Talk to Your Favorite Character", page_icon="🎭", layout="centered")
st.title("🎭 Talk with Your Favorite Character")
st.markdown("Choose a character and have a fun, emotional, or motivating conversation with them!")

# ------------------- Set up Gemini API -------------------
# Option 1: Use secrets (recommended on Streamlit Cloud)
# genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Option 2: Hardcode your key (only for local/testing)
genai.configure(api_key="AIzaSyCX5TKAFYkpT3JLnEa0_alXNjwYpe_-S2E")  # 👈 Replace this with your real key

# ------------------- Load the model -------------------
model = genai.GenerativeModel("gemini-1.5-flash")

# ------------------- Character Selection -------------------
character_gifs = {
    "Harry Potter": "https://media.giphy.com/media/13FrpeVH09Zrb2/giphy.gif",
    "Iron Man": "https://media.giphy.com/media/3o7TKy5xgXuQK0zrQY/giphy.gif",
    "Doraemon": "https://media.giphy.com/media/SqmkZ5Idn3Fi8/giphy.gif",
    "Naruto": "https://media.giphy.com/media/12kV5lgZVc6fGk/giphy.gif",
    "Elsa": "https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif"
}

character = st.selectbox("Choose a character:", list(character_gifs.keys()))

# ------------------- Chat Input -------------------
user_input = st.chat_input(f"What do you want to tell {character}?")

# ------------------- Character Response -------------------
if user_input:
    with st.spinner(f"{character} is thinking..."):
        try:
            # Generate roleplay response
            response = model.generate_content(
                f"You are roleplaying as {character}. Stay in character, use their tone and style. Respond to: '{user_input}'"
            )

            # Display character GIF and response
            st.image(character_gifs[character], use_container_width=True)
            st.markdown(f"**{character}**: {response.text}")

        except Exception as e:
            st.error("Oops! Something went wrong. Please try again later.")

# ------------------- Footer -------------------

