# **Chatbot with LLaMA 2.7B-HF**

This project implements an interactive chatbot using the LLaMA 2.7B-HF model (Hugging Face). The chatbot is capable of maintaining coherent and contextual conversations thanks to the power of the LLaMA language model. Additionally, instructions are provided for downloading the model, and the possibility of using LLaMA 3 is mentioned, although the latter is heavier and requires greater computational capacity.

## **Project Description**

The chatbot is built using the LLaMA 2.7B-HF model, an open-source language model developed by Meta. This model is lightweight compared to larger versions like LLaMA 3, making it ideal for systems with limited resources. However, if your system has sufficient computational capacity (e.g., a powerful GPU), you can opt to use LLaMA 3, which offers superior performance but requires more memory and processing power.

The project includes:

- A Python script to interact with the model.

- Detailed instructions for downloading and setting up the model.

- An interactive chat interface to converse with the chatbot.

## **System Requirements**
Before getting started, ensure your system meets the following requirements:

### For LLaMA 2.7B-HF:
- RAM: Minimum 8 GB (16 GB or more recommended).

- GPU: Optional but recommended for better performance. A GPU with at least 8 GB of VRAM is sufficient.

- Storage: At least 10 GB of free space to download the model.

### For LLaMA 3:
- RAM: Minimum 16 GB (32 GB or more recommended).

- GPU: Highly recommended. A GPU with at least 16 GB of VRAM is ideal.

- Storage: At least 20 GB of free space.

## **Instructions for Downloading the Model**
- Access Hugging Face: Visit the model page on Hugging Face: LLaMA 2.7B-HF or LLaMA 3.

- Accept the Terms of Use: You must accept Meta's terms of use to download the model.

- Authenticate on Hugging Face: If you don’t have an account, create one and generate an access token from Hugging Face Tokens.

- Download the Model (Llama2 or Llama 3). If you want to test with Llama 3 ensure you have enough disk space, as LLaMA 3 is larger than LLaMA 2.

## **Environment Setup**
- Install Dependencies: Make sure you have the following Python libraries installed:
      pip install torch transformers
  
- Configure the Model: In the Python script, ensure the model path (local_files_only=True) points to the location where you downloaded the model.
- If you are using a GPU, change device="cpu" to device="cuda" in the script.

## **Run the Chatbot:**

Once configured, run the script to start the interactive chatbot:
```python
      python chatbot.py
```

Using the Chatbot
The chatbot is interactive and responds to your questions in real time. To exit the chat, simply type exit.

Example usage:
```text
Welcome to the chatbot! Type 'exit' to leave.
You: Hi, how are you?
Chatbot: Hello! I'm here to help. How can I assist you today?
You: What is artificial intelligence?
Chatbot: Artificial intelligence is...
```


## **Considerations for LLaMA 3**
If you decide to use LLaMA 3, keep in mind:

- It is a larger and more powerful model but requires significantly more computational resources.

- You will need a powerful GPU to run it efficiently.

- Inference time (response generation) will be slower compared to LLaMA 2.7B-HF.