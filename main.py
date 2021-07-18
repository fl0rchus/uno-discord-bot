import discord
from discord.ext import commands
import random
import os

TOKEN = os.environ.get('TOKEN')

bot = commands.Bot(command_prefix="!")

speakers = ["Ferfer", "murd0c", "Mati", "Luqui", "Nacho", "Flwerr", "bri_96"]
subject = ["Rust", "Node", "React", "Haskell", "Python",
           "GraphQL?", "Ingles ah no Moni no está jeje"]

cosas = ["Joya", "JAJAJA LPM", "chupala gato",
         "ferlacion",  "eee no se, que se yo", "No se puede creer estos caras de remil verga", "Sos trolo?", "me quiero morir", "si si", "aham", "messirve", "FIUUUUMBA", "VALORES Y PRINCIPIOS", "COMO NO TE VAN A GUSTAR LOS SANGUCHITOS DE MIGA?", "ah re"]

month = ["Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
day = random.randint(1, 31)

saludos = ["Buenos dias lucesitas", "Buendia Pimpollos",
           "Arriba remolonxs que es un nuevo dia", "Levantensé parásitos miren la hora que es y ustedes durmiendo como cerdos", "Holo", "https://www.youtube.com/watch?v=L2ggChyoBWM"]

despedida = ["ay deberia estar durmiendo", "deberia estar trabajando xd"]


@bot.command()
async def frase(ctx):
    await ctx.send(random.choice(cosas))


@bot.command()
async def morning(ctx):
    await ctx.send(random.choice(saludos))


@bot.command()
async def bye(ctx):
    await ctx.send(random.choice(despedida))


@bot.command()
async def charla(ctx):
    fecha = f"{day} de {random.choice(month)}"
    message = f"La próxima charla será de {random.choice(speakers)} sobre {random.choice(subject)} el día {fecha}"
    await ctx.send(message)


@bot.command()
async def issue(ctx):
    await ctx.send("No se aceptan issues")


@bot.command()
async def frases(ctx):
    await ctx.send("deberia tirar un arreglo de frase ah re")


@bot.command()
async def buenosdias(ctx):
    await ctx.send("https://www.youtube.com/watch?v=7epc90S4w_E")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="ser alto bot"))
    print("Alive")

bot.run(TOKEN)
