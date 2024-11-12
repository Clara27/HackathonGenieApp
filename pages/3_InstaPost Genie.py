import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Custom CSS to change the background color
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

# Streamlit App
st.markdown("<h1 style='text-align: center;'>🖼️ InstaPost Genie</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Upload your product image, InstaPost Genie will create Instagram content.</h2>", unsafe_allow_html=True)

# Input API key
api_key_input = st.text_input("Enter your Gemini API Key", type="password")

# Check if API key is provided
if api_key_input:
    genai.configure(api_key=api_key_input)
else:
    st.warning("Please enter your Gemini API Key to proceed.")

# Initialize Generative AI
def init_generative_ai(api_key):
    genai.configure(api_key=api_key)



# Upload image
uploaded_image = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

# Prompt for analysis
prompt = """This image contains a sketch of a potential product along with some notes.
Given the product sketch, describe the product as thoroughly as possible based on what you
see in the image, making sure to note all of the product features. Return output in json format:
{description: description, features: [feature1, feature2, feature3, etc]}"""

# Function to analyze image
def analyze_image(image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, image])
    return response.text

# Function to generate Instagram post
def generate_instagram_post(product_description, brand_tone, image_style):
    # Define prompt
    prompt = f"Create a captivating Instagram post based on the product description: {product_description}. Match the {brand_tone} tone and {image_style} image style."
    
    # Define guidelines
    guidelines = "1. Use a catchy headline (max 50 characters)\n2. Write a brief description (max 300 characters)\n3. Include a call-to-action (CTA)\n4. Add relevant hashtags (min 5)"
    
    # Generate post
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, guidelines])
    return response.text

# Main logic
if __name__ == "__main__":
   # Check if API key is provided
    if api_key_input:
        # Initialize Generative AI
        init_generative_ai(api_key_input)
        
        if uploaded_image:
            # Display uploaded image
            st.image(uploaded_image, caption='Uploaded Image')
            
            # Convert uploaded image to PIL format
            img = Image.open(uploaded_image)
            
            # Analyze image
            product_description = analyze_image(img)
            
            # Display product description
            st.write("Product Description:")
            st.write(product_description)
            
            # Get brand tone and image style
            brand_tone = st.selectbox("Select Brand Tone", ["Playful", "Professional", "Luxurious"])
            image_style = st.selectbox("Select Image Style", ["Lifestyle", "Product-only", "Minimalist"])
            
            # Generate Instagram post
            if st.button("Generate Instagram Post"):
                instagram_post = generate_instagram_post(product_description, brand_tone, image_style)
                st.write("Instagram Post:")
                st.write(instagram_post)
    else:
        st.warning("Please enter your Gemini API Key to proceed.")
