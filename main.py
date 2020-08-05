import requests
import discord
import json

with open("token.json") as tokenFile:
    token = str(json.load(tokenFile)["token"])

client = discord.Client()

@client.event
async def on_ready():
    print("bot is ready")
@client.event
async def on_message(message):
    #Detects that the message was sent by a user(not the bot)
    if message.author != client.user:
        content = message.content.lower()
        if content.find("tell me a joke") != -1:
            embed = discord.Embed(title="Here you go")
            embed.add_field(name="Joke: ", value=str(requests.get("https://api.chucknorris.io/jokes/random").json()["value"]))

            await message.channel.send(content=None, embed=embed)

client.run(str(token))