import discord 
from discord.ext import commands 


# Config
BOT_TOKEN = "Token"
counting_channel = 1131193551032684606 # The ID of the channel to be counted in
wrong_emoji = "❌"
correct_emoji = "✅"
correct_100_emoji = "🔥" # Will be used after 100 is reached



bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
count = 1
user = 0



@bot.event
async def on_message(message):
    global count,user
    if message.channel.id != counting_channel or message.author.id == bot.user.id:
        return
    if message.author.id == user:
        if count > 1:
            count = 1
            await message.add_reaction(wrong_emoji)
            embed = discord.embeds.Embed(color=0xE74C3C, title="Wrong user!", description=f"You cannot count twice in a row! Count reset to 1!")
            await message.reply(embed=embed)
            user = 0
            return
        
    user = message.author.id  

    if str(message.content) != str(count):
        if count > 1:
            count = 1
            await message.add_reaction(wrong_emoji)
            embed = discord.embeds.Embed(color=0xE74C3C, title="Wrong Number!", description=f"<@{message.author.id}> got the count wrong! Count reset to 1!")
            await message.reply(embed=embed)
    else:
        if count >= 100:
            await message.add_reaction(correct_100_emoji)
        else:
            await message.add_reaction(correct_emoji)
        count += 1


bot.run(BOT_TOKEN)
