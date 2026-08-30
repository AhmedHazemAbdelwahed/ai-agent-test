from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what a Kubernetes Pod is in 2 sentences."
)

print(response.text)