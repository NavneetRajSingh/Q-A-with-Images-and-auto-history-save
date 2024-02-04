# Q-A-with-Images

This Streamlit app allows users to upload images and ask questions about them. The app uses a generative AI model to generate responses to the questions. Each session's history of questions and answers is stored in a text file named after the uploaded image, allowing for easy review and record-keeping.

## Features

- **Image Upload**: Users can upload images in JPG or PNG format to ask questions about.
- **Q&A Interface**: After uploading an image, users can input questions, and the app provides AI-generated answers based on the image and question context.
- **History Tracking**: Each question and its corresponding answer are stored in a session-specific history, which is displayed below the input area.
- **Persistent Records**: The app saves a history of all questions and answers for each image in a text file named after the uploaded image, facilitating easy access to past interactions.

## Installation

To run this app locally, you will need Python and Streamlit installed, along with a few other dependencies.

1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Start the App**: Launch the app using the Streamlit command mentioned above.
2. **Upload an Image**: Use the "Choose an image..." button to upload a JPG or PNG image.
3. **Ask a Question**: Enter your question about the uploaded image in the "Input Prompt:" text input field.
4. **View the Answer**: Press the "Ask" button to receive an AI-generated answer to your question.
5. **Review History**: The "History" section below the "Ask" button displays all the questions asked and answers received for the current image.
6. **Access Saved Histories**: The app saves each session's Q&A history in a `.txt` file named after the uploaded image, which can be found in the app's running directory.

## Dependencies

- Streamlit
- Google Generative AI (or your choice of AI model API)
- Python-dotenv
- PIL (Python Imaging Library)

## Configuration

Before running the app, make sure to set up your environment variables:

1. Create a `.env` file in the root directory of your project.
2. Add your Google API Key (or relevant API Key for the AI model you are using) to the `.env` file:

    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

3. The app will read this key to authenticate requests to the AI service.

## Contributing

Contributions to improve the app are welcome. Please follow the standard fork-clone-branch-pull request workflow.

## Contact

gmail - rajnavnetsingh@gmail.com
linkedin - linkedin.com/in/navneetrajsingh
