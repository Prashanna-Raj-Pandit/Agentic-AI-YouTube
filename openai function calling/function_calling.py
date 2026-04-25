from dotenv import load_dotenv
load_dotenv(override=True)
from openai import OpenAI
from rich import print
import json

client=OpenAI()

# step 1:  define the tool schema

weather_tool={
    "type":"function",
    "function":{
        "name":"get_weather",
        "description":"Get the current weather of a city",
        "parameters":{
            "type":"object",
            "properties":{
                "city":{
                    "type":"string",
                    'description':"The city name"
                }
            },
            "required":['city'],
            "additionalProperties":False
        }
    }
}

# Step 2:
def get_weather(city):
    return {"city":city,"temperature":"22C", "condition":"sunny"} # we will implement the weather API in the next video

#Step 3: Handle the tool call loop

def run_with_tools(user_message):
    messages=[{"role":"user","content":user_message}]

    while True:
        response=client.chat.completions.create(model="gpt-4o-mini",
                                                messages=messages,
                                                tools=[weather_tool])
        
        choice=response.choices[0]
        print(choice)
        if choice.finish_reason=="tool_calls":
            tool_call=choice.message.tool_calls[0]
            function_name=tool_call.function.name
            argument=json.loads(tool_call.function.arguments)
            # call the fuction
            tool_name=globals().get(function_name)
            result=tool_name(**argument)

            messages.append(choice.message)
            messages.append({
                "role":"tool",
                "content":json.dumps(result),
                "tool_call_id":tool_call.id
            })
        else:
            return choice.message.content

print(run_with_tools("What is the weather in Tokyo?"))
