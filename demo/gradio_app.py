import gradio as gr
from typing import List

# Mock semantic search function
def search_profiles(query: str) -> List[str]:
    # Replace with FAISS logic later
    mock_results = {
        "ai": ["Mayra Harley - Enterprise Architect", "Jordan Lee - Data Scientist"],
        "cloud": ["Mayra Harley - Enterprise Architect"],
        "education": ["Ava Chen - Workforce Strategist"]
    }
    return mock_results.get(query.lower(), ["No matches found"])

# Gradio interface
demo = gr.Interface(
    fn=search_profiles,
    inputs=gr.Textbox(label="Enter search query"),
    outputs=gr.Label(label="Matching Profiles"),
    title="PMD Semantic Search",
    description="Search professional member profiles using semantic keywords."
)

if __name__ == "__main__":
    demo.launch()
