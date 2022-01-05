messages=["hello", "how are you?", "bye"]
sent_messages=[]

def show_messages(messages):
	for message in messages:
		print(message)

def send_messages(messages, sent_messages):
	show_messages(messages)
	while messages:
		item=messages.pop()
		sent_messages.append(item)
	sent_messages.reverse()

send_messages(messages[:], sent_messages)

print("First list:")
show_messages(messages)
print("Second list:")
show_messages(sent_messages)