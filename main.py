import os
import discord
import data_input
from replit import db
import random
from keep_alive import keep_alive

client = discord.Client()
token = os.environ['token']
keys = db.keys()

number_of_keys = len(keys)

cached_keys = []

def randomIndex():
  return random.randrange(1,number_of_keys+1)

def fill_cached_keys():
  for index in range(0,10):
    cached_keys.append(randomIndex())

def add_key():
  while(True):
    index = randomIndex()
    if(index not in cached_keys):
      cached_keys.append(index)
      break
  

@client.event
async def on_ready():
  fill_cached_keys()
  print('We have logged in as {0.user}'.format(client))
  # print(cached_keys)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('~question'):
    await message.channel.send(db[str(cached_keys[0])])  
    cached_keys.remove(cached_keys[0])
    add_key()
    # print(cached_keys)


keep_alive()
client.run(token)