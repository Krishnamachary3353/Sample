import ollama

# Correct initialization using 'host'
ollama_client = ollama.Client(host="http://localhost:11434")

response = ollama_client.chat(
    model="mistral",
    messages=[{"role": "user", "content": "Hello, Mistral!"}]
)

print("Response:", response)
