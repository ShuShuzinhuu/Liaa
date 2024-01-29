################################
ip = ''
server_port = 0000
rcon_senha = ''
################################



#version
import requests
async def get_version():
        try:
         repo_owner = 'ShuShuzinhuu'
         repo_name = 'Liaa'
         response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest')
         response.raise_for_status()
         data = response.json()
         release_name = data.get('name', 'N/A')
         response.raise_for_status()
        except:
         release_name = 'I love You ShuKurenai`s'
            
        return release_name

#update_presence
import discord
async def update_presence(bot):
     current_version = ""
     new_version = await get_version()
     if new_version != current_version:
        current_version = new_version
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'💫{current_version}💫'))

#start_server
from discord import Interaction
import subprocess
async def start_server(interaction):
     if interaction.user.guild_permissions.administrator:
        try:
         caminho_executavel = 'C:\Games\Palworld.Early.Access\steamcmd\steamapps\common\PalServer\Pal\Binaries\Win64\PalServer-Win64-Test.exe'
         subprocess.Popen([caminho_executavel], creationflags=subprocess.CREATE_NO_WINDOW)
         await interaction.response.send_message('**O server foi iniciado!**\n> IP: `` \n> Nome da rede: `` \n> Senha: `` ')
        except Exception as e:
         await interaction.response.send_message('Não foi possível iniciar o server:(', ephemeral=True)
     else:
        interaction.response.send_message('Rapaiz tu vai tomar ban', ephemeral=True)

#stop_server
import os
async def stop_server(interaction):
   if interaction.user.guild_permissions.administrator:
     try:  
        processo = 'PalServer-Win64-Test.exe' 
        os.system(f'TASKKILL /F /IM {processo}')
        await interaction.response.send_message('*O server foi fechado*')
     except Exception as e: 
        await interaction.response.send_message('Não possível fechar o server :(', ephemeral=True)
   else: 
      await interaction.response.send_message('MAS RAPA OIA O BAN', ephemeral=True)    

#clear
from discord import app_commands
import asyncio
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
         
#restart_server
from valve.rcon import RCON, RCONCommunicationError
async def restart_server():
   try:
      ip = ''
      server_port = 0000
      rcon_senha = ''

      processo = 'PalServer-Win64-Test.exe' 
      caminho_executavel = 'C:\Games\Palworld.Early.Access\steamcmd\steamapps\common\PalServer\Pal\Binaries\Win64\PalServer-Win64-Test.exe'
      

      mensagem = 'O_servidor_sera_reiniciado_em_5_minutos!Salve_Seus_Pertences'
      mensagem_ascii = mensagem.encode('ascii', 'replace').decode('ascii')

      with RCON((ip, server_port), rcon_senha) as rcon:
         try:
            await rcon(f'broadcast {mensagem_ascii}')
         except RCONCommunicationError:
            print
  
      print(f'ResetServer 5 min')
      await asyncio.sleep(300)
      os.system(f'TASKKILL /F /IM {processo}')
      await asyncio.sleep(10)
      subprocess.Popen([caminho_executavel], creationflags=subprocess.CREATE_NO_WINDOW)
   except Exception as e:
      print(f'Erro ao reiniciar o servidor: {e}')
      

#msg
async def send_message(interaction,
                        mensagem: app_commands.Range[str, 0, 50]):
   if interaction.user.guild_permissions.administrator:
    try:
     with RCON((ip, server_port), rcon_senha) as rcon:
      mensagem_ascii = mensagem.encode('ascii', 'replace').decode('ascii')
      await rcon(f'broadcast {mensagem_ascii}')
    except:
       print(f'A menssagem {mensagem} foi enviada para o servidor')
   else:
      await interaction.response.send_message('Sem adm otaro', ephemeral=True)