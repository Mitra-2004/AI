#Write a Python program to develop a simple chatbot using predefined rules and pattern matching.
print("Chatbot: Hello , I am simple chatbot !")
print("Type 'bye' to exit the system.")

while True:
    message = input("You:").lower()

    if "hello" in message or "hi" in message :
        print("chatbot: Hello ! How are you ?")

    elif "How are you" in message:
        print("Chatbot:I am fine , thankyou !")

    elif " What is your name " in message or "name" in message :
        print("Chatbot:I am simple Chatbot.")

    elif "Can you tell me about I2it College?" in message :
        print("Chatbot:I can provide you basic information about this college.")

    elif "bye" in message :
        print("Chatbot: Okie , bye !")

        break

    else:
        print("Chatbot: Sorry , I don't understand .")