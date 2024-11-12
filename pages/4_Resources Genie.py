import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Resources Page", layout="centered")

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

st.markdown("<h1 style='text-align: center;'> 🔗 Resource Genie</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'> One stop to find your Resource Links </h2>", unsafe_allow_html=True)

# Display banner image
banner_url = "https://images.pexels.com/photos/6340676/pexels-photo-6340676.jpeg"
st.image(banner_url, use_column_width=True)

# Explanation about the sidebar
st.write("""
On the left sidebar, you will find a combo box where you can choose different options. The available options are:
1. Business Plan Templates
2. Support Groups
3. Empower Women Videos
4. Organizations
Select an option to view the relevant resources links and information.
""")

# Add a sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write("Select a resource:")
resource_options = ["Business Plan Templates", "Support Groups", "Empower Women Videos", "Organizations"]
selected_resource = st.sidebar.selectbox("Choose a resource", resource_options)

# Display content based on the selected resource
if selected_resource == "Business Plan Templates":
    st.subheader("Business Plan Templates")
    st.write("Here are some business plan templates for women entrepreneurs:")
    st.markdown("[Ladies Who Launch - Business Plan Templates](https://www.ladieswholaunch.org/business-plan-templates)")
    st.markdown("[Canva - Business Plan Templates](https://www.canva.com/documents/templates/business-plan/)")
    st.markdown("[PandaDoc - Business Plan Templates](https://www.pandadoc.com/business-plan-templates/)")
    st.markdown("[Bplans - Business Plan Templates](https://www.bplans.com/downloads/business-plan-template/)")
    st.markdown("[Smartsheet - Business Plan Templates](https://www.smartsheet.com/content/simple-business-plan-templates)")
elif selected_resource == "Support Groups":
    st.subheader("Support Groups")
    st.write("Here are some support groups for women entrepreneurs:")
    st.markdown("[Federation of Indian Women Entrepreneurs (FIWE)](https://fiwe.org/)")
    st.markdown("[Women Entrepreneurs India](https://womenentrepreneursindia.com/)")
    st.markdown("[Ellevate Network](https://startupsavant.com/online-support-communities-for-female-entrepreneurs)")
    st.markdown("[Women Who Startup](https://startupsavant.com/online-support-communities-for-female-entrepreneurs)")
    st.markdown("[The Female Entrepreneur Association](https://startupsavant.com/online-support-communities-for-female-entrepreneurs)")
    st.markdown("[Woomentum](https://startupsavant.com/online-support-communities-for-female-entrepreneurs)")
elif selected_resource == "Empower Women Videos":
    st.subheader("Empower Women Videos")
    st.write("Here are some videos to empower women:")
    st.markdown("[Empowering Women Benefits Everyone | Jane Sojka | TEDxUCincinnati](https://www.youtube.com/watch?v=PC0Zx7VxxNg)")
    st.markdown("[Becoming an Empowered Woman | Paula Lacobara | TEDxCumbernauldWomen](https://www.youtube.com/watch?v=9ZQOUmQ562o)")
    st.markdown("[Empowering Women in the Public Sector | Dr. Shirin Sharmin Chaudhury | TEDxGulshan](https://www.youtube.com/watch?v=QPtdoCGDLDk)")
    st.markdown("[Empowering Women to Power the World | Anya Cherneff | TEDxZurich](https://www.youtube.com/watch?v=6lncdtX2ajI)")
    st.markdown("[Empowering Women in Developing Countries | Jennifer Lonergan | TEDxMontrealWomen](https://www.youtube.com/watch?v=DbtfYNKYing)")
elif selected_resource == "Organizations":
    st.subheader("Organizations")
    st.write("Here is a table of organizations that support women entrepreneurs:")

    st.table({
        "Organization": [
            "National Association for Women Business Owners (NAWBO)",
            "Women's Business Enterprise National Council (WBENC)",
            "Small Business Administration (SBA) Office of Women's Business Ownership",
            "Women Entrepreneurs (WE)",
            "Ellevate Network",
            "Women's Entrepreneurial Organization (WEO)",
            "Astia",
            "Springboard Enterprises",
            "Digital Undivided",
            "Girlboss",
            "Women's Business Centers (WBCs)",
            "SCORE",
            "Startup India",
            "WEConnect International",
            "Indian Women Network (IWN)"
        ],
        "Focus": [
            "Empowering women entrepreneurs",
            "Women-owned business certification",
            "Women's business development",
            "Community building",
            "Professional development",
            "Business growth",
            "Access to capital",
            "Women-led business growth",
            "Women of color in tech",
            "Community building",
            "Business development",
            "Business mentorship",
            "Startup ecosystem",
            "Women-owned business certification",
            "Women's empowerment"
        ],
        "Benefits": [
            "Networking, advocacy, education",
            "Access to corporate contracts, networking",
            "Training, counseling, access to credit",
            "Networking, mentorship, resources",
            "Networking, mentorship, training",
            "Networking, education, mentorship",
            "Funding, networking, mentorship",
            "Networking, funding, mentorship",
            "Funding, mentorship, resources",
            "Networking, resources, inspiration",
            "Training, counseling, access to credit",
            "Free mentorship, training",
            "Funding, mentorship, resources",
            "Access to corporate contracts",
            "Networking, training, mentorship"
        ],
        "Eligibility": [
            "Women business owners",
            "Women-owned businesses",
            "Women entrepreneurs",
            "Women entrepreneurs",
            "Women professionals and entrepreneurs",
            "Women entrepreneurs",
            "Women-led startups",
            "Women-led businesses",
            "Women of color in tech",
            "Women entrepreneurs and professionals",
            "Women entrepreneurs",
            "All entrepreneurs",
            "Indian startups",
            "Women-owned businesses globally",
            "Indian women professionals and entrepreneurs"
        ],
        "Website": [
            "https://www.nawbo.org/",
            "https://www.wbenc.org/",
            "https://www.sba.gov/offices/headquarters/wbo",
            "https://www.womenentrepreneurs.com/",
            "https://www.ellevatenetwork.com/",
            "https://www.weo.org/",
            "https://www.astia.org/",
            "https://sb.co/",
            "https://www.digitalundivided.com/",
            "https://www.girlboss.com/",
            "https://www.awbc.org/",
            "https://www.score.org/",
            "https://www.startupindia.gov.in/",
            "https://weconnectinternational.org/en/",
            "https://www.cii-iwn.in/"
        ]
    })

st.write("Is there anything else you'd like to explore?")
