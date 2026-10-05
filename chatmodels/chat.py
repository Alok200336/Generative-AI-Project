from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2",
    temperature=0.7,
    max_tokens=50
)

response = model.invoke("write a poem about the ocean")
print(response.content)