import os
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from discord.ext import commands

# Simple web server to keep host alive
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Dev Alert Bot is alive!")

def run_web_server():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "alert dev call" in message.content.lower():
        await message.channel.send("⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️
⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️
⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️
⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️
@Dev team ")

    await bot.process_commands(message)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
