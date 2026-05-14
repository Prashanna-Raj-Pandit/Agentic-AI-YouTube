# OpenAI Function Calling — AI Engineering Series

This is the code from Video 1 of my AI Engineering series on YouTube.

The video covers one of the most fundamental concepts in building AI agents — 
function calling with the OpenAI API. By default, an LLM can only generate 
text based on its training data. It hallucinates when it doesn't know something. 
Function calling gives it a way to reach out and call your actual Python 
functions — check real weather, query databases, search the web — instead of 
making things up.

## What this code does

It implements a simple weather assistant that demonstrates the full function 
calling loop. You ask about the weather in any city, the LLM decides to call 
the get_weather function, we execute it, send the result back, and the LLM 
generates a natural language response. The weather data is hardcoded for now — 
a real weather API integration is coming in the next video.

## How it works

There are three steps to implement function calling:

Step 1 — Define the tool schema. This is a dictionary that describes your 
function to the LLM. It tells it the function name, what it does, and what 
parameters it expects.

Step 2 — Define the actual Python function. This is where the real logic 
lives. In this video it returns hardcoded data, but in production you'd call 
a real API here.

Step 3 — Handle the tool call loop. We send the messages and tool schema to 
the API, check the finish_reason, execute the function if the LLM requests it, 
and keep looping until we get a final answer.

## Setup

```
Clone the repo and install dependencies:

pip install openai python-dotenv rich

or if you're using UV (recommended):

uv add openai python-dotenv rich

Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your-key-here

Then run:

python tools.py
```



## Series

This is part of an ongoing AI engineering series where we build up from 
the foundations all the way to full multi-agent systems.

Video 1 — Project setup (UV, venv, .env), Function calling (this video)

Video 2 — Async OpenAI SDK (coming soon)

Video 3 — Agent as a tool (coming soon)

## About

I'm Prashanna, an ML engineer and CS graduate student. I build AI systems 
and break down complex concepts into real working code. Subscribe on YouTube 
for weekly AI engineering videos.

* YouTube: https://www.youtube.com/@prashanna_raj

* LinkedIn: https://www.linkedin.com/in/ra-prashanna/
* GitHub: https://github.com/Prashanna-Raj-Pandit