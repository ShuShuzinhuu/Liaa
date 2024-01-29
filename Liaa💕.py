from typing import Optional
import discord
from discord import app_commands
from comandos import comands
from discord import Interaction
from discord.ext import tasks
import asyncio

MY_GUILD = discord.Object(id=986023438634352660)

class Mybot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

bot = Mybot()

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    await update_presence()
    update_presence.start()
    await asyncio.sleep(3 * 60 * 60)
    restart_server.start()

@tasks.loop(minutes=30)
async def update_presence():
   await comands.update_presence(bot)

async def get_version():
    return await comands.get_version()

@tasks.loop(hours=3)
async def restart_server():
    await comands.restart_server()

@bot.tree.command()
async def send_message(interaction,
                       mensagem: app_commands.Range[str, 0, 50]):
    """Manda uma mensagem para o servidor de PAL"""
    await comands.send_message(interaction, mensagem)

@bot.tree.command()
async def start_server(interaction):
    """Inicia o Servidor de PalWorld"""
    await comands.start_server(interaction)

@bot.tree.command()
async def stop_server(interaction):
    """Fecha o servidor de PalWorld"""
    await comands.stop_server(interaction)

@bot.tree.command()
@app_commands.describe(number='Quantas mensagens?')
async def clear(interaction: Interaction,
                number: app_commands.Range[int, 0, 500]):
    """Apaga Mensagens *Somente Administradores*"""
    await comands.clear(interaction, number, clear)

def token():
    with open('status/token.txt', 'r') as arquivo:
        return arquivo.read().strip()

token_bot = token()

bot.run(token_bot)
