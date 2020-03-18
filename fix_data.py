import pandas as pd 
import numpy as np

counter = 0
df = pd.read_csv("~/python_projs/discordbot/databases/dataMain.csv")
money = pd.read_csv("~/python_projs/discordbot/databases/mtransfer.csv")

print(money)

print(len(df["users"]))
print(len(money["user"]))

for x in range(len(df["users"])):
	for i in range(len(money["user"])):
		print(str(df["users"][x]) + " " + str(money["user"][i]))		
		if str(df["users"][x]) == str(money["user"][i]):
			df["money"][x] = (money["val"][i])
			


print(df["money"])
print(counter)
df.to_csv("~/python_projs/discordbot/databases/dataMainFixed.csv")


