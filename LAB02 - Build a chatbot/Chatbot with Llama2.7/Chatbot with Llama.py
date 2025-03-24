# Interactive chat using Llama 2
# This is a simple chatbot that responds to user input
# Check the README.md for the instalation details

import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# Load the model and tokenizer
tokenizer = LlamaTokenizer.from_pretrained(
    r"PATH TO YOUR LLAMA MODEL",
    local_files_only=True
)
model = LlamaForCausalLM.from_pretrained(
    r"PATH TO YOU LLAMA MODEL",
    local_files_only=True
)

# Configure the padding token if it is not defined
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Configure the device (GPU or CPU)
#device = "cuda" if torch.cuda.is_available() else "cpu"
device="cpu"
model = model.to(device)
model.eval()

# Conversation history
conversation_history = []

def chatbot_response(user_input):
    """
    Generates the chatbot's response based on the user's input.
    """
    global conversation_history

    # Add the user's input to the history
    conversation_history.append(f"User: {user_input}")

    # Build the conversation history
    formatted_history = "\n".join(conversation_history) + "\nAssistant:"

    # Tokenize the conversation history
    inputs = tokenizer(
        formatted_history,
        return_tensors="pt",
        truncation=True,
        max_length=1024  # Limit the history to avoid memory issues
    ).to(device)

    # Generate the model's response
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=150,  # Maximum length of the generated response
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id,  # Avoid padding warnings
            repetition_penalty=1.2  # Avoid unnecessary repetitions
        )

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the response after "Assistant:"
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()
    else:
        response = response.strip()

    # Validate the response: if empty, offer a generic message
    if not response:
        response = "Sorry, I don't have a clear answer for that right now. Can you try rephrasing your question?"

    # Add the response to the history
    conversation_history.append(f"Assistant: {response}")

    return response

def interactive_chat():
    """
    Interactive chat interface for the user.
    """
    print("Welcome to the chatbot! Type 'exit' to leave.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if not user_input:
            print("Chatbot: Please type something.")
            continue

        # Generate and display the chatbot's response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the interactive chat
interactive_chat()