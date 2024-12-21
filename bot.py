import discord
import requests
from dotenv import load_dotenv
import os
import time  

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PRODIA_API_KEY = os.getenv('PRODIA_API_KEY')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!generate'):
        prompt = message.content[len('!generate '):]
        await message.channel.send('Generating image...')
        image_url = generate_image(prompt)
        if image_url:
            await message.channel.send(image_url)
        else:
            await message.channel.send('Failed to generate image.')

def generate_image(prompt):
    url = "https://api.prodia.com/v1/sd/generate"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-Prodia-Key": f'{PRODIA_API_KEY}'
    }
    data = {
        "prompt": prompt,
        "steps": 50, 
        "num_images": 1,
        "width": 512,
        "height": 512
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            job_id = response.json()["job"]
            url = f"https://api.prodia.com/v1/job/{job_id}"
            
            time.sleep(9)

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                try:
                    status = response.json()["status"]
                    if status == "succeeded":
                        return response.json()["imageUrl"]
                    elif status == "failed":
                        print("Error: job failed")
                        return None
                    else:
                        print(f"Error: unknown status - {status}")
                        return None
                except (KeyError, IndexError):
                    print("Error parsing response JSON:", response.json())
                    return None
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None
            
        except (KeyError, IndexError):
            print("Error parsing response JSON:", response.json())
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

client.run(DISCORD_TOKEN)
