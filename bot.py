import discord, os, requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='/', intents=intents)

def get_quotes():
    response = requests.get('https://officeapi.akashrajpurohit.com/quote/random')
    if response.status_code == 200:
        json_data = response.json()
        quote = json_data.get('quote')
        character = json_data.get('character')
        return (f" \"{quote}\" - {character}")
    

@client.command(name='quote', description='Sends a random quote from the office tv show')
async def slash_command(interaction: discord.Interaction):
    await interaction.send(get_quotes())
    

@client.event
async def on_ready():
    await client.tree.sync()
    print(f'Bot is live!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content == '!quote':
#         await message.channel.send(get_quotes())



client.run(token)
