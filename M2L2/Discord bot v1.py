import discord
import openai
import random
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import roll_dice
from bot_logic import guess_number
from bot_logic import guess_number

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)
openai.api_key = 'TOKEN'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ecology_def(ctx):
    await ctx.send(' 1.  Наука, изучающая взаимоотношения человека, животных, растений и микроорганизмов между собой и с окружающей средой.\n2.  Окружающая человека среда; условия существования животных и растений в какой-л. местности.')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass())

@bot.command
async def rolldice(ctx):
    await ctx.send(roll_dice())

@bot.command
async def guess_my_number(ctx):
    await ctx.send(guess_number())

@bot.command()
async def ideas(ctx):
    await ctx.send(idea())

@bot.command()
async def helpme(ctx):
    await ctx.send('функции в боте:\n   1.ecology_def\n     даёт значение слова "экология"\n    2.ideas:\n      даёт идеи как спасти планету\n  3.chat:\n       отправляет ваш запрос ChatGPT.')
    

@bot.command()
async def chat(ctx, *, message):
    response = openai.Completion.create(
        model="davinci",
        messages=[
            {"role": "system", "content": "You are a bot."},
            {"role": "user", "content": message}
        ],
        max_tokens=50
    )

    reply = response.choices[0].message.content

    await ctx.send(reply)

bot.run("TOKEN")
