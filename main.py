import discord
from pathlib import Path
from codes import parseLatex, config

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('##'):
        command = message.content.replace('##', '').split()
        load = config.getLoad(command)
        await message.channel.send(load)
    
    elif message.content.startswith('$') and message.content.endswith('$'):
        print(message.author)
        print("Message recieved, parsing to svg...")
        await message.channel.send('Parsing...')
        latexExpression = message.content[1:-1]
        await parseLatex.parseExpression(latexExpression)
        if Path("svg/expression.svg").stat().st_size == 0:
            await message.channel.send("Invalid Latex Syntax.")
        else:
            await message.channel.send(file=discord.File(r"png/expression.png"))

client.run("ODMyODc4MDUzNzQ2NTQwNTQ0.YHqMIg.Vdyvqg4J-d7JPdNDENX5mCFuJKg")