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

PREBUILT_KNOWLEDGE = """
Sreenidhi Institute of Science and Technology (SNIST) is a prominent private engineering institution located in Hyderabad, Telangana, India. Established in 1997 under the aegis of the Sree Educational Group, the institute was founded by Dr. K.T. Mahhe, an educationist and entrepreneur with extensive experience in both academia and industry. SNIST is affiliated with Jawaharlal Nehru Technological University, Hyderabad (JNTUH), and offers a range of undergraduate and postgraduate programs in engineering, technology, and management disciplines.​
fp.sreenidhi.edu.in
+8
Wikipedia
+8
Top Colleges and Universities in India
+8
sreenidhi.edu.in
+1
Top Colleges and Universities in India
+1

Campus and Infrastructure

Situated in Yamnampet, Ghatkesar, Hyderabad, the SNIST campus spans 33 acres and provides a suburban setting conducive to academic pursuits. The institute boasts modern infrastructure, including well-equipped laboratories, spacious classrooms, a central library with a vast collection of resources, and advanced ICT e-learning facilities. Additional amenities include sports facilities, transportation services, hostels, and various campus facilities aimed at enhancing the student experience. ​
sreenidhi.edu.in
+1
sreenidhi.edu.in
+1
sreenidhi.edu.in
+1
sreenidhi.edu.in
+1

Academic Programs

SNIST offers a diverse array of programs across multiple disciplines:​
Gyaanarth
+10
Top Colleges and Universities in India
+10
Top Colleges and Universities in India
+10

Undergraduate Programs (B.Tech): The institute provides four-year Bachelor of Technology degrees in various specializations, including:​
sreenidhi.edu.in

Computer Science and Engineering​
Wikipedia
+9
CollegeDekho
+9
Top Colleges and Universities in India
+9

Computer Science and Engineering – Data Science​

Computer Science and Engineering – Artificial Intelligence and Machine Learning​
sreenidhi.edu.in

Computer Science and Engineering – Cyber Security​
sreenidhi.edu.in
+1
CollegeDekho
+1

Computer Science and Engineering – Internet of Things​
sreenidhi.edu.in
+7
CollegeDekho
+7
sreenidhi.edu.in
+7

Electronics and Communication Engineering​
Top Colleges and Universities in India
+1
sreenidhi.edu.in
+1

Electronics and Computer Engineering​
sreenidhi.edu.in
+2
sreenidhi.edu.in
+2
sreenidhi.edu.in
+2

Electrical and Electronics Engineering​
sreenidhi.edu.in
+1
Top Colleges and Universities in India
+1

Information Technology​
sreenidhi.edu.in
+12
sreenidhi.edu.in
+12
sreenidhi.edu.in
+12

Mechanical Engineering​
sreenidhi.edu.in

Civil Engineering​
sreenidhi.edu.in

Biotechnology​
CollegeDekho
+1
CollegeDekho
+1

Postgraduate Programs (M.Tech): SNIST offers Master of Technology degrees in specializations such as:​
CollegeDekho
+12
CollegeDekho
+12
sreenidhi.edu.in
+12

Software Engineering​

Biotechnology​
Gyaanarth
+7
sreenidhi.edu.in
+7
sreenidhi.edu.in
+7

Computer Science and Engineering​

Nano Technology​
CollegeDekho

Mechanical Engineering (CAD/CAM)​
CollegeDekho

Power Electronics​

VLSI System Design​

Embedded Systems​

Structural Engineering​

Master of Business Administration (MBA): The institute also offers a two-year MBA program focusing on various aspects of business management.​
Top Colleges and Universities in India
+3
sreenidhi.edu.in
+3
CollegeDekho
+3

Admissions

Admission to SNIST's B.Tech programs is primarily based on performance in the Telangana State Engineering, Agriculture, and Medical Common Entrance Test (TS EAMCET). For M.Tech programs, candidates are required to have a valid Graduate Aptitude Test in Engineering (GATE) score or qualify in the Telangana State Post Graduate Engineering Common Entrance Test (TS PGECET). MBA admissions are conducted through the Telangana State Integrated Common Entrance Test (TSICET). ​
sreenidhi.edu.in
+4
Top Colleges and Universities in India
+4
CollegeDekho
+4

Accreditations and Rankings

SNIST has received various accreditations and rankings that attest to its academic excellence:​
sreenidhi.edu.in

The institute is accredited by the National Board of Accreditation (NBA) and the National Assessment and Accreditation Council (NAAC).​

In The Week 2023 rankings, SNIST was placed 73rd out of 246 engineering colleges in India. ​
Top Colleges and Universities in India

Placements

SNIST has a dedicated placement cell that facilitates recruitment drives and career enhancement programs for students:​
Top Colleges and Universities in India

The average placement package is approximately ₹6.8 lakh per annum, with the highest package reaching up to ₹40 lakh per annum.​
CollegeDekho
+4
Top Colleges and Universities in India
+4
fp.sreenidhi.edu.in
+4

The institute collaborates with various industries to provide students with opportunities for internships and placements, aiming to bridge the gap between academic learning and industry requirements. ​

Research and Innovation

SNIST emphasizes research and innovation, encouraging faculty and students to engage in projects that contribute to technological advancements. The institute has initiated collaborations with industry partners and research organizations to design and develop innovative solutions. For instance, SNIST launched SREESAT-1 from the Tata Institute of Fundamental Research, Hyderabad, marking a significant step in enhancing its space technology capabilities. ​
sreenidhi.edu.in
+9
sreenidhi.edu.in
+9
sreenidhi.edu.in
+9
CollegeDekho

Student Life and Extracurricular Activities

Beyond academics, SNIST fosters a vibrant campus life with numerous extracurricular activities:​

SreeVision: An annual technical fest that provides a platform for students to showcase their technical skills and innovations.​

Traditional Day: An event celebrating cultural diversity, where students participate in various cultural programs and activities. ​

The institute also supports various clubs and organizations that cater to diverse interests, promoting holistic development among students.​

Conclusion

Sreenidhi Institute of Science and Technology stands as a notable institution in the field of engineering education in India. With its comprehensive academic programs, state-of-the-art infrastructure, emphasis on research and innovation, and a commitment to student development, SNIST continues to contribute significantly to the technological and managerial workforce of the country.
"""
# Initialize generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="A anything teacher who helps the student to understand a concept or give a tap on their shoulder and encourage them use socratic inqury when explaining or guiding",
)

def get_gemini_response(chat, question, retries=3, delay=5):
    full_query = PREBUILT_KNOWLEDGE + "\n\nUser Question: " + question  # Append knowledge
    for attempt in range(retries):
        try:
            response = chat.send_message(full_query, stream=True)
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
