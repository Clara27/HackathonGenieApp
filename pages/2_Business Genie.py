import openai
import streamlit as st
import google.generativeai as genai
from datetime import datetime
import json

# Set page config first (before any other Streamlit commands)
st.set_page_config(page_title="Business Genie", layout="wide")

# Initialize session state for checklist data
def init_checklist_data():
    return {
        "legal": {
            "title": "Legal & Administrative Foundation",
            "items": [
                {"id": "l1", "text": "Business registration and licenses", "done": False, "priority": "high"},
                {"id": "l2", "text": "Tax ID and permits", "done": False, "priority": "high"},
                {"id": "l3", "text": "Business bank account", "done": False, "priority": "high"},
                {"id": "l4", "text": "Basic accounting system", "done": False, "priority": "medium"},
                {"id": "l5", "text": "Business insurance", "done": False, "priority": "high"},
                {"id": "l6", "text": "Trademark/IP protection", "done": False, "priority": "medium"},
                {"id": "l7", "text": "File business name with the state", "done": False, "priority": "low"},
            ]
        },
        "financial": {
            "title": "Financial Health Checklist",
            "items": [
                {"id": "f1", "text": "Weekly cash flow review", "done": False, "priority": "high"},
                {"id": "f2", "text": "Monthly profit/loss review", "done": False, "priority": "high"},
                {"id": "f3", "text": "Emergency fund setup", "done": False, "priority": "high"},
                {"id": "f4", "text": "Credit score monitoring", "done": False, "priority": "medium"},
                {"id": "f5", "text": "Payment collection system", "done": False, "priority": "high"},
                {"id": "f6", "text": "Pricing strategy documentation", "done": False, "priority": "medium"},
                {"id": "f7", "text": "Review old expense reports", "done": False, "priority": "low"},
            ]
        },
        "operations": {
            "title": "Business Operations",
            "items": [
                {"id": "o1", "text": "Standard operating procedures", "done": False, "priority": "medium"},
                {"id": "o2", "text": "Quality control measures", "done": False, "priority": "high"},
                {"id": "o3", "text": "Vendor/supplier agreements", "done": False, "priority": "medium"},
                {"id": "o4", "text": "Customer service protocol", "done": False, "priority": "high"},
                {"id": "o5", "text": "Data backup system", "done": False, "priority": "high"},
                {"id": "o6", "text": "Cybersecurity measures", "done": False, "priority": "high"},
                {"id": "o7", "text": "Update office supplies inventory", "done": False, "priority": "low"},
            ]
        },
        "growth": {
            "title": "Growth & Development",
            "items": [
                {"id": "g1", "text": "Business plan documentation", "done": False, "priority": "high"},
                {"id": "g2", "text": "Networking goals", "done": False, "priority": "medium"},
                {"id": "g3", "text": "Professional development plan", "done": False, "priority": "medium"},
                {"id": "g4", "text": "Mentorship connections", "done": False, "priority": "medium"},
                {"id": "g5", "text": "Grant opportunities research", "done": False, "priority": "medium"},
                {"id": "g6", "text": "Market research schedule", "done": False, "priority": "medium"},
                {"id": "g7", "text": "Read business-related articles", "done": False, "priority": "low"},
            ]
        },
        "balance": {
            "title": "Personal & Professional Balance",
            "items": [
                {"id": "b1", "text": "Self-care routine", "done": False, "priority": "high"},
                {"id": "b2", "text": "Work hours boundaries", "done": False, "priority": "high"},
                {"id": "b3", "text": "Delegation plan", "done": False, "priority": "medium"},
                {"id": "b4", "text": "Support system list", "done": False, "priority": "medium"},
                {"id": "b5", "text": "Time management system", "done": False, "priority": "high"},
                {"id": "b6", "text": "Stress management strategies", "done": False, "priority": "high"},
                {"id": "b7", "text": "Journal personal reflections", "done": False, "priority": "low"},
            ]
        }
    }

# Initialize all session state variables at the start
if 'initialized' not in st.session_state:
    st.session_state.checklist_data = init_checklist_data()
    st.session_state.progress_tracking = {
        section_id: 0 for section_id in st.session_state.checklist_data.keys()
    }
    st.session_state.initialized = True

# Custom CSS styles
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #81334C, #81334C);
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    p {
        font-size: 1.1em;
        line-height: 1.6;
    }
    a {
        color: #FFB6C1 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    a:hover {
        color: #FFC0CB !important;
        text-decoration: underline;
    }
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
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>💼 Business Genie</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Business Genie: Your Business Success Partner.</h2>", unsafe_allow_html=True)

# Input API key for Gemini
api_key_input = st.text_input("Enter your Gemini API Key", type="password")
if api_key_input:
    genai.configure(api_key=api_key_input)
else:
    st.warning("Please enter your Gemini API Key to proceed.")

