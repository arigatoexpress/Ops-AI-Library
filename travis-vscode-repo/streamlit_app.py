import streamlit as st
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.embeddings import FakeEmbeddings
from langchain_community.chat_models import FakeListChatModel

# 1. Set up the Streamlit UI Page
st.set_page_config(page_title="FedEx AI Prototype", page_icon="📦")
st.title("📦 FedEx Offline Assistant")
st.markdown("This is a 100% offline, air-gapped prototype using local vector search.")

# 2. Manage State (Crucial for Streamlit)
# Streamlit reruns the whole script every time you click a button. 
# We use st.session_state to prevent the Fake Model from resetting to the first answer!
if "fake_model" not in st.session_state:
    st.session_state.fake_model = FakeListChatModel(
        responses=[
            "(OFFLINE TEST 1): JP is a newly hired District Field Operations Specialist for the Northern California District.",
            "(OFFLINE TEST 2): Travis Long is a Northern California District Engineering Specialist.",
            "(OFFLINE TEST 3): The official color codes are Purple and Orange.",
            "(OFFLINE TEST 4): According to N2.0, all outbound sorts must be completed by 03:30 AM local time."
        ]
    )

# 3. Prepare Knowledge Base & Retriever
@st.cache_resource # This caches the database so it doesn't rebuild on every click
def setup_retriever():
    private_knowledge = [
        "FedEx Standard Operating Procedure N2.0 requires all outbound sorts to complete by 03:30 AM local time.",
        "Travis Long is an Engineering Specialist that works with Express and Ground for the Northern California District.",
        "The official color code for FedEx Ground operations is Purple and Orange.",
    ]
    embeddings = FakeEmbeddings(size=1536)
    vector_store = DocArrayInMemorySearch.from_texts(private_knowledge, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 1})

retriever = setup_retriever()

# 4. Build the RAG Chain
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | st.session_state.fake_model
    | StrOutputParser()
)

# 5. Build the Interactive UI
# Create a text input box for the user
user_query = st.text_input("Ask a question about operations:")

# Create a submit button
if st.button("Submit Query", type="primary"):
    if user_query:
        with st.spinner("Searching internal documents..."):
            # Run the LangChain pipeline
            response = rag_chain.invoke(user_query)
            
            # Display the result in a success box
            st.success("Query Complete!")
            st.write("**Answer:**")
            st.info(response)
    else:
        st.warning("Please enter a question first.")
