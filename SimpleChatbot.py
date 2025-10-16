import wikipedia
import re
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Set the topic correctly
topic = "Machine learning"  # You can change this to any valid Wikipedia topic

# Fetch and clean content
wiki_content = wikipedia.page(topic, auto_suggest=False).content

# Clean text
def clean_text(text):
    text = re.sub(r'==.*?==+', '', text)  # remove headings
    text = re.sub(r'\n+', '\n', text)     # remove extra newlines
    text = re.sub(r'\[[^\]]*\]', '', text)  # remove referenaces
    return text.strip()

cleaned_text = clean_text(wiki_content)

# Show preview
print(cleaned_text[:1000])
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_answer(question, context, max_len=128):
    input_text = f"question: {question}  context: {context}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=max_len, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
context_chunk = cleaned_text[:10000]  # First part of text
question = "What is machine learning?"
answer = generate_answer(question, context_chunk)
print("❓ Question:", question)
print("✅ Answer:", answer)
