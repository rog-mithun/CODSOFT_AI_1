import re

def simple_chatbot(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    greeting_patterns = ['hi', 'hello', 'hey', 'howdy']
    goodbye_patterns = ['bye', 'goodbye', 'see you', 'farewell']
    weather_patterns = ['weather', 'forecast', 'temperature']
    help_patterns = ['help', 'assistance', 'support']
    purpose_patterns = ['what are you', 'your purpose', 'who are you']

    # Check for greetings
    if any(pattern in user_input for pattern in greeting_patterns):
        return "Hello! How can I help you today?"

    # Check for goodbyes
    elif any(pattern in user_input for pattern in goodbye_patterns):
        return "Goodbye! Have a great day."

    # Check for weather-related queries
    elif any(pattern in user_input for pattern in weather_patterns):
        return "I'm sorry, I don't have the current weather information."

    # Check for requests for help
    elif any(pattern in user_input for pattern in help_patterns):
        return "Sure, I can help you. What do you need assistance with?"

    # Check for questions about the chatbot's purpose
    elif any(pattern in user_input for pattern in purpose_patterns):
        return "I am a simple rule-based chatbot designed to provide information and assistance."

    # Specific responses for certain queries
    elif "your name" in user_input:
        return "I'm a chatbot, and you can call me ChatBOT."

    # Default response for unknown inputs
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"

# Example usage
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types "exit"
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
