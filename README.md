# Personalized Travel Planner with LangChain

This application leverages LangChain to perform knowledge embeddings of all my past travel experiences. 
It then takes in a prompt for an activity you want to do in a certain city and looks through the embeddings to find past experiences that match the activity prompt entered. 
An input prompt is then assembled and placed into ChatGPT to provide personalized travel recommendations.

## Features

	•	Vectorizes Travel Experiences: Uses LangChain to embed past travel experiences from a CSV file.
	•	Similarity Search: Finds past experiences similar to a given query using FAISS.
	•	Generates Recommendations: Uses ChatGPT to generate travel recommendations based on past experiences and user queries.

## Installation

1.	Clone the repository:
```
git clone git@github.com:zdefranc/knowledge-embedding-travel-app.git
cd knowledge-embedding-travel-app
```

2. Create a virtual environment and activate it:
```
python -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

4. Create a .env file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1.	Run the Streamlit application:
```
streamlit run travel_app.py
```

## Acknowledgment

Thank you for the great tutorial and starting code made by AI Jason. 

["How to give GPT my business knowledge?" - Knowledge embedding 101](https://www.youtube.com/watch?v=c_nCjlSB1Zk)


[Github Repo](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbm5mdHFZT1VhMUU3My1SdnhhY1BXWjk4Ql84Z3xBQ3Jtc0ttWnBVbXl3Q0ptNFU5STF2ajViM3VsSFlSREw3MGlCbmtvOEM5ZVQ0WFV4aTlxRFhHOUVDNDlLT0l6blpUdk4xTXpqdWxIRUhsMWc1YmhvNzNWbTFpdmJMb2RCOV9hcGpkVXlFWW9saG92NzlDMkU2RQ&q=https%3A%2F%2Fgithub.com%2FJayZeeDesign%2FKnowledgebase-embedding&v=c_nCjlSB1Zk)

