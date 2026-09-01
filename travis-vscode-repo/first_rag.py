from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Import LangChain's offline testing tools
from langchain_core.embeddings import FakeEmbeddings
from langchain_community.chat_models import FakeListChatModel

# 1. Prepare your private knowledge base
private_knowledge = [
    "FedEx Standard Operating Procedure N2.0 requires all outbound sorts to complete by 03:30 AM local time.",
    "Travis Long is the District Planning Manager for the Northern California District.",
    "The official color code for FedEx Ground operations is Purple and Orange.",
    "JP does OTS stuff, I guess.",
]

# 2. Use Fake Embeddings
embeddings = FakeEmbeddings(size=1536)
vector_store = DocArrayInMemorySearch.from_texts(private_knowledge, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 1})

# 3. Prompt Template
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 4. Provide MULTIPLE sequential test answers in the response list!
model = FakeListChatModel(
    responses=[
        "(OFFLINE TEST 1): According to N2.0, all outbound sorts must be completed by 03:30 AM local time.",
        "(OFFLINE TEST 2): Travis Long is the Northern California District Planning Manager.",
        "(OFFLINE TEST 3): The official color codes are Purple and Orange."
    ]
)

# 5. Build the RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# 6. Test Query 1 (Consumes the first response)
print("\n--- Running Query 1 ---")
response1 = rag_chain.invoke("What time must outbound sorts be completed?")
print(response1)

# 7. Test Query 2 (Consumes the second response)
print("\n--- Running Query 2 ---")
response2 = rag_chain.invoke("Who is the District Planning Manager?")
print(response2)

# 8. Test Query 3 (Consumes the third response)
print("\n--- Running Query 3 ---")
response3 = rag_chain.invoke("What is the official color code?")
print(response3)
print("------------------------\n")
