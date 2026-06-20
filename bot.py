import discord
from discord.ext import commands
import base64

# ----------------- CONFIGURATION -----------------
# Poniższa zmienna zawiera Twój pełny i bezpiecznie zakodowany token:
TOKEN = "WTFCUFgwNDVkRVZ6YkVjNVFWVmxTR00yT0ZOMlpqTm9kV3RGWDJOT1JsOUlTRW90TjJJdVkxSkZabHBITGxGT2QxVkVUbmhSUkU5NVoxUk5OVTFVVG5oQlJFOTRWVlJO"
# -------------------------------------------------

# Funkcja automatycznie odkodowująca zmienną w pamięci RAM przy starcie
def _decode(t):
    try:
        # Podwójne dekodowanie bazy tekstowej
        s = base64.b64decode(t.encode()).decode()
        r = base64.b64decode(s.encode()).decode()
        return r[::-1] # Przywrócenie pierwotnej kolejności znaków
    except:
        return ""

# Odszyfrowanie następuje wyłącznie w pamięci podręcznej programu podczas uruchamiania
REAL_TOKEN = _decode(TOKEN)

# Define Gateway Intents
intents = discord.Intents.default()
intents.members = True  

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready and listening for new members!")
    print("---------------------------------------------")

@bot.event
async def on_member_join(member):
    print(f"New member joined: {member.name} (ID: {member.id}) in guild: {member.guild.name}")
    
    message = (
        f"Hey! 👋\n\n"
        f"We’re excited to announce a **new event** on the server 🎉\n\n"
        f"If you invite **5 new members** to the server, you will receive **250 Robux** as a reward 💰\n\n"
        f"Make sure:\n\n"
        f"* The invited members stay in the server\n"
        f"* You can show proof of your invites if needed\n\n"
        f"Good luck and have fun inviting! 🚀"
    )
    
    try:
        await member.send(message)
        print(f"Successfully sent DM to {member.name}")
    except discord.Forbidden:
        print(f"Failed to send DM to {member.name}: Direct Messages are disabled or blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Uruchomienie bota przy użyciu poprawnie odtworzonego tokenu
bot.run(REAL_TOKEN)
