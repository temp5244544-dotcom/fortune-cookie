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

# Change this to your actual Dev Team Role ID!
DEV_ROLE_ID = "YOUR_ROLE_ID_HERE"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "alert dev call" in message.content.lower():
        alert_text = (
            "# ⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️\n"
            "# ⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️\n"
            "# ⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️\n"
            "# ⚠️⚠️🚨🚨 ALERT DEV CALL 🚨🚨⚠️⚠️\n"
            f"<@&{1500143470919159990}>"
        )
        await message.channel.send(alert_text)

    await bot.process_commands(message)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
