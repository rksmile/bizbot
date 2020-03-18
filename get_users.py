import pandas as pd
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import pandas as pd 

#restructure entire

mem = []

volatile_df = pd.read_csv("~/python_projs/discordbot/databases/dataMainFixed.csv")

Client = discord.Client()
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():	
	print("Running")


# @client.listen()
# async def on_message(message):
# 	if message.content =="!members_update":
# 		x = message.guild.members
# 		for i in range(len(x)):
# 			if "472944238972370955" not in x[i].roles:
# 				mem.append(x[i].id)

# 		await message.channel.send("Members updated")


@client.listen()
async def on_message(message):
    if message.content == "!money":
    	auth = str(message.author.id)
    	print(auth)
    	for x in range(len(volatile_df["users"])):
    		if auth == str(volatile_df["users"][x]):
    			await message.channel.send("$" + volatile_df["money"][x])


client.run('token')

user_db = {"users": [], "weeb": [], "untouchable": [], "homeless": [], "impovrished": [], "lower-mid": [], "mid": [], "upper-mid": [], "rich": [], "one_perc": [], "bezos": [], "leader_fw": [], 
			"money": [], "business_owner": [], "business_name": []}



# for i in range(len(mem)):
# 	user_db["users"].append(int(mem[i]))
# 	user_db["weeb"].append(False)
# 	user_db["untouchable"].append(False)
# 	user_db["homeless"].append(False)
# 	user_db["impovrished"].append(False)
# 	user_db["lower-mid"].append(False)
# 	user_db["mid"].append(False)
# 	user_db["upper-mid"].append(False)
# 	user_db["rich"].append(False)
# 	user_db["one_perc"].append(False)
# 	user_db["bezos"].append(False)
# 	user_db["leader_fw"].append(False)
# 	user_db["money"].append(0)
# 	user_db["business_owner"].append(False)
# 	user_db["business_name"].append("na")


# user_df = pd.DataFrame(user_db, columns=["users", "weeb", "untouchable", "homeless", "impovrished", "lower-mid", "mid", "upper-mid", "rich", "one_perc", "bezos", "leader_fw", "money", "business_owner", "business_name"])

# user_df.to_csv("~/python_projs/discordbot/databases/dataMain.csv")

# print(len(mem))

