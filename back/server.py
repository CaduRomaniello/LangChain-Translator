import os

from fastapi import FastAPI
from dotenv import load_dotenv
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
SERVER_PORT = os.getenv("SERVER_PORT")

# Create the language model
llm = ChatOpenAI(openai_api_key=OPEN_API_KEY)

# Create the prompt and output parser
prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following sentence to Portuguese: {sentence}"),
])

output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Create the FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Add the routes to the app
add_routes(
    app,
    chain,
    path="/translate",
)

# Run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)