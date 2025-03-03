import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Configure API key
genai.configure(api_key)

# Select model
model = genai.GenerativeModel("gemini-1.5-pro")  # Change model if needed

# Interactive loop
while True:
    user_input = input("\nAsk me anything (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = model.generate_content(user_input)
        if response and response.text:
            print("\nGemini AI:", response.text, "\n")
        else:
            print("\nGemini AI: Sorry, I couldn't generate a response.\n")
    except Exception as e:
        print("Error:", e)