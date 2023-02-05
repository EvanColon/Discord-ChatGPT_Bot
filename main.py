import openai
import discord

openai.api_key = "your_openai_api_key"

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.content}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    await message.channel.send(response)

client.run("your_discord_token")
