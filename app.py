import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from pypdf import PdfReader

# 1. Page Configuration
st.set_page_config(page_title="AI Document Brain", layout="wide")
st.title("🧠 Enterprise AI Document Brain & PDF Chat Assistant")
st.write("Upload private PDFs or operational manuals to analyze and chat with your corporate data safely.")

# 2. Sidebar Setup for Authentication
st.sidebar.header("System Authentication")
api_key = st.sidebar.text_input("Enter Gemini API Key (Starts with AIzaSy):", type="password")

st.sidebar.markdown("""
### Secure RAG Operations:
1. **Document Ingestion:** The `pypdf` node extracts raw string data from your uploaded file.
2. **Contextual Injection:** Extracted text is fed into the Agent loop as an inline knowledge vector.
3. **Inference Guardrails:** The model is locked to answer questions *only* using facts from the uploaded document.
""")

st.write("---")

# 3. File Uploader Control Layout
uploaded_file = st.file_uploader("📥 Choose a PDF file to process:", type=["pdf"])

if uploaded_file:
    with st.spinner("Parsing document structure and extracting text nodes..."):
        try:
            # Read structural text pages using PyPDF
            pdf_reader = PdfReader(uploaded_file)
            raw_text = ""
            for page in pdf_reader.pages:
                text_content = page.extract_text()
                if text_content:
                    raw_text += text_content + "\n"
            
            if not raw_text.strip():
                st.error("Could not extract any readable text from this PDF. Please try a text-based document.")
            else:
                st.success(f"Successfully processed {len(pdf_reader.pages)} pages into localized context!")
                
                st.write("---")
                st.subheader("💬 Query the Document Matrix")
                user_query = st.text_input("Ask anything about the uploaded file:", placeholder="e.g., What are the key takeaways or specific metrics?")

                if st.button("Query Knowledge Base"):
                    if not api_key:
                        st.error("Please enter a valid Gemini API key in the left sidebar configuration box.")
                    elif not user_query.strip():
                        st.warning("Please type a valid question regarding the document content.")
                    else:
                        with st.spinner("Running contextual search over document index..."):
                            # 4. Initialize the Insulated RAG Agent
                            document_agent = Agent(
                                model=Gemini(id="gemini-2.5-flash", api_key=api_key),
                                description="You are an elite corporate intelligence analyst tasked with answering questions about custom business documents.",
                                instructions=[
                                    f"Here is the context of the document you must evaluate:\n\n{raw_text}",
                                    "Your answers must be completely factual based on the provided document context above.",
                                    "If the answer cannot be found in the provided document text, state explicitly that the information is missing from the document.",
                                    "Structure long answers with clean headers, bullet points, and markdown spacing.",
                                    "Do not make up facts or hallucinate any outside data."
                                ],
                                markdown=True
                            )
                            
                            # 5. Run Inference Execution
                            response = document_agent.run(user_query)
                            
                            st.write("### 🤖 Agent Response:")
                            st.markdown(response.content)
                            
        except Exception as e:
            st.error(f"System Parsing Error: {e}")
else:
    st.info("💡 Upload a company document above to populate the AI agent's secure reasoning matrix.")