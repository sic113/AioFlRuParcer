import random

def user_agent():
	file=open("user-agents.txt","r")
	user_agent_val = []
	for x in file:
		user_agent_val.append(x)
	x = random.randint(0,999)
	user = user_agent_val[x]
	user = str(user)[:-2]
	return user

if __name__ == '__main__':
	user_agent()