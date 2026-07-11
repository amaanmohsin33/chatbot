"""
Simple Rule-Based Chatbot
Goal: Respond to predefined user inputs using if-else logic in a loop.
"""

def get_response(user_input):
    text = user_input.lower().strip()

    # Greetings
    if text in ["hi", "hello", "hey", "salam", "assalam o alaikum"]:
        return "Hello! How can I help you today?"

    elif text in ["how are you", "how are you?"]:
        return "I'm just a bot, but I'm doing great! How about you?"

    elif text in ["what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot built in Python."

    elif "help" in text:
        return "I can greet you, tell you my name, or chat a little. Try saying 'hi'!"

    elif text in ["thanks", "thank you"]:
        return "You're welcome!"

    elif text in ["what can you do", "what do you do"]:
        return "I can chat about simple topics — try asking my name, time, or how I work."

    elif text in ["what time is it", "time"]:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    elif text in ["what is the date", "date", "today's date"]:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"

    elif text in ["how old are you", "your age"]:
        return "I don't have an age, I'm just lines of code!"

    elif text in ["where are you from", "where do you live"]:
        return "I live inside your computer, running as a Python script."

    elif text in ["are you human", "are you a robot", "are you real"]:
        return "Nope, I'm a chatbot — just following if-else rules."

    elif text in ["what is python"]:
        return "Python is a popular programming language used for AI, web, and more."

    elif text in ["tell me a joke", "joke"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif text in ["good morning"]:
        return "Good morning! Hope you have a great day ahead."

    elif text in ["good night"]:
        return "Good night! Sleep well."

    # Exit commands
    elif text in ["bye", "exit", "quit", "goodbye"]:
        return "EXIT"

    # Default fallback
    else:
        return "Sorry, I didn't understand that. Type 'help' for options."


def run_chatbot():
    print("=" * 50)
    print(" Simple Rule-Based Chatbot ")
    print(" Type 'bye', 'exit', or 'quit' to end the chat ")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Take care.")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()