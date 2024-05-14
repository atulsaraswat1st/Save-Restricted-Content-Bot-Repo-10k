from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

MONGO_DB = ""

mongo = MongoCli(MONGO_DB)
db = mongo.captions
db = db.caption_db



async def re_caption(user_id, replaced_word):
    data = await check_premium(user_id)
    if data and data.get("_id"):
        await db.update_one({"_id": user_id}, {"$set": {"replaced_word": replaced_word}})
    else:
        await db.insert_one({"_id": user_id, "replaced_word": replaced_word})


async def del_caption(user_id, del_word):
    data = await check_premium(user_id)
    if data and data.get("_id"):
        await db.update_one({"_id": user_id}, {"$set": {"del_word": del_word}})
    else:
        await db.insert_one({"_id": user_id, "del_word": del_word})


async def check_premium(user_id):
    x = await db.find_one({"_id": user_id})
    return x

