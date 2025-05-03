import streamlit as st
import requests

st.set_page_config(page_title="CV Parser", layout="centered")
st.title("📄 CV Parser Interface")

# Upload file
uploaded_file = st.file_uploader("Upload a CV (PDF, DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success(f"File uploaded: {uploaded_file.name}")
    
    # Send file to FastAPI backend
    if st.button("Parse CV"):
        with st.spinner("Parsing CV..."):
            response = requests.post(
                "http://127.0.0.1:8000/parse-cv",
                files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)},
            )
        
        if response.status_code == 200:
            result = response.json()
            st.subheader("✅ Parsed Result:")
            st.json(result)
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
