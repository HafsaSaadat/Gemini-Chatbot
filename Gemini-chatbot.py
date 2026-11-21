from google import genai

# Add your Gemini API key between the quotation marks
client = genai.Client(api_key="YOUR_API_KEY_HERE")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    print("\033[92mGemini: \033[0m" + response.text)