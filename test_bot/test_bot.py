# Access Token
TOKEN = ''

# ID
ID_guild = ''

# Import Libralies
import discord
from discord import Intents, Client, Interaction, Game, Object
from discord import guild
from discord.app_commands import CommandTree

# Create Objects
intents = Intents.default()
client = Client(intents=intents)
tree = CommandTree(client)
guild=Object(id=ID_guild)

intents.message_content = True

@client.event
async def on_ready():
    #await tree.sync()   # コマンドを同期
    await tree.sync(guild=guild)   # コマンドを同期
    await client.change_presence(activity=Game(name="Activated"))    # ステータス表示

    # 起動したらターミナルにログイン通知が表示される  
    print(f"Logged in: {client.user.name} [ID:{client.user.id}]")    # Bot Name, [Bot ID]
    print(f"discord.py Version: {discord.__version__}")     # discord.py Version
    print("------")
    
@tree.command(name='hello', description='挨拶する（返信のみ）')     # /hello
async def hello(interaction: Interaction):
    await interaction.response.send_message('Hello!')

@tree.command(name='greet', description='挨拶する（送信者にメンションする）')    # /greet
async def greet(interaction: Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} , Hi!') # コマンド送信者にメンション

# Bot起動, Discordサーバーへ接続
client.run(TOKEN)
