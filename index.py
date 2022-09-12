import discord
from discord.ext import commands

import os
from dotenv import load_dotenv, find_dotenv

from urllib import parse, request

import re

load_dotenv(find_dotenv())

ncp_bot = commands.Bot(command_prefix="ncp>", description="Bot oficial de NoCopeo Gang", intents=discord.Intents.all())

@ncp_bot.event
async def on_ready():
    await ncp_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Bombardeo a la casa de Yanfri"))
    print("Bot listo")

@ncp_bot.event
async def on_message(message):
    if message.author == ncp_bot.user:
        return

    if message.content.startswith("ncp>"):
        await ncp_bot.process_commands(message)

@ncp_bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Comandos", description="Lista de comandos disponibles", color=discord.Color.yellow())

    embed.set_thumbnail(url="https://firebasestorage.googleapis.com/v0/b/anny-kaktus.appspot.com/o/icon%20(1).png?alt=media&token=b8d993c4-7d20-4445-934a-97346b5de12b")
    embed.add_field(name="Todos los comandos van con el prefijo ncp>", value="---------------", inline=True)
    embed.add_field(name="ayuda", value="Muestra los comandos disponibles", inline=False)
    embed.add_field(name="info", value="Muestra información sobre el bot y el servidor", inline=False)
    embed.add_field(name="youtube", value="Busca un video en YouTube, se enviará el primer resultado --EN DESARROLLO--", inline=False)
    embed.set_footer(text="Cualquier duda comunicarse/pingear a pulgueta_#2810")

    await ctx.send(embed=embed)

@ncp_bot.command()
async def care(ctx):
    await ctx.send("verga")

@ncp_bot.command()
async def info(ctx):
    embed = discord.Embed(title=ctx.guild.name, description="Bot oficial de Nocopeo Gang", color=discord.Color.blue())
    embed.add_field(name="Creador", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Invitación", value=os.getenv("DISCORD_INVITE"), inline=False)
    embed.set_thumbnail(url="https://firebasestorage.googleapis.com/v0/b/anny-kaktus.appspot.com/o/Screenshot_1.png?alt=media&token=d5b07119-c816-4cb7-9989-a08fbee28fef")
    embed.add_field(name="Acerca de", value="Servidor creado en 2016 por SrTakashi y Kevin el gordilli. Actualmente con +100 miembros y originario de Barrancabermeja, Colombia.", inline=True)
    embed.add_field(name="Miembros actuales:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Creado el:", value=ctx.guild.created_at, inline=False)
    embed.add_field(name="ID del servidor:", value=ctx.guild.id, inline=False)

    await ctx.send(embed=embed)

@ncp_bot.command()
async def youtube(ctx, *, search):
    base = "https://www.youtube.com/results?"
    q = parse.urlencode({"search_query": search})
    content = request.urlopen(base + q)

    results = re.findall('href=\"\\/watch\\?v=(.{11})', content.read().decode())
    print(results[0])
    # await ctx.send("http://www.youtube.com/watch?v=" + search_results[0])
    
ncp_bot.run(os.getenv("DISCORD_TOKEN"))