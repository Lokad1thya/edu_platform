import streamlit as st
import os
import PyPDF2
import google.generativeai as genai
from google.api_core.exceptions import ServiceUnavailable
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="A anything teacher who helps the student to understand a concept or give a tap on their shoulder and encourage them use socratic inqury when explaining or guiding",
)

def get_gemini_response(chat, question, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = chat.send_message(question, stream=True)
            return response
        except ServiceUnavailable:
            st.warning(f"Service is overloaded. Retrying in {delay} seconds...")
            time.sleep(delay)
        except Exception as e:
            return [str(e)]
    return ["Service is currently unavailable. Please try again later."]

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def rigel_page():
    st.header("A Gemini application.")

    # Initialize session state variables
    if 'chat' not in st.session_state:
        st.session_state['chat'] = model.start_chat(history=[])
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'input_text' not in st.session_state:
        st.session_state['input_text'] = ""

    # Display chat history at the top
    st.subheader("Conversation History")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

    # Input and response section
    input_text = st.text_input("Input: ", key="input", value=st.session_state['input_text'])
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
    submit = st.button("Ask the question")

    # Handle user input and generate response
    if submit:
        if uploaded_file:
            input_text = extract_text_from_pdf(uploaded_file)
            st.write("Extracted text from PDF:")
            st.write(input_text)
        
        if input_text:
            response = get_gemini_response(st.session_state['chat'], input_text)
            st.session_state['chat_history'].append(("You", input_text))
            
            st.subheader("Response:")
            response_text = "".join([chunk.text for chunk in response])
            st.write(response_text)
            st.session_state['chat_history'].append(("Rigel", response_text))
            
    # Update the input field value
    st.session_state['input_text'] = input_text
