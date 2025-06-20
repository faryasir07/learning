from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

api_key = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=api_key,
    max_tokens=50
)

prompt = PromptTemplate(
    template="You are a helpful short-answer assistant. Reply with as few tokens as possible.\nQuery: {Query}",
    input_variables=["Query"]
)

chain = prompt | model | StrOutputParser()

while True:
    Query = input("You: ")
    if Query.lower() in ["/bye", "/exit"]:
        print("AI: Goodbye!")
        break

    AI = chain.invoke({"Query": Query})
    print("AI:", AI)
