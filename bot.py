import discord
from discord.ext import commands

# ----------------- CONFIGURATION -----------------
# Paste your Discord Bot Token inside the quotes below:
TOKEN = "MTUxODAxNTM5MTgyODQxNDUwNQ.GZfERc.b7-JHH_FNc_Ekuh3fvS86cHeUA9GlsEt9N_OPc"
# -------------------------------------------------

# Define Gateway Intents
# default() includes most intents, but we MUST explicitly enable 'members' to receive on_member_join events
intents = discord.Intents.default()
intents.members = True  # Required to detect when a new member joins

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")
    print("Bot is ready and listening for new members!")
    print("---------------------------------------------")

@bot.event
async def on_member_join(member):
    # This event is triggered when a new member joins any server the bot is in
    print(f"New member joined: {member.name} (ID: {member.id}) in guild: {member.guild.name}")
    
    # Message to send to the new member in DM
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
        # Send DM to the member
        await member.send(message)
        print(f"Successfully sent DM to {member.name}")
    except discord.Forbidden:
        # This error occurs if the user has direct messages disabled for server members or blocked the bot
        print(f"Failed to send DM to {member.name}: Direct Messages are disabled or blocked by the user.")
    except Exception as e:
        print(f"An error occurred while sending DM to {member.name}: {e}")

if __name__ == "__main__":
    if TOKEN == "YOUR_DISCORD_BOT_TOKEN_HERE" or not TOKEN:
        print("\n[!] Error: Please replace 'YOUR_DISCORD_BOT_TOKEN_HERE' on line 6 with your actual Discord Bot Token!")
    else:
        bot.run(TOKEN)
