#Bot qui gère le débat
import sys
import discord
import asyncio
import datetime
import time
TOKEN = 'NTAyNTUzNzA1MDY1ODczNDA4.DqpnPA.f3DCUouC_-qt4B-zb-rC7nq1q5A'
IDSALON = 502560765341859841

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
async def objectif_atteint(temps, objectif):
    # Sleep for one hour
    await asyncio.sleep(temps)
    await client.send_message(channel, "Alors ? L'objectif **"+objectif+"** a t'il été atteint ? :innocent: si oui, et :no_mouth: si non")
    get_reaction_users


@client.event
async def on_message(message):
    print(message.content)
    msg = message.content.split()
    if msg[0] == "!remindme" or msg[0]+msg[1] == "!remindme" :
        objectif = ""
        if msg[0]+msg[1] == "!remindme" :
            objectif = somme(msg[2:-1])
        else :
            objectif = somme(msg[1:-1])
        temps = msg[-1]
        t = datetime.datetime.now() #En heures
        delai = 0
        if temps[-1].upper() == "H" :
            t+=datetime.timedelta(hours = int(temps[:-1]))
            delai = int(temps[:-1])*3600
        if temps[-1].upper() == "D" :
            t+=datetime.timedelta(days = int(temps[:-1]))
            delai = int(temps[:-1])*3600*24
        t = str(t.day)+"/"+str(t.month)+" à "+str(t.hour)+"H"
        await client.send_message(message.channel, "C'est noté ! Objectif '**"+objectif+"**' à faire avant le "+t)
        
        #Cette partie est executée une fois l'objectif atteint ou non
        await asyncio.sleep(delai)
        await client.send_message(channel, "Alors " + message.author.mention + " ? L'objectif **"+objectif+"** a t'il été atteint ? :innocent:")        
        def check(msg):
            return "OUI" in msg.content.upper() or "YEP" in msg.content.upper()or "NON" in msg.content.upper()
        message = await client.wait_for_message(author=message.author, check=check)
        await client.send_message(channel, "Reçu")
        if "OUI" in message.content.upper() or "YEP" in message.content.upper() :
            await client.send_message(channel, "Nice :)")
        if "NON" in message.content.upper() :
            await client.send_message(channel, "Deg :(")
            

@client.event
async def on_ready():
    pass

client.run(TOKEN)
