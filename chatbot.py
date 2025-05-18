def chatbot():
    print("🤖 Hello! I am AlphaBot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("AlphaBot: Hello! 😊")
        elif "how are you" in user_input:
            print("AlphaBot: I'm just a bot, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("AlphaBot: I'm AlphaBot, your friendly Python assistant!")
        elif "bye" in user_input:
            print("AlphaBot: Goodbye! Have a great day!")
            break
        else:
            print("AlphaBot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
