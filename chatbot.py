# Simple Rule-Based Chatbot

def chatbot():
    print("🤖: Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("🤖: Hello there! How can I help you?")
        elif user_input in ['how are you?', 'how are you', 'how are you doing?']:
            print("🤖: I'm just a bunch of code, but I'm doing great! 😊")
        elif "your name" in user_input:
            print("🤖: I’m ChatBot, your virtual assistant!")
        elif "weather" in user_input:
            print("🤖: Sorry, I can't provide real-time weather info yet.")
        elif user_input in ['bye', 'exit', 'quit']:
            print("🤖: Goodbye! Have a great day! 👋")
            break
        else:
            print("🤖: I'm not sure how to respond to that. Can you try something else?")

# Run the chatbot
chatbot()
