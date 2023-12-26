# !pip install langchain
# !pip install pathlib
# !pip install xmltodict
from langchain.retrievers import PubMedRetriever
from transformers import GPTJForCausalLM, GPT2Tokenizer
import torch

# Initialize the PubMed retriever
retriever = PubMedRetriever()

# Retrieve relevant documents about "brain fog"
# documents = retriever.get_relevant_documents("brain fog")

# device = "cuda"
# Initialize the GPT-J tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", low_cpu_mem_usage=True)
# model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True)

# Example question
question = "What is the remedy for brain fog?"

# print(documents)
# Combine the documents into a single context string
# context = " ".join([doc.page_content for doc in documents[:5]]) # Limiting to first 5 documents for brevity

# Prepare the prompt
p = ''
prompt = p + question

# Tokenize and generate the answer
inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
outputs = model.generate(max_length=50, num_return_sequences=1, **inputs)
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Question:", question)
print("Answer:", answer)

print("------")
print(outputs)