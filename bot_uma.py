import discord
import os
import random
import json
from datetime import date
from discord.ext import commands

# Nama file untuk menyimpan riwayat latihan
HISTORY_FILE = "training_history.json"

# --- DAFTAR UMA MUSUME ---
list_uma = [
    "Special Week", "Maruzensky", "Oguri Cap", "Gold Ship", "Vodka",
    "Daiwa Scarlet", "Air Groove", "Mayano Top Gun", "Mejiro Ryan",
    "Agnes Tachyon", "Winning Ticket", "Sakura Bakushin O", "Super Creek",
    "Haru Urara", "Matikanefukukitaru", "Nice Nature", "King Halo",
    "Grass Wonder", "El Condor Pasa", "Seiun Sky"
]

# --- FUNGSI UNTUK MEMBACA DAN MENYIMPAN RIWAYAT ---

def load_history():
    """Membaca file riwayat dan mengembalikan daftar Uma yang dilatih hari ini."""
    try:
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
            # Cek apakah tanggal di file sama dengan tanggal hari ini
            if history.get('date') == str(date.today()):
                return history.get('trained_umas', [])
    except FileNotFoundError:
        # Jika file tidak ada, berarti ini pertama kali dijalankan atau hari baru
        return []
    except json.JSONDecodeError:
        # Jika file rusak atau kosong, anggap saja sebagai hari baru
        return []
    # Jika tanggalnya sudah berbeda, kembalikan daftar kosong
    return []

def save_history(trained_umas):
    """Menyimpan daftar Uma yang baru dilatih ke file riwayat."""
    history = {
        'date': str(date.today()),
        'trained_umas': trained_umas
    }
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

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
@bot.command(name='latih', help='Memilih 3 Uma Musume secara acak untuk dilatih hari ini.')
async def pilih_latihan(ctx):
    # 1. Muat riwayat Uma yang sudah dilatih HARI INI
    trained_today = load_history()

    # 2. Buat daftar Uma yang tersedia (semua Uma KECUALI yang sudah dilatih hari ini)
    available_umas = [uma for uma in list_uma if uma not in trained_today]

    # 3. Cek apakah ada cukup Uma yang tersedia untuk dipilih
    if len(available_umas) < 3:
        await ctx.send("Maaf, tidak ada cukup Uma yang tersisa untuk dilatih hari ini!")
        return

    # 4. Ambil 3 nama acak dari daftar yang TERSEDIA
    uma_terpilih = random.sample(available_umas, 3)

    # 5. Gabungkan daftar lama dengan yang baru dan simpan
    new_trained_list = trained_today + uma_terpilih
    save_history(new_trained_list)

    # Membuat pesan Embed (sama seperti sebelumnya)
    embed = discord.Embed(
        title="🐎 Pilihan Latihan Hari Ini 🐎",
        description="Berikut adalah 3 Uma yang terpilih untuk sesi latihanmu hari ini!",
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