import streamlit as st
import google.generativeai as genai

# Set up the page configuration
st.set_page_config(page_title="AI ChatBot", layout="centered")

# Custom CSS to change the background color
st.markdown("""
<style>
/* Custom styling for the page */
.stApp {
    background: linear-gradient(135deg, #81334C, #81334C);
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'> 🧚‍ Athena AI ChatBot </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'> Chat with Athena for any question! </h3>", unsafe_allow_html=True)

# Input API key
api_key_input = st.text_input("Enter your Gemini API Key", type="password")

# Check if API key is provided
if api_key_input:
    genai.configure(api_key=api_key_input)

    # Initialize the Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Initialize session state for chat history
    if "history" not in st.session_state:
        st.session_state["history"] = []

    # Function to get response from the model
    def get_chatbot_response(user_input):
        prompt = f"Athena Genie: {user_input}\nUser: {user_input}\nAthena Genie:"
        response = model.generate_content(prompt)
        return response.text

    # Display chat history
    st.markdown("---")
    for user_message, bot_message in st.session_state["history"]:
        st.markdown(f"""
        <div style="
            background-color: #4682b4;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 80%;
            text-align: left;
            display: inline-block;
        ">
            <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
            background-color: #00308f;
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px 0;
            max-width: 99%;
            text-align: left;
            display: inline-block;
        ">
            <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Athena Genie:</b> {bot_message} 🤖</p>
        </div>
        """, unsafe_allow_html=True)

    # Form for user input at the bottom
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area("Ask me anything...", max_chars=2000, height=100)
        submit_button = st.form_submit_button("Send")

        if submit_button:
            if user_input:
                # Get response from the model
                response = get_chatbot_response(user_input)
                st.session_state.history.append((user_input, response))

                # Re-run to update chat history
                st.rerun()
            else:
                st.warning("Please enter a message.")
else:
    st.warning("Please enter your Gemini API Key to proceed.")
