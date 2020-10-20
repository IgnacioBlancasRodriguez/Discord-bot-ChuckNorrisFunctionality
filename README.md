# 💬Discord-bot-ChuckNorrisFunctionality

This is a litle ten-minute project that I did as a way to try the requests module in python.

<hr>

## 🚀Technologies used

The bot uses three main technologies:
 * [Python](https://www.python.org/)
 * [Discord.py](https://discordpy.readthedocs.io/en/latest/)
 * [Request](https://pypi.org/project/requests/)

<hr>

## 🔧What does it do?
The bot's pretty simple, In fact, we can divide it in three short steps:

> ### <strong>1º Step</strong>
> The bot listens for any message containing the phrase "tell me a joke" comming from any user in the server:
>```python
>@client.event
>async def on_message(message):
>    #Detects that the message was sent by a user(not the bot)
>    if message.author != client.user:
>        content = message.content.lower()
>        if content.find("tell me a joke") != -1:
>```
>

<hr>

> ### <strong>2º Step</strong>
> The bot executes a GET request to a Chuck Norris jokes api:
>  * [Chuck Norris api](https://api.chucknorris.io/jokes/random)
>```python
>requests.get("https://api.chucknorris.io/jokes/random").json()["value"]
>```
>

<hr>

> ### <strong>3º Step</strong>
> The bot sends the joke as an embended message:
>```python
>embed = discord.Embed(title="Here you go")
>embed.add_field(name="Joke: ", value=str(requests.get("https://api.chucknorris.io/jokes/random").json()["value"]))
>
>await message.channel.send(content=None, embed=embed)
>```
>

<hr>

## 💻How to use it

Asuming you have installed the three technologies used:
 * Windows, MacOS and Linux:
    ```bat
    pip install request
    pip install discord.py
    ```
> ### <strong>Getting the api token</strong>
> Go to your discord developer portal, create a new bot, copy the token on the token tab and paste it on token.json.
>

<hr>

> ### <strong>Give permission to the bot</strong>
> On the developer portal ckick on the OAuth tab, select Manage Messages and select a server you want the bot to be in.
>

<hr>

> ### <strong>Ending</strong>
> To finish just run the script main.py.
>