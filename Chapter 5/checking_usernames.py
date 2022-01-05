current_users=["Homer", "Marge", "Bart", "Lisa", "Maggie"]
new_users=["bart", "LISA", "Bob", "Clancy"]

current_users_lower=[]
for user in current_users:
	current_users_lower.append(user.lower())

for user in new_users:
	if(user.lower() in current_users_lower):
		print(f"Sorry {user}, you have to choose a new username.")
	else:
		print(f"{user}, your username is available.")