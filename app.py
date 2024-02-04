from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="Q&A with Images", page_icon=":gem:")
st.header("Q&A with Images")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True, width=300)


if 'history' not in st.session_state:
    st.session_state['history'] = {}

input_prompt = st.text_input("Input Prompt: ", key="input")


def save_history_to_file(filename, history):
    with open(filename, 'w') as file:
        for item in history:
            file.write(f"Question: {item['question']}\nAnswer: {item['answer']}\n\n")

def process_input():
    if uploaded_file is not None:
        image_filename = uploaded_file.name.split('.')[0]
        if image_filename not in st.session_state.history:
            st.session_state.history[image_filename] = []

        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(st.session_state.input, image_data, st.session_state.input)
        st.session_state.history[image_filename].append({"question": st.session_state.input, "answer": response})

        
        history_filename = f"{image_filename}.txt"
        save_history_to_file(history_filename, st.session_state.history[image_filename])

        return response, history_filename
    else:
        return "Please upload an image to start asking questions.", ""


if st.button("Ask"):
    response, history_filename = process_input()

    
    st.subheader("Answer: ")
    st.write(response)
    
    
    if uploaded_file:
        image_filename = uploaded_file.name.split('.')[0]
        st.subheader("History")
        if image_filename in st.session_state.history:
            for i, qa in enumerate(st.session_state.history[image_filename]):
                st.text(f"Q{i+1}: {qa['question']}")
                st.caption(f"A{i+1}: {qa['answer']}")

        if history_filename:
            st.info(f"History saved to {history_filename}")
