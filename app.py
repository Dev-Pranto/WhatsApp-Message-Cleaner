# app.py
import streamlit as st
import re
from io import StringIO

st.set_page_config(
    page_title="WhatsApp Message Cleaner",
    page_icon="💬",
    layout="wide"
)

# Custom CSS for better mobile experience
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    textarea {
        font-size: 16px !important; /* Prevents zoom on iOS */
    }
    .stButton button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stDownloadButton button {
        width: 100%;
        background-color: #2196F3;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def clean_whatsapp_messages(input_text):
    # Pattern to match WhatsApp message headers
    pattern = r'\[\d{2}/\d{2}, \d{1,2}:\d{2}(?: [ap]m)?\] [^:]+: '
    
    # Split the text using the pattern
    parts = re.split(pattern, input_text)
    
    # Remove any empty parts and strip whitespace
    cleaned_parts = [part.strip() for part in parts if part.strip()]
    
    # Join the cleaned parts with two newlines
    return '\n\n'.join(cleaned_parts)

def main():
    st.title("💬 WhatsApp Message Cleaner")
    st.markdown("Paste your WhatsApp export below to remove timestamps and sender information")
    
    # Create a large text area for input
    input_text = st.text_area(
        "Paste your WhatsApp messages here:",
        height=300,
        placeholder="""[31/08, 10:24 pm] Rakibul Bhai: নাম : মাহিন
মোবাইল নাম্বার : 01790139904
জেলা : ঢাকা নারায়ণগঞ্জ  
থানা : সোনারগাঁও  
এলাকার নাম : পর্মেশ্বরদী  আমতলা

আপনার অর্ডার:
৩০ পিসের নিউট্রিশন মিল্ক -৭০০ টাকা S

[31/08, 10:30 pm] Rakibul Bhai: নাম: মুফতী তরিকুল ইসলাম হাসান 
০১৯১৬১৪৯৯৪০
নগর বাইতুল ইসলাম জামে মসজিদ কামরাংগীর চর ঢাকা

আপনার অর্ডার:
১ পিস হেলথ+১ টি মিনি দুধ -৫০০ টাকা S"""
    )
    
    # Process button
    if st.button("Clean Messages", type="primary"):
        if input_text.strip():
            with st.spinner("Cleaning messages..."):
                cleaned_text = clean_whatsapp_messages(input_text)
            
            st.success("Messages cleaned successfully!")
            
            # Display cleaned text
            st.subheader("Cleaned Messages")
            st.text_area("Cleaned output", cleaned_text, height=300)
            
            # Download button
            st.download_button(
                label="Download Cleaned Messages",
                data=cleaned_text,
                file_name="cleaned_whatsapp_messages.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please paste some WhatsApp messages first.")

    # Add instructions
    with st.expander("How to use this tool"):
        st.markdown("""
        1. Open WhatsApp and navigate to the chat you want to export
        2. Tap on the contact/group name at the top
        3. Scroll down and tap "Export chat"
        4. Choose "Without media" to get a text file
        5. Open the text file and copy all the content
        6. Paste the content in the text area above
        7. Click the "Clean Messages" button
        8. Download the cleaned messages using the download button
        """)

if __name__ == "__main__":
    main()
