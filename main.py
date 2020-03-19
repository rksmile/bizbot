import pandas as pd
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
from get_users import create_db

counter = 0
mem = []
try:
	volatile_df = pd.read_csv("E:/PythonScripts/bizbot-master/bizbot-master/dataMainFixed.csv")
except FileNotFoundError:
	print("Not set yet!")

def append_user(user_info, member):
	user_info["users"].append(int(member.id))
	user_info["weeb"].append(False)
	user_info["untouchable"].append(False)
	user_info["homeless"].append(False)
	user_info["impovrished"].append(False)
	user_info["lower-mid"].append(False)
	user_info["mid"].append(False)
	user_info["upper-mid"].append(False)
	user_info["rich"].append(False)
	user_info["one_perc"].append(False)
	user_info["bezos"].append(False)
	user_info["leader_fw"].append(False)
	user_info["money"].append(0)
	user_info["business_owner"].append(False)
	user_info["business_name"].append("na")

	volatile_df = volatile_df.append(user_info, ignore_index=True)


Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():	
	print("Running")


@client.event
async def on_member_join(member):
	new_user_dict = {{"users": [], "weeb": [], "untouchable": [], "homeless": [], "impovrished": [], "lower-mid": [], "mid": [], "upper-mid": [], "rich": [], "one_perc": [], "bezos": [], "leader_fw": [], "money": [], "business_owner": [], "business_name": []}}
	append_user(new_user_dict, member)



@client.listen()
async def on_message(message):
  	if message.content =="!members_get":
  		x = message.guild.members
  		for i in range(len(x)):
  			if "472944238972370955" not in x[i].roles:
  				mem.append(x[i].id)
  		create_db(mem)
  		await message.channel.send("Members updated")


@client.listen()
async def on_message(message):
	if message.content == "!import_database":
		volatile_df = pd.read_csv("E:/PythonScripts/bizbot-master/bizbot-master/dataMainFixed.csv")
		await message.channel.send("Data imported! All functions usable.")


@client.listen()
async def on_message(message):
    if message.content == "!money":
    	auth = str(message.author.id)
    	print(auth)
    	for x in range(len(volatile_df["users"])):
    		if auth == str(volatile_df["users"][x]):
    			await message.channel.send("$" + str(volatile_df["money"][x]))


@client.listen()
async def on_message(message):
	global counter
	if message.content[0] != "!":
		counter += 1
		auth = str(message.author.id)
		if counter == 5:
			counter = 0
			volatile_df.to_csv("E:/PythonScripts/bizbot-master/bizbot-master/dataMainFixed.csv")
		for x in range(len(volatile_df["users"])):
			if auth == str(volatile_df["users"][x]):
				volatile_df['money'][x] += random.randint(20, 40)


@client.listen()
async def on_message(message):
	if message.content == "!die":
		await client.logout()


client.run('your token')
