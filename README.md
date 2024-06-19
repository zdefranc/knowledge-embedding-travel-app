# Personalized Travel Planner with LangChain

This application leverages LangChain to perform knowledge embeddings of all your past travel experiences. 
It then takes in a prompt for an activity you want to do in a certain city and looks through the embeddings to find past experiences that match the activity listed. 
A prompt is then assembled and placed into ChatGPT to provide personalized travel recommendations.

## Features

	•	Vectorizes Travel Experiences: Uses LangChain to embed past travel experiences from a CSV file.
	•	Similarity Search: Finds past experiences similar to a given query using FAISS.
	•	Generates Recommendations: Uses ChatGPT to generate travel recommendations based on past experiences and user queries.
	•	Streamlit Interface: Provides a user-friendly interface to input trip details and display recommendations.

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



