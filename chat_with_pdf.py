from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import PyPDF2

# Load the embeddings model for better retrieval
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
generator = pipeline('text-generation', model='gpt2')

# Extract text from PDF
def extract_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Preprocess text into chunks for retrieval
def preprocess_chunks(text, chunk_size=300):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

# Retrieve the most relevant chunk
def retrieve_relevant_chunk(query, chunks):
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    chunk_embeddings = embedding_model.encode(chunks, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, chunk_embeddings)
    best_chunk_index = scores.argmax().item()
    return chunks[best_chunk_index]

# Generate a response
def generate_response(query, context):
    input_text = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = generator(input_text, max_new_tokens=50, num_return_sequences=1)
    return response[0]['generated_text'].split('Answer:')[1].strip()

# Main chatbot function
def chat_with_pdf(pdf_path):
    pdf_text = extract_pdf_text(pdf_path)
    chunks = preprocess_chunks(pdf_text)

    print("Ask something about the PDF (type 'exit' to stop):")
    while True:
        query = input()
        if query.lower() == 'exit':
            break
        relevant_chunk = retrieve_relevant_chunk(query, chunks)
        response = generate_response(query, relevant_chunk)
        print(response)

# Run the chatbot with your PDF
if __name__ == "__main__":
    pdf_path = r"C:\Users\dell\OneDrive\Desktop\pdf-chatbot\my_document.pdf"  # Update with the correct PDF path
    chat_with_pdf(pdf_path)
