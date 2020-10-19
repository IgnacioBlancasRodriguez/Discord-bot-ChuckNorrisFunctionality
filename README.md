# Discord-bot-ChuckNorrisFunctionality

This is a litle ten-minute project that I did as a way to try the requests module in python.

### What does it do?
The bot's pretty simple, In fact, we can divide it in three short steps:

> ### <strong>1º Step</strong>
> The bot listens for any message containing the phrase "tell me a joke" comming from any user in the server:
```python
@client.event
async def on_message(message):
    #Detects that the message was sent by a user(not the bot)
    if message.author != client.user:
        content = message.content.lower()
        if content.find("tell me a joke") != -1:
```
>