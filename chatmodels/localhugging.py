from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
pipeline_kwargs=dict(
    temperature=0.7,
    max_new_tokens=50,
    top_p=0.9,
    repetition_penalty=1.2,))

chat_model = ChatHuggingFace(llm= llm)

chat_response = chat_model.invoke("what is ,machine learning?")
print(chat_response.content)

    