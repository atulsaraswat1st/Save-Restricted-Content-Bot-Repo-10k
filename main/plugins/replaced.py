from pyrogram import Client, filters
from pyromod import listen
from main.plugins import mongo

@Client.on_message(filters.command("replaced"))
async def replaced_word(_,message):
 lol = await _.ask(message.chat.id, text="send me a replaced word")
 replaced_txt = lol.text
 await mongo.add_replaced(message.from_user.id, replaced_txt)
 await message.reply_text("succeffully added your replaced word.")
 

@Client.on_message(filters.command("delete"))
async def delete_word(_,message):
 lol = await _.ask(message.chat.id, text="send me a delete word")
 del_txt = lol.text
 await mongo.add_replaced(message.from_user.id, del_txt)
 await message.reply_text("succeffully added your delete word.")
 
