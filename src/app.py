from config import TOKEN
import discord

class QuotaLex(discord.Client):
    async def on_ready(self):
        print('Logged as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = QuotaLex()
client.run(TOKEN)