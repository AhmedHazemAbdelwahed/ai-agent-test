from google import genai

client = genai.Client(api_key="AQ.Ab8RN6Kz_vBCCrgZbN3uQcDzvqmoThTjhzyXWIAcisKtJIU3BQ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what a Kubernetes Pod is in 2 sentences."
)

print(response.text)