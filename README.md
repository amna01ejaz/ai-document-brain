# 🧠 Enterprise AI Document Brain & PDF Chat Assistant

A production-grade, self-contained **Retrieval-Augmented Generation (RAG)** application built using **Python**, **Agno Framework**, and **Streamlit UI**, utilizing **PyPDF** data stream extractions and **Google Gemini 2.5 Flash** models.

This application allows enterprise users to upload heavily unstructured localized text environments (like private PDF whitepapers or operational manifests) and dynamically converse with the document without uploading data to external vector storage providers.

## ✨ Architectural Core Features
* **Inline PDF Content Extraction:** Leverages `pypdf` page node mapping loops to distill binary document fragments into accessible runtime memory strings.
* **Insulated Context Rigging:** Dynamically maps parsed data strings straight into the structural instructions layer of the model, preventing external token contamination.
* **Deterministic Hallucination Guardrails:** Employs strict operational criteria instructing the agent to refuse external search queries if information does not exist inside the uploaded document.
* **Zero-Retention Client States:** Features client-side ephemeral upload buffers keeping document handling entirely isolated to the immediate runtime session.

## 🛠️ System Engineering Stack
* **Agent Orchestration Tier:** Agno Framework
* **Core Language Model:** Google Gemini 2.5 Flash API
* **Parsing Processing Layer:** PyPDF Engine
* **Application Layout Server:** Streamlit Interface Engine

## 💻 Local Quickstart Pipeline
1. Clone this project module:
   ```bash
   git clone [https://github.com/amna01ejaz/ai-document-brain.git](https://github.com/amna01ejaz/ai-document-brain.git)
   cd ai-document-brain