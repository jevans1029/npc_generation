import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from npc import Npc

load_dotenv()
client = OpenAI()


def generate_npc(description):
    prompt = f"""
Create a stat block for a dungeons and dragons npc.
Read the description between the <DESCRIPTION> and </DESCRIPTION> tags.
Next, think about the stats of the npc. What abilities does the npc have.
Send the result to the function called Npc in the correct format.

<DESCRIPTION>
{description}
</DESCRIPTION>
"""
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Dungeons and Dragons 5th edition dungeon master."},
            {"role": "user", "content": prompt}
        ],
        tools=[
        {
            "type": "function",
            "function": {
                "name": "Npc",
                "description": "The statistics of an Npc",
                "parameters": Npc.model_json_schema(),
            },
        }
    ],
    tool_choice={
        "type": "function",
        "function": {"name": "Npc"},
    },
    )
    npc = Npc.model_validate_json(
        completion.choices[0].message.tool_calls[0].function.arguments
    )
    return npc
