from typing import Optional
import discord
from discord import app_commands
from comandos import comands
from discord import Interaction
from discord.ext import tasks

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
    await expirekey()
    await update_presence()
    expirekey.start()
    update_presence.start()

@tasks.loop(seconds=30)
async def update_presence():
   await comands.update_presence(bot)


async def get_version():
    return await comands.get_version()

@bot.tree.command()
async def help(interaction: Interaction):
    """Ajuda Sobre o Bot ShuKurenais"""
    await comands.help(interaction, help)

@bot.tree.command()
@app_commands.describe(number='Quantas mensagens?')
async def clear(interaction: Interaction,
                number: app_commands.Range[int, 0, 500]):
    """Apaga Mensagens *Somente Administradores*"""
    await comands.clear(interaction, number, clear)

@bot.tree.command()
async def status(interaction: Interaction):
    """Status atual do korepi hehehe"""
    await comands.status(interaction, status)


@bot.tree.command()
@app_commands.describe(newstate='Novo Estado do korepi', set_cargos_requeridos='Seta os cargos nescessários')
async def setstatus(interaction: Interaction,
                    newstate: Optional[app_commands.Range[str, 0, 100]],
                    set_cargos_requeridos: Optional[app_commands.Range[str, 0, 100]]):
    """Definir Status do korepi*Somente Administradores*"""
    await comands.setstatus(interaction, newstate, set_cargos_requeridos, setstatus)


@bot.tree.command()
async def downloadkorepi(interaction: Interaction):
    """Baixar última versão do korepi"""
    await comands.downloadkorepi(interaction)


@bot.tree.command()
@app_commands.describe(mykey='Sua key korepi!')
async def depmykey(interaction: Interaction,
                   mykey: app_commands.Range[str, 0, 100]):
    """Salva sua key e te mostra quando você pede download"""
    await comands.depmykey(interaction, mykey)

@bot.tree.command()
async def deletemykey(interaction:Interaction):
    """Deleta sua key armazenada antes de expirar"""
    await comands.deletemykey(interaction)

@tasks.loop(hours=1)
async def expirekey():
    await comands.expirekey()


def token():
    with open('status/token.txt', 'r') as arquivo:
        return arquivo.read().strip()

token_bot = token()

bot.run(token_bot)
