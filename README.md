PDF Chatbot using GPT-2 and Sentence Embeddings
This project demonstrates how to build a chatbot that can respond to questions based on the content of a provided PDF file. It uses Sentence-Transformers for better retrieval and GPT-2 for generating context-based responses.

Features
Extracts and processes text from a PDF file.
Uses Sentence-Transformers to create embeddings for efficient query-based document retrieval.
Leverages the GPT-2 model to generate answers based on the retrieved context.
Provides an interactive chatbot interface where users can ask questions about the PDF content.
Technologies Used
Python
Transformers (for GPT-2 text generation)
Sentence-Transformers (for sentence embeddings and retrieval)
PyPDF2 (for extracting text from PDFs)
Requirements
To run this project, make sure you have the following Python libraries installed:

transformers
sentence-transformers
PyPDF2
You can install these dependencies by running the following command:

pip install transformers sentence-transformers PyPDF2

How to Use
Clone the repository:

git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot

Place your PDF file:
Place your PDF file in the directory or specify the correct path to the file in the code.
Run the chatbot:
Execute the script to start the chatbot interface.

python chatbot.py

Ask questions:
Once the chatbot is running, it will prompt you to ask questions related to the PDF's content.
Type your query and the chatbot will generate a relevant response based on the content of the PDF.
To exit, type exit.
How it Works
Extract PDF Content: The extract_pdf_text() function reads and extracts text from the provided PDF file using PyPDF2.

Preprocess Text: The preprocess_chunks() function splits the extracted text into smaller chunks (based on word count) for better document retrieval.

Retrieve Relevant Content: The retrieve_relevant_chunk() function computes sentence embeddings for both the user's query and the document chunks. It uses cosine similarity to find the most relevant chunk based on the query.

Generate Responses: The generate_response() function uses the GPT-2 model to generate a response. The context is provided by the most relevant chunk retrieved from the document.

Interactive Chat: The chatbot runs in an interactive loop where users can ask questions and get responses based on the PDF content. Users can stop the interaction by typing exit.

Ask questions:
Once the chatbot is running, it will prompt you to ask questions related to the PDF's content.
Type your query and the chatbot will generate a relevant response based on the content of the PDF.
To exit, type exit.
How it Works
Extract PDF Content: The extract_pdf_text() function reads and extracts text from the provided PDF file using PyPDF2.

Preprocess Text: The preprocess_chunks() function splits the extracted text into smaller chunks (based on word count) for better document retrieval.

Retrieve Relevant Content: The retrieve_relevant_chunk() function computes sentence embeddings for both the user's query and the document chunks. It uses cosine similarity to find the most relevant chunk based on the query.

Generate Responses: The generate_response() function uses the GPT-2 model to generate a response. The context is provided by the most relevant chunk retrieved from the document.

Interactive Chat: The chatbot runs in an interactive loop where users can ask questions and get responses based on the PDF content. Users can stop the interaction by typing exit.
