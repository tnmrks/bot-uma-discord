import discord
import os
import random
from discord.ext import commands

# --- DAFTAR UMA MUSUME ---
# Anda bisa menambah atau mengurangi daftar ini kapan saja.
list_uma = [
    "Special Week", "Maruzensky", "Oguri Cap", "Gold Ship", "Vodka",
    "Daiwa Scarlet", "Air Groove", "Mayano Top Gun", "Mejiro Ryan",
    "Agnes Tachyon", "Winning Ticket", "Sakura Bakushin O", "Super Creek",
    "Haru Urara", "Matikanefukukitaru", "Nice Nature", "King Halo",
    "Grass Wonder", "El Condor Pasa", "Seiun Sky"
]

# --- PENGATURAN DASAR BOT ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot telah login sebagai {bot.user}')
    print('Bot siap menerima perintah!')
    print('---------------------------')

# --- PERINTAH UNTUK MEMILIH UMA ---
@bot.command(name='latih', help='Memilih 3 Uma Musume secara acak untuk dilatih.')
async def pilih_latihan(ctx):
    # Cek apakah ada cukup Uma di dalam daftar utama
    if len(list_uma) < 3:
        await ctx.send("Maaf, daftar Uma Musume kurang dari tiga untuk bisa diacak.")
        return

    # Langsung ambil 3 nama acak dari daftar lengkap setiap saat
    uma_terpilih = random.sample(list_uma, 3)

    # Membuat pesan Embed (tidak ada yang berubah di sini)
    embed = discord.Embed(
        title="🐎 Pilihan Latihan Hari Ini 🐎",
        description="Berikut adalah 3 Uma yang terpilih untuk sesi latihanmu!",
        color=discord.Color.blue()
    )
    embed.add_field(name="Uma 1", value=f"**{uma_terpilih[0]}**", inline=False)
    embed.add_field(name="Uma 2", value=f"**{uma_terpilih[1]}**", inline=False)
    embed.add_field(name="Uma 3", value=f"**{uma_terpilih[2]}**", inline=False)
    embed.set_footer(text=f"Semangat melatih, {ctx.author.name}!")

    await ctx.send(embed=embed)

# --- MENJALANKAN BOT ---
bot_token = os.getenv('DISCORD_TOKEN')
bot.run(bot_token)