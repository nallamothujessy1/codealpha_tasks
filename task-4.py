# TASK 4: Basic Chatbot 

def chatbot():  #function using
    print(" Simple Chatbot")
    print("Type 'bye' to exit.\n")
    
    #loop using
    
    while True:
        user = input("You: ").lower()  #input/output using
        
        if user == "hello":
            print("Bot: Hi!")  #if-elif using

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
