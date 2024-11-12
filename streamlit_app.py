import streamlit as st
from PIL import Image


# Custom CSS and HTML to style your app and place the logo at the top left corner
st.markdown(
 """
    <style>
    /* Main background and text colors */
    .stApp {
        background: linear-gradient(135deg, #81334C, #81334C);
        color: #ffffff;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* Paragraphs */
    p {
        font-size: 1.1em;
        line-height: 1.6;
    }

    /* Links */
    a {
        color: #FFB6C1 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }

    a:hover {
        color: #FFC0CB !important;
        text-decoration: underline;
    }

    /* Buttons */
    .stButton > button {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        font-size: 1em;
        padding: 10px 20px;
    }

    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Spacing */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Set page title
st.markdown("<h1 style='text-align: center; margin-bottom: 1rem;'>**Athena AI App**</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-bottom: 3rem;'>Women's AI Ally for Leadership Success</h3>", unsafe_allow_html=True)

# Display default banner image
default_image_url = "https://images.pexels.com/photos/6400345/pexels-photo-6400345.jpeg"
st.image(default_image_url, use_container_width=True)

# Explanation section
st.markdown("## About Athena AI App")
st.write("""
Empowered by the wisdom of Athena, Athena AI App is your go-to app for women entrepreneurs. With our innovative tools and supportive community, you can unlock your creativity, boost your business, and achieve your goals.
""")

# Features section
st.markdown("## Key Features")

# Chatbot powered by AI
st.markdown("### 1. Athena AI Genie")
st.write("""
Get instant answers and guidance on entrepreneurship and personal growth.
""")

# Business Genie
st.markdown("### 2. Business Genie")
st.write("""
Business Genie will track your progress in your business, do smart analysis, and suggest improvements.
""")

# Summarize Genie
st.markdown("### 3. Summarize Genie")
st.write("""
Paste or upload your text, get a summary, and listen to the summarized content.
""")

# InstaPost Genie
st.markdown("### 4. InstaPost Genie")
st.write("""
Let InstaPost Genie turn your photos into captivating Instagram posts. When you're at a loss for words upon seeing a picture, InstaPost Genie steps in to craft standout Instagram posts effortlessly.
""")

# Resources Section
st.markdown("### 5. Resource Genie")
st.write("""
Our app offers a variety of resources tailored for women entrepreneurs to help them succeed:
- **Business Plan Templates**: Access comprehensive business plan templates to help you start and grow your business.
- **Support Groups**: Join support groups to connect with fellow women entrepreneurs, share experiences, and gain valuable insights.
- **Organizations**: Discover organizations that support women entrepreneurs with funding, mentorship, and networking opportunities.
""")


if "todo_list" not in st.session_state:
    st.session_state["todo_list"] = []

def display_todo_list():
    for index, item in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{item['task']}")
        with col2:
            if st.button("Mark as Done", key=f"done_{index}"):
                item["done"] = True

display_todo_list()

# Partners Section
st.markdown("## Partners")
st.write("""
* [Google](https://www.google.com)
* [She Builds AI Hackathon](https://womentechmakers.devpost.com/)
* [Streamlit App](https://www.streamlit.io)
""")
