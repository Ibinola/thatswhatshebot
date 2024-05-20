import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
      
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == 'hello':
            await message.channel.send('Hello World!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTEzNDQwNDAyMjc5OTk2NjI5OA.GAcj4m.NX9uexLLQK6Oxu-QaTGzo2-cF3Fk8p-f9RJL4I') 