import discord
from discord.ext import commands
import os

# กำหนด intents สำหรับบอท (ตั้งค่าให้บอทสามารถอ่านข้อมูลที่จำเป็นได้)
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งานการอ่านเนื้อหาข้อความ

# สร้าง instance ของบอท
bot = commands.Bot(command_prefix='!', intents=intents)

# เมื่อบอทออนไลน์ จะพิมพ์ข้อความนี้ในคอนโซล
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# สร้างคำสั่งง่ายๆ เมื่อผู้ใช้พิมพ์ "!ping"
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# เริ่มต้นบอทโดยใช้ TOKEN
TOKEN = os.getenv('DISCORD_TOKEN')  # เก็บ TOKEN ไว้ใน environment variable เพื่อความปลอดภัย

server_on()
bot.run(TOKEN)
