import requests

# Set your Gemini API URL and API key (replace with your credentials)
GEMINI_API_URL = "insert_gemini_api_endpoint_here"  # Replace with the actual Gemini API endpoint
API_KEY = "insert_gemini_api_endpoint_here"  # Replace with your Gemini API key

def get_gemini_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "gemini-1",  # Or another model name if available
    }
    response = requests.post(GEMINI_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        return "Error: Could not get response from Gemini API."

def chat():
    print("Welcome to the Gemini Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            bot_response = get_gemini_response(user_input)
            print("Gemini: " + bot_response)

if __name__ == "__main__":
    chat()