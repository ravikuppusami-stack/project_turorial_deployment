import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Chatbot",    
        page_icon="🤖",           
        layout="centered"        
    )

    # Create the page header
    st.title("🤖 AI Chatbot")
    st.markdown("---")  

if __name__ == "__main__":
    main()