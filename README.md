# WikipediaBasedchatbot
Building a Simplistic Wikipedia Chatbot with Python
Description:

As we continue to explore the vast capabilities of artificial intelligence, the intersection between natural language processing (NLP) and accessible data from platforms like Wikipedia becomes particularly intriguing. For AI enthusiasts, building a chatbot that can source information from Wikipedia using the Python programming language is not only a fun project but also a great way to harness the power of models like T5 (Text-to-Text Transfer Transformer). In this article, we will walk through the steps of creating a lightweight chatbot that uses the Wikipedia package to fetch data and the Hugging Face Transformers library to process natural language.

## Setting Up Your Environment

Before we dive into the code, you will need to make sure that you have the necessary packages installed. The primary packages required are `wikipedia-api` for accessing Wikipedia content and `transformers` from Hugging Face for leveraging the T5 model. You can install these packages via pip:

```bash
pip install wikipedia transformers torch
```

Once the packages are installed, you can begin building your chatbot.

## Fetching Data from Wikipedia

To start, let’s create a function that retrieves articles from Wikipedia. The `wikipedia` is a powerful tool for extracting content efficiently. 
## Leveraging the T5 Model

Now that we can fetch data from Wikipedia, it’s time to utilize the T5 model to process this data into a conversational format. We will load the T5 model and tokenizer.

## Creating a simple chatbot
Now that we have the tokens ready we will write a simple function to ask a question and fetch the answer from wikipedia 

## TODO Next 
Build a simple webui for this using Gradio / Streamlit

