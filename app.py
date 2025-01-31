import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from clean_data import clean_text
from chains import Chain


def display_email(email_content):
    """Display the email in a professional format with a call-to-action"""
    
    parts = email_content.split("\n\n")
    subject = parts[0].replace("Subject:", "").strip()
    body = "\n\n".join(parts[1:])

    # Display Subject
    st.markdown(f"""
        <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem;
        border: 1px solid #e0e0e0; color: #0f1116; margin-bottom: 1rem;'>
            <strong>Subject:</strong> {subject}
        </div>
    """, unsafe_allow_html=True)

    # Display Email Body
    st.markdown(f"""
        <div style='background-color: #f0f2f6; padding: 2rem; border-radius: 0.5rem;
        border: 1px solid #e0e0e0; font-family: Arial, sans-serif;
        line-height: 1.6; white-space: pre-wrap; color: #0f1116;'>
            {body}
        </div>
    """, unsafe_allow_html=True)

    # Call-to-Action Highlight
    st.markdown("""
        <div style='background-color: #ffebcc; padding: 1rem; border-radius: 0.5rem;
        border: 2px solid #ff9900; text-align: center; font-weight: bold; font-size: 16px;
        color: #663300; margin-top: 1rem;'>
            ✨ Now personalize it and slide into HR's DMs! ✨
        </div>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, clean_text):
    st.title("📧 Cold Mail Generator")

    input_method = st.radio(
        "Choose how to input the job description:", 
        ("Copy-Paste", "Provide URL (Excluding LinkedIn)")
    )

    if input_method == "Copy-Paste":
        job_description = st.text_area(
            "Paste the job description here:", 
            height=300, 
            placeholder="Copy and paste the full job description here..."
        )
    else:
        url_input = st.text_input(
            "Enter the job description URL (excluding LinkedIn):", 
            placeholder="https://example.com/job-description"
        )

    submit_button = st.button("Generate Email")

    if submit_button:
        with st.spinner("Generating your email..."):
            if input_method == "Copy-Paste":
                if not job_description.strip():
                    st.error("Please enter a job description.")
                    return
                data = clean_text(job_description)
            else:
                if not url_input.strip():
                    st.error("Please enter a valid URL.")
                    return
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
            
            jobs = llm.extract_jobs(data)
            job = jobs[0]  

            email = llm.write_mail(
                job["role"], 
                job["experience"], 
                ", ".join(job["skills"]), 
                job["description"]
            )
            
            st.success("✨ Email generated successfully!")
            display_email(email)

if __name__ == "__main__":
    chain = Chain()
    create_streamlit_app(chain, clean_text)
