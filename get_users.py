import pandas as pd
import random


user_db = {"users": [], "weeb": [], "untouchable": [], "homeless": [], "impovrished": [], "lower-mid": [], "mid": [], "upper-mid": [], "rich": [], "one_perc": [], "bezos": [], "leader_fw": [], 
 			"money": [], "business_owner": [], "business_name": []}


def create_db(members_list):
	for i in range(len(members_list)):
		user_db["users"].append(int(members_list[i]))
		user_db["weeb"].append(False)
		user_db["untouchable"].append(False)
		user_db["homeless"].append(False)
		user_db["impovrished"].append(False)
		user_db["lower-mid"].append(False)
		user_db["mid"].append(False)
		user_db["upper-mid"].append(False)
		user_db["rich"].append(False)
		user_db["one_perc"].append(False)
		user_db["bezos"].append(False)
		user_db["leader_fw"].append(False)
		user_db["money"].append(0)
		user_db["business_owner"].append(False)
		user_db["business_name"].append("na")
	
		user_df = pd.DataFrame(user_db, columns=["users", "weeb", "untouchable", "homeless", "impovrished", "lower-mid", "mid", "upper-mid", "rich", "one_perc", "bezos", "leader_fw", "money", "business_owner", "business_name"])

		user_df.to_csv("E:/PythonScripts/bizbot-master/bizbot-master/dataMain.csv")