# Initialize the Generative AI model
model = genai.GenerativeModel('gemini-1.5-flash')

def update_progress(section_id):
    """Update progress for a specific section"""
    section_items = st.session_state.checklist_data[section_id]["items"]
    if not section_items:
        st.session_state.progress_tracking[section_id] = 0
    else:
        completed = sum(1 for item in section_items if item["done"])
        st.session_state.progress_tracking[section_id] = int((completed / len(section_items)) * 100)

def on_checkbox_change(section_id, item_id):
    """Callback function for checkbox changes"""
    # Update the item's done status
    for item in st.session_state.checklist_data[section_id]["items"]:
        if item["id"] == item_id:
            item["done"] = st.session_state[f"checkbox_{item_id}"]
            break
    
    # Update progress immediately
    update_progress(section_id)

def generate_suggestions(section_id):
    """Generate suggestions based on completed tasks"""
    section_data = st.session_state.checklist_data.get(section_id)
    if section_data:
        completed_tasks = [
            item['text'] for item in section_data['items'] if item['done']
        ]
        if completed_tasks:
            prompt = f"Based on the completed tasks in the {section_data['title']} section: {', '.join(completed_tasks)}, provide detailed next steps and motivational advice to further enhance the progress in this specific area."
            response = model.generate_content(prompt)
            return response.text
    return "Keep up the good work! You're on track to success!"

def add_new_section(section_name):
    """Add a new section to the checklist"""
    new_section = {
        "title": section_name,
        "items": []
    }
    st.session_state.checklist_data[section_name] = new_section
    st.session_state.progress_tracking[section_name] = 0
    st.success(f"New section '{section_name}' added successfully!")

def add_task_to_section(section_id, task_text, task_priority):
    """Add a custom task to a specific section"""
    task_id = f"{section_id}_{len(st.session_state.checklist_data[section_id]['items']) + 1}"
    new_task = {
        "id": task_id,
        "text": task_text,
        "done": False,
        "priority": task_priority
    }
    st.session_state.checklist_data[section_id]["items"].append(new_task)
    update_progress(section_id)

def main():
    # Create tabs for each section
    section_titles = [section["title"] for section in st.session_state.checklist_data.values()]
    tabs = st.tabs(section_titles)

    # Display checklist items for each section
    for tab, (section_id, section_data) in zip(tabs, st.session_state.checklist_data.items()):
        with tab:
            # Show progress bar using session state tracking
            st.progress(st.session_state.progress_tracking[section_id] / 100)
            st.markdown(f"**Progress: {st.session_state.progress_tracking[section_id]}%**")

            # Display tasks sorted by priority
            for priority in ['high', 'medium', 'low']:
                st.markdown(f"### {priority.capitalize()} Priority Tasks")
                filtered_items = [item for item in section_data["items"] if item["priority"] == priority]
                
                for item in filtered_items:
                    # Create a unique key for the checkbox
                    checkbox_key = f"checkbox_{item['id']}"
                    
                    # Initialize the checkbox state in session state if not exists
                    if checkbox_key not in st.session_state:
                        st.session_state[checkbox_key] = item["done"]
                    
                    # Create checkbox with callback
                    checked = st.checkbox(
                        item["text"],
                        value=st.session_state[checkbox_key],
                        key=checkbox_key,
                        on_change=on_checkbox_change,
                        args=(section_id, item["id"])
                    )
                    
                    # Update the item's done status
                    item["done"] = checked

            # # Generate suggestions if all tasks are complete
            # if all(item['done'] for item in section_data['items']):
                # st.markdown("### Business Genie Suggestion")
                # suggestions = generate_suggestions(section_id)
                # st.write(suggestions)
                
            # Generate suggestions if all tasks are complete
            if all(item['done'] for item in section_data['items']):
                st.markdown("### Business Genie Suggestion")
                with st.spinner('Generating AI suggestions...'):
                    suggestions = generate_suggestions(section_id)
                    st.write(suggestions)

    # Customize Your Checklist section
    with st.expander("Customize Your Checklist"):
        st.header("Add New Section")
        new_section_name = st.text_input("New Section Name:")
        if st.button("Add Section"):
            if new_section_name:
                add_new_section(new_section_name)
            else:
                st.error("Please provide a section name.")

        st.header("Add Task to an Existing Section")
        section_options = list(st.session_state.checklist_data.keys())
        section_to_add_task = st.selectbox("Select Section", section_options)
        new_task_text = st.text_input("Task Text")
        task_priority = st.selectbox("Priority", ["high", "medium", "low"])
        
        if st.button("Add Task"):
            if new_task_text:
                add_task_to_section(section_to_add_task, new_task_text, task_priority)
                st.success(f"Task added to the {section_to_add_task.capitalize()} section.")
            else:
                st.error("Please provide a task description.")

if __name__ == "__main__":
    main()