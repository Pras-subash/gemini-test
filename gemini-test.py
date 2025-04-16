import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# print genai.listmodels() to see available models
print(genai.list_models())
for i, m in zip(range(5), genai.list_models()):
    print(f"Name: {m.name} Description: {m.description} support: {m.supported_generation_methods}")

# Create model instance
# model = genai.GenerativeModel('gemini-pro-latest')
# model = genai.GenerativeModel('models/text-bison-001')
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def chat_with_gemini():
    # Initialize chat
    chat = model.start_chat(history=[])
    print("Chatbot: Hello! I'm a Gemini-powered chatbot. Type 'quit' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
            
        try:
            # Get response from Gemini
            response = chat.send_message(user_input)
            print("Chatbot:", response.text)
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    chat_with_gemini()