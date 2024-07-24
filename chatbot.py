data = {
  "hi": "Greetings! I'm here as a friendly chatbot ready to assist you.",

"hello": "Hello there! How may I be of help to you today?",

"what is your name": "My name is Chatbot, at your service.",

"where are you from": "I don't have a fixed location; I'm always available to chat!",

"how are you": "I'm doing well, thank you. How can I support you today?",
}

def get_response(user_input):
  for pattern, response in data.items():
    if pattern in user_input.lower():
      return response
  return "Could you kindly phrase your statement differently?"
  
print("Chatbot: Hello! I'm a straightforward chat assistant here to help you!")
while True:
  user_input = input("You: ")
  if user_input.lower() == 'bye':
    print("Chatbot: Farewell! Wishing you a fantastic day!")
    break
  else:
    response = get_response(user_input)
    print("Chatbot:", response)
