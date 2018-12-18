
 

 
print('if you have some problem to choice you can ask me~')


import random

 

responses = {

  ("hello", "hi", "greetings", "sup", "what's up",): "hi~ can I help you?",

  ("name", "name please", "your name", "what's your name?"): "my name is ChatBot",

  ("weather", "hows weather", "what's today's weather?"): "It's sunny.",

  ("thanks","thank youbye","oh thank","fine thank"): "your welcome!",

  ("menu", "what can you do?", "how can i ask?"): "you can ask movies,food....and so on"

  }

 

 

 

greeting_words = ("food", "chioce some food to me", "i am hungry")

greeting_responses = ["noodles", "kimbap", "jjigae", "fried chicken"]

 

greeting_words2 = ("movie", "chioce some movies to me", "movies")

greeting_responses2 = ["Fantastic Beasts: The Crimes of Grindelwald", "Spider-Man: Into the Spider-Verse", "Intimate Strangers"]

 

greeting_words3 = ("drink", "chioce some drink to me", "drinking")

greeting_responses3 = ["soda", "coke", "water", "lemonade"]

 

responses_no = ["i don't know", "say once again", "*nope*","try again"]

 

 

 

        

def respond(user_message):

    # dictionary에 존재하는 모든 key(tuple)에 대해서

    for user_messages in responses:

        # 해당하는 tuple에 질문이 포함되는지

        if user_message in user_messages:

            return responses[user_messages]

        elif user_message in greeting_words:

            return random.choice(greeting_responses)

        elif user_message in greeting_words2:

            return random.choice(greeting_responses2)

        elif user_message in greeting_words3:

            return random.choice(greeting_responses3)

    else:

        return random.choice(responses_no)

    

 

 

while True:

    user_message = input('chatbot:')

    if user_message == 'bye':

        print("See you soon ~")

        break

    print(respond(user_message))

    
