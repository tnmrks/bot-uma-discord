import discord
import os
import random
from discord.ext import commands

# --- DAFTAR UMA MUSUME ---
# Kamu bisa melengkapi daftar ini sebanyak yang kamu mau!
list_uma = [
    "Special Week", "Maruzensky", "Oguri Cap", "Gold Ship", "Vodka",
    "Daiwa Scarlet", "Air Groove", "Mayano Top Gun", "Mejiro Ryan",
    "Agnes Tachyon", "Winning Ticket", "Sakura Bakushin O", "Super Creek",
    "Haru Urara", "Matikanefukukitaru", "Nice Nature", "King Halo"
]

# --- PENGATURAN DASAR BOT ---

# Menentukan prefix (tanda seru) dan intent (izin) yang diperlukan bot
intents = discord.Intents.default()
intents.message_content = True  # Mengizinkan bot membaca konten pesan

# Membuat objek bot
bot = commands.Bot(command_prefix="!", intents=intents)

# --- EVENT KETIKA BOT SIAP ---
@bot.event
async def on_ready():
    print(f'Bot telah login sebagai {bot.user}')
    print('Bot siap menerima perintah!')
    print('---------------------------')

# --- PERINTAH UNTUK MEMILIH UMA ---
@bot.command(name='latih', help='Memilih 3 Uma Musume secara acak untuk dilatih hari ini.')
async def pilih_latihan(ctx):
    # Memastikan ada cukup Uma di dalam daftar
    if len(list_uma) < 3:
        await ctx.send("Maaf, daftar Uma Musume kurang dari tiga untuk bisa diacak.")
        return

    # Mengambil 3 nama secara acak dari list_uma tanpa ada yang sama
    uma_terpilih = random.sample(list_uma, 3)

    # Membuat pesan yang lebih cantik menggunakan Embed
    embed = discord.Embed(
        title="🐎 Pilihan Latihan Hari Ini 🐎",
        description="Berikut adalah 3 Uma yang terpilih untuk sesi latihanmu hari ini!",
        color=discord.Color.blue() # Kamu bisa ganti warnanya
    )

    # Menambahkan nama-nama Uma yang terpilih ke dalam embed
    embed.add_field(name="Uma 1", value=f"**{uma_terpilih[0]}**", inline=False)
    embed.add_field(name="Uma 2", value=f"**{uma_terpilih[1]}**", inline=False)
    embed.add_field(name="Uma 3", value=f"**{uma_terpilih[2]}**", inline=False)

    embed.set_footer(text=f"Semangat melatih, {ctx.author.name}!")

    # Mengirim pesan embed ke channel tempat perintah dipanggil
    await ctx.send(embed=embed)

# --- MENJALANKAN BOT ---
# Ganti 'TOKEN_BOT_KAMU_DISINI' dengan token bot yang sudah kamu dapatkan dari Developer Portal
bot_token = os.getenv('DISCORD_TOKEN')
bot.run(bot_token)