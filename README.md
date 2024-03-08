# LangChain Translator

## What is it?

This is a simple translator made using [LangChain framework](https://python.langchain.com/docs/get_started/introduction)

## How to run it?

The app is composed by two parts:
- Front-end
- Back-end

And both need to be being executed fot the app to work properly.

## Front-end

To run the front-end part, you need to install all the dependencies that this part requires. To do so, just run the following commands in your terminal in the root folder (you must have Node installed):

```bash
cd frontend
npm i
npm run start
```

It will install all the packages and start the front-end at port ```3000``` of your computer.

## Back-end

To run the back-end part, you also need to install all the dependencies that this part requires. To do so, just run the following commands in your terminal in the root folder (you must have Python and pip installed):

```bash
pip install "fastapi[all]"
pip install python-dotenv
pip install "langserve[all]"
pip install langchain
pip install langchain-openai
pip install langchain-core
```

It will install all the packages needed to run the back-end server.

## .ENV

Both front-end and back-end use.env files to access private variables, and those files are not in this repository. To complete the configuration of the project and run it, you'll need to create a `.env` file in the `front` and `back` directories. In the `back` directory, copy and paste this code:

```bash
OPEN_API_KEY = "paste your OpenAPI key here"
SERVER_PORT = 8000
```

The `OPEN_API_KEY` variable is your OpenAPI key, which you can access [here](https://platform.openai.com/api-keys). The `SERVER_PORT` is a variable that defines the port where your server will run, so make sure that you're choosing an available port. In the `front` directory, copy and paste this code: 

```bash
REACT_APP_SERVER_PORT = 8000
```

Make sure that `REACT_APP_SERVER_PORT` has the same value as `SERVER_PORT`.

## Running the program

After doing all these, you'll need to execute both the `front` and the `back`. To do it, go to the `front` directory and run the following code:

```bash
npm run start
```

After doing it, go to the `back` directory and run the following code:

```bash
python server.py
```

After completing all these steps, you can finally use the program. Enjoy it!