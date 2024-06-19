import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables.base import RunnableSequence
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# 1. Vectorise the travel experiences csv data
loader = CSVLoader(file_path="travel_experiences.csv")
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

# 2. Function for similarity search
def retrieve_info(query):
    similar_response = db.similarity_search(query, k=7)

    page_contents_array = [doc.page_content for doc in similar_response]

    return page_contents_array

# 3. Setup RunnableSequence & prompts
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
You are a world-class travel advisor. 
I will share my travel preferences and previous trip experiences with you, and you will give me the best travel recommendations 
based on these experiences, and you will follow ALL of the rules below:

1/ Recommendations should be very similar or even identical to the past experiences in terms of category, destination type, 
and activities if they align with the user's preferences.

2/ If the past experiences are irrelevant, then try to mimic the type of the experiences to suggest new destinations.

3/ If a city is given in the message about the upcoming trip the suggestions must be close to the city within a 1 hour commute.

4/ Place the reccomendations in a table with the category, location, reccomendation name, a description of the reccomendation, and a comment on how it relates to past experiences. Include a maximum of 5 reccomendations.

5/ Pay attention to the rating a low rating means that the activity was not previously enjoyed. Use that in your decision making process to avoid activities that may also not be enjoyed.

Below is a message about what I am looking for in my upcoming trip:
{message}

Here is a list of my past travel experiences with rating from 1 to 5:
{travel_preferences}

Please write the best travel recommendations that you think I will enjoy:
"""

prompt = PromptTemplate(
    input_variables=["message", "travel_preferences"],
    template=template
)


chain = prompt | llm

# 4. Retrieval augmented generation
def generate_response(message):
    travel_preferences = retrieve_info(message)
    response = chain.invoke({
    "message": message,
    "travel_preferences": travel_preferences
    })
    return response

# message = 'Find me things to do in Brno, Czechia that is good for a large amount of people.'
# print(f"\n\n{retrieve_info(message)}")
# print(f"\n\n{generate_response(message)}")

# Streamlit interface for user input and displaying recommendations
st.title("Personalized Travel Planner")
user_input = st.text_area("Describe the details of the trip and what you are looking for:")

if st.button("Get recommendations"):
    if user_input:
        response = generate_response(user_input)
        st.write("### Recommended Travel Destinations")
        st.write(response.content)
    else:
        st.write("Please enter your travel preferences and past experiences.")
