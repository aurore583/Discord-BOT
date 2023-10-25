import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 642493596653584426  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx, message):
    await ctx.send(message.author)

@bot.command()
async def d6(ctx):
    number= random.randint(1,6)
    await ctx.send(number)

@bot.event
async def on_message(message):
    #Check that the message meet requirements
    if message.content == "Salut tout le monde":
        await message.channel.send(f"Bienvenue à {message.author.mention} sur le serveur discord ! N'oublie pas de faire !regles") 

### Administration

@bot.command()
async def admin(ctx, member : discord.Member):
    # Does the role Admin already exist?
    role_admin = discord.utils.get(ctx.guild.role, name='Admin')
    if not role_admin : 
        #Create the role admin
        await ctx.guild.create_role(name='Admin', permissions=discord.Permissions.all(), mentionable=True)
    member.add_role("Admin")

@bot.command()
async def ban(ctx, member : discord.Member, reason : None):
    funny_catchphrase = [ "Time to take the exit stage left, my friend!", "We're about to hit the 'eject' button on this one.", "This is your cue for a dramatic exit, à la reality TV.", "Consider this your free subscription to 'Outta Here' magazine", "You've officially been 'disinvited' to the party." ]
    if member == None or member == ctx.message.author:
        #Check that the ban is valid
        await ctx.channel.send("You cannot ban yourself")
    if reason == None:
        #Check that the ban have a valid reason and if not choose a random reason in the list
        number= random.randint(0, len(funny_catchphrase))
        reason = funny_catchphrase[number]
    await member.send(f"You have been banned from {ctx.guild.name} for {reason}")
    #Precise in the channel that the member is banned
    await ctx.channel.send(f"{member} is banned!")
    

token = "MTE2Njc4NDMwNDA5Mzg3MjE2OQ.GVap05.lIhfrmFgPKGEkcOZ_ufgGM2l_wMXmgV4T_HgzY"
bot.run(token)  # Starts the bot