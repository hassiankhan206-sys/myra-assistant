# Myra Assistant - Made by hassiankhan206
print("Hello, I am Myra!")

def myra_reply(msg):
    msg = msg.lower()
    if "salam" in msg or "hello" in msg:
        return "Walaikum Salam! Main Myra hun :)"
    elif "name" in msg:
        return "Mera naam Myra hai!"
    else:
        return f"Aapne kaha: {msg} - Main aapki help karungi!"

# Test run
user_msg = input("Aap kuch likho: ")
print(myra_reply(user_msg))
