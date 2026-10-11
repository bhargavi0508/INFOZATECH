def chatbot():
    print("AI Chatbot: Hello! Welcome.")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "your name" in user_input:
            print("Bot: I am an AI chatbot.")

        elif "how are you" in user_input:
            print("Bot: I am doing well! Thank you.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I didn't understand that.")

chatbot()
