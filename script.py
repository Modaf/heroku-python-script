#Bot qui gère le débat
import sys
import discord
import asyncio
import json
import datetime
TOKEN = 'NTAyNTUzNzA1MDY1ODczNDA4.DqpnPA.f3DCUouC_-qt4B-zb-rC7nq1q5A'
IDSALON = 502554506081599490

client = discord.Client()
channel = discord.Object(id=IDSALON)

def begin_with(str, chaine) :
    if str[:len(chaine)] == chaine :
        return True
    return False
def somme(liste) :
    res = ""
    for k in liste :
        res += k+" "
    return res[:-1]

@client.event
async def on_message(message):
    msg = message.content.split()
    if msg[0] == "!remindme" or msg[0]+msg[1] == "!remindme" :
        objectif = ""
        if msg[0]+msg[1] == "!remindme" :
            objectif = somme(msg[2:-1])
        else :
            objectif = somme(msg[1:-1])
        temps = msg[-1]
        t = datetime.datetime.now() #En heures
        if temps[-1].upper() == "H" :
            t+=datetime.timedelta(hours = int(temps[:-1]))
        if temps[-1].upper() == "D" :
            t+=datetime.timedelta(days = int(temps[:-1]))
        t = str(t.day)+"/"+str(t.month)+" à "+str(t.hour)+"H"
        await client.send_message(channel, "Objectif '**"+objectif+"**' à faire avant le "+t)

    
@client.event
async def on_ready():
    await client.send_message(channel, "Je suis la")

client.run(TOKEN)





