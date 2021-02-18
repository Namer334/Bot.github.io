import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

filtered_words = ["fuck", "shit", "Fuck", "Shit"]

@client.event
async def on_ready():
	print("bot is online")

@client.event
async def on_message(msg):
	for word in filtered_words:
		if word in msg.content:
			await msg.delete()

	await client.process_commands(msg)

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	await member.send("you have been kicked from The Official Gaming Server, Because:"+ reason)
	await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await member.send(member.name + " has been banned from The Official Gaming Server, Because:"+ reason)
	await member.ban(reason=reason)

@client.command(aliases=['w'])
@commands.has_permissions(kick_members = True)
async def whois(ctx, member : discord.Member):
	embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.green())
	embed.add_field(name = "ID", value = member.id , inline = True )
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(aliases=['e1'])
async def emoji1(ctx):
	await ctx.send("<:pog:779466274933702716>")

@client.command(aliases=['e2'])
async def emoji2(ctx):
	await ctx.send("<a:Vibin:780213534633099264>")


client.run("Nzk5NjczMjQ1NTk4MzUxMzkx.YAG_vg.eDh3WggCi7-3waMDhbmR0uBcHWE")
