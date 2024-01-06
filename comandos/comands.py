
#help
async def help(interaction, help):
    await interaction.response.send_message(f'**Lista de comandos:**\n``/status`` = *Te mostra o status atual do korepi*\n``/downloadkorepi`` = *Donwload da última versão do korepi*\n', ephemeral=True)

#statuskorpei
async def status(interaction, status):
   try: 
       with open('status/status.txt', 'r') as arquivo:
           status = arquivo.read()
           await interaction.response.send_message(f'O status atual do korepi é: ``{status}``', ephemeral=True)

   except:
      await interaction.response.send_message('Não foi possível obter o status atual do korepi😥')

#downloadkorepi
def sponsor():
    with open('status/CargosRequeridos.txt', 'r') as arquivo:
        return arquivo.read().strip()
import requests
async def downloadkorepi(interaction):
    try:
        repo_owner = 'Cotton-Buds'
        repo_name = 'colorpicker'

        response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest')
        data = response.json()

        assets = data.get('assets', [])
        file_name = assets[0].get('name', 'N/A')
        release_name = data.get('name', 'N/A')
        tag_name = data.get('tag_name', 'N/A')

        download_link = f'https://github.com/{repo_owner}/{repo_name}/releases/download/{tag_name}/{file_name}'

        await interaction.response.send_message(f'> Última versão do korepi: **{release_name}** \nCargo Requerido:``{sponsor()}``\n||{download_link}||\nSenha:||1234||\n<@{interaction.user.id}>', ephemeral=True)
        return release_name
    except Exception as e:
        print(f'Erro ao obter última versão do korepi: {e}')
        await interaction.response.send_message('Erro ao obter a última versão...')



#setstats
import asyncio
from typing import Optional
from discord import app_commands
from discord import Interaction

async def setstatus(interaction: Interaction,
                    newstate: Optional[app_commands.Range[str, 0, 100]],
                    set_cargos_requeridos: Optional[app_commands.Range[str, 0, 100]], setstatus):
    if newstate is not None:
      if interaction.user.guild_permissions.administrator:
        with open('status/status.txt', 'w') as arquivo:
            arquivo.write(newstate)
            await interaction.response.send_message(f'O status foi alterado para: ``{newstate}``!', ephemeral=True)
      else:
         await interaction.response.send_message('Você não é Administrador porque esta tenatndo?', ephemeral=True)
         print(f'{interaction.user.id} = {interaction.user} Tentou usar o SetStatus')
    else:
        if set_cargos_requeridos is not None:
            if interaction.user.guild_permissions.administrator:
               with open('status/CargosRequeridos.txt', 'w') as arquivo:
                arquivo.write(set_cargos_requeridos)
                await interaction.response.send_message(f'Os cargos foram alterados para ``{set_cargos_requeridos}``!', ephemeral=True)
            else:
               print(f'{interaction.user.id} = {interaction.user} Tentou usar o SetStatus')
               await interaction.response.send_message('Você não é Administrador porque esta tenatndo?', ephemeral=True)
        else:
           await interaction.response.send_message('Forneça algum valor em alguma das duas opcões!', ephemeral=True)

#clear
async def clear(interaction: Interaction,
                number: app_commands.Range[int, 0, 500], clear):
    if interaction.user.guild_permissions.administrator:
       deleted_mensages = await interaction.channel.purge(limit=number)
       msg = await interaction.channel.send(f'{len(deleted_mensages)} Mensagens foram apagadas por <@{interaction.user.id}>!')
       await asyncio.sleep(4)
       await msg.delete()
    else:
        print(f'{interaction.user.id} = {interaction.user} Tentou usar o clear')
        await interaction.response.send_message('Você não é Administrador porque esta tenatndo?', ephemeral=True)


#depmykey
import os

async def depmykey(interaction: Interaction, mykey: app_commands.Range[str, 0, 100]):
      if mykey.startswith(f'micah-{interaction.user.id}'):
           filename = f'keys/{interaction.user.id}.txt'
           if os.path.exists(filename):
               await interaction.response.send_message('Você já tem uma key registrada use o ``/deletekey``.')    
           else:
               with open(filename, 'a') as arquivo:
                   arquivo.write(mykey)
                   await interaction.response.send_message(f'Sua key: ``{mykey}`` foi registrada!')
      else:
          await interaction.response.send_message('Coloque uma key válida!')

#deletemykey
async def deletemykey(interaction: Interaction):
      filename = f'keys/{interaction.user.id}.txt'
      if os.path.exists(filename):
          os.remove(filename)
          await interaction.response.send_message('Key deletada com sucesso!')
      else:
          await interaction.response.send_message('Sua key ou ja foi deletada ou ja expirou!')
    

#expirekey
from datetime import datetime, timedelta

async def expirekey():
    diretorio = 'keys/'
    dias = 7
    try:
        for arquivo in os.listdir(diretorio):
            caminho = os.path.join(diretorio, arquivo)
            data =  datetime.fromtimestamp(os.path.getatime(caminho))
            data_expired = datetime.now() - timedelta(days=dias)

            if data < data_expired:
                os.remove(caminho)
                print(f'O arquivo {caminho} expirou e foi deletado!')
    except OSError as e:
        print(f'Erro ao verificar expiração: {e}')


