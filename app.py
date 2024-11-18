import streamlit as st
import google.generativeai as genai

# Configure your Google API key
genai.configure(api_key="AIzaSyCtEKTnKXJOnqvjyDs9TQjozhQ5CW9_aqU")  


# Advanced Sidebar (Bio Section)
with st.sidebar:
    # Display the image using the new parameter
    st.image("C:/Users/parmo/Downloads/r.png", use_container_width=True)
    st.title("About This Project")
    st.markdown("""
    ### Internship at: 
    **Innomatics Research Labs**  
    Supervised by **Kanav Bansal**  
    
    **Objective**:  
    This project leverages AI to enhance Python code quality by providing:  
    - Bug detection  
    - Improvement suggestions  
    - Fixed code snippets  
    
    **Features**:  
    - Real-time AI code review  
    - Clean and intuitive interface  
    - Session-based history tracking  
    
    ---
    ### Developer's Note:
    This tool was created as part of an internship to explore AI-assisted code review capabilities.
    """)

# Main Interface
st.title("GenAI App - AI Code Reviewer")
st.markdown("**Submit your Python code below to receive feedback.**")

llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

def update_chat(role, message):
    st.session_state["chat_history"].append({"role": role, "content": message})

input_code = st.text_area("Paste your Python code here:")

# Button for code review
if st.button("Review Code"):
    if input_code.strip():
        update_chat("human", input_code)
        review_prompt = f"Review the following Python code. Identify bugs, areas of improvement, and provide fixed code snippets:\n{input_code}"
        response = chatbot.send_message(review_prompt)
        
        # Add AI response to chat history and display
        update_chat("ai", response.text)
        st.success("Code reviewed successfully! See suggestions below.")
        st.subheader("AI Suggestions and Fixed Code:")
        st.write(response.text)
    else:
        st.warning("Please paste some Python code to review.")

# Button to view past history
if st.button("Show History"):
    if st.session_state["chat_history"]:
        st.subheader("Past Review History")
        for entry in st.session_state["chat_history"]:
            role = "User" if entry["role"] == "human" else "AI"
            st.markdown(f"**{role}:** {entry['content']}")
    else:
        st.info("No history available yet.")







