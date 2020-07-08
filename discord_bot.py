"""
Developed by Laureline. 04.07.2020 13:17

Hosting by Cardistymo. 08.07.2020 17:30
"""



import discord
import random
import json
import asyncio
import time
import datetime



with open("warningcount.json", "r") as warning_count_file:
    warnings = json.load(warning_count_file)

with open("reason.json", "r") as reason_file:
    reasons = json.load(reason_file)

with open("datum.json", "r") as datum_file:
    datum = json.load(datum_file)



tag = time.strftime(" %d.%m.%Y")
uhrzeit = time.strftime("%d.%m.%Y • %H:%M:%S Uhr")


client = discord.Client()
TOKEN = 'NzI4NTg4NTk3OTg0MzYyNTM3.Xv8lCA.iXZayKYrZEenAA8OYLcgiPnTPN8'
Farbe = 0x1E7AEB
footer = 'Autobahnpolizei ist zur Stelle!'

Farbe1 = 0x27E821
Farbe2 = 0x2608E5
Farbe3 = 0xE7806B
Farbe5 = 0xE6DE06
Farbe6 = 0x20DDBA
Farbe7 = 0x14B1EB
Farbe8 = 0xEF16E3
Farbe9 = 0x4B8220
Farbe10 = 0xE1800A
Farbe11 = 0xF6020A
Farbe12 = 0xFDF367





@client.event
async def on_ready():
    print ('eingeloggt')




@client.event
async def on_message(message):
    guild = client.get_guild(581785829857296395)
    modrolle = discord.utils.get(guild.roles, id = 717391327947653220)
    mutedrole = discord.utils.get(guild.roles, id = 720720582689423372)
    logging = client.get_channel(728901938586058823)
     

    farbton = random.choice([Farbe, Farbe1, Farbe2, Farbe3, Farbe3, Farbe5, Farbe6, Farbe7, Farbe8, Farbe9, Farbe10, Farbe11, Farbe12])
    if message.content.startswith('!info'):
        
        with open(("warningcount.json"), "w") as warning_count_file:
            warning_count_file.write(json.dumps(warnings))

        with open(("datum.json"), "w") as datum_file:
            datum_file.write(json.dumps(datum))

        with open(("reason.json"), "w") as reason_file:
            reason_file.write(json.dumps(reasons))

        mention = message.content.split(' ')[1]
        autor = mention.replace('<', '')
        autor2 = autor.replace('>', '')
        autor3 = autor2.replace('!', '')
        autor4 = autor3.replace('@', '')
        wert = autor4
        #wert = message.content.replace("!show ", "")
        print(wert)
        guild = message.guild
        member = guild.get_member(int(wert))
        if not wert in warnings:
            warnungen = 0
        else:
            warnungen = warnings[wert]

        if not wert in datum:
            datumzeit = None
        else:
            datumzeit = datum[wert]

        if not wert in reasons:
            gründe = None
        else:
            gründe = reasons[wert]
        embed = discord.Embed(title='{}'.format(member),description='{}'.format(member.mention),color= farbton)
        embed.add_field(name='Server beigetreten:', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),inline=True)
        embed.add_field(name='Account erstellt:', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),inline=True)
        embed.add_field(name='Nickname:', value =member.nick, inline = True)
        #embed.add_field(name='Name', value=member.name, inline = True)
        embed.add_field(name=f'Warnings:', value=f'{str(datumzeit)}', inline = True)
        embed.add_field(name=f'({str(warnungen)} Stück)', value=f'{str(gründe)}', inline = True)
        rollen = ''
        for role in member.roles:
            if not role.is_default():
                rollen += '{} \r\n'.format(role.mention)
        if rollen:
            embed.add_field(name='Rollen:', value=rollen, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=uhrzeit)
        await message.channel.send(embed=embed)

    if message.content.startswith('!mute') and modrolle in message.author.roles:

        messageauthor = message.author
        mention = message.content.split(' ')[1]
        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User zu muten, musst du !mute [user] [reason] schreiben.')

        if tester:
            autor = mention.replace('<', '')
            autor2 = autor.replace('>', '')
            autor3 = autor2.replace('!', '')
            autor4 = autor3.replace('@', '')
            autor5 = int(autor4)
            author_id = str(autor5)

            guild = message.guild
            member = guild.get_member(autor5)
            await member.add_roles(mutedrole)
            print ('succeded')


            if author_id in warnings:
                currentValue = warnings[author_id]
                warnings[author_id] = currentValue + 1
            else:
                warnings[author_id] = 1

            with open(("warningcount.json"), "w") as warning_count_file:
                warning_count_file.write(json.dumps(warnings))

            if author_id in reasons:
                wieso = reasons[author_id]
                reasons[author_id] = wieso + reason + ' + __Mute__ \n '
            else:
                reasons[author_id] =  reason + ' + __Mute__ \n '

            with open(("reason.json"), "w") as reason_file:
                reason_file.write(json.dumps(reasons))

            if author_id in datum:
                day = datum[author_id]
                datum[author_id] = day + tag + '    --> \n '
            else:
                datum[author_id] = tag + '    --> \n '

            with open(("datum.json"), "w") as datum_file:
                datum_file.write(json.dumps(datum))

            skygamer = guild.get_member(605731050823614504)
            mutedembed = discord.Embed(title = 'Mute', description = f"Der User <@{str(autor5)}> wurde verwarnt und gemutet.", colour = farbton)
            mutedembed.add_field(name = f"Grund:", value = f"{str(reason)}", inline = True)
            mutedembed.add_field(name = f"\n Moderator:", value = f"{messageauthor.mention} \n", inline = True)
            mutedembed.set_footer(text = uhrzeit)
            await logging.send(embed = mutedembed)
            muted = discord.Embed(title = "Achtung", description = f"Du wurdest von der Server-Moderation für 24 Stunden gemutet. \nGrund: {str(reason)} \n \nBei Fragen zu dieser Maßnahme wende dich bitte an {str(skygamer.mention)}", colour = farbton)
            await member.send(embed = muted)
            time = 86400
            await asyncio.sleep(time)
            await member.remove_roles(mutedrole)

    if message.content.startswith('!warn') and modrolle in message.author.roles:
        
        mention = message.content.split(' ')[1]
        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User zu warnen, musst du !warn [user] [reason] schreiben.')
        if tester:
            mention = message.content.split(' ')[1]
            reason = message.content.split('> ') [1]
            autor1 = mention.replace('<', '')
            autor2 = autor1.replace('>', '')
            autor3 = autor2.replace('!', '')
            autor4 = autor3.replace('@', '')
            print (autor4)
            author_id = autor4
            dmautor = int(autor4)
            guild = message.guild

            if author_id in warnings:
                currentValue = warnings[author_id]
                warnings[author_id] = currentValue + 1
            else:
                warnings[author_id] = 1

            with open(("warningcount.json"), "w") as warning_count_file:
                warning_count_file.write(json.dumps(warnings))

            if author_id in reasons:
                wieso = reasons[author_id]
                reasons[author_id] = wieso + reason + ' \n '
            else:
                reasons[author_id] =  reason + ' \n '

            with open(("reason.json"), "w") as reason_file:
                reason_file.write(json.dumps(reasons))

            if author_id in datum:
                day = datum[author_id]
                datum[author_id] = day + tag + '--> \n '
            else:
                datum[author_id] = tag + '--> \n '

            with open(("datum.json"), "w") as datum_file:
                datum_file.write(json.dumps(datum))

            skygamer = guild.get_member(605731050823614504)
            dmmer = guild.get_member(dmautor)
            warnungenembeded = discord.Embed(title = 'Warn', description = f'Der User {str(mention)} wurde verwarnt', colour = farbton)
            warnungenembeded.add_field(name = "Grund: ", value = f"{str(reason)}", inline=True)
            warnungenembeded.add_field(name = "Moderator: ", value = f"{message.author.mention} \n", inline=True)
            warnungenembeded.set_footer(text = '\n' + uhrzeit)
            dmembed = discord.Embed(title = "Achtung!", description = f'Du wurdest von der Server-Moderation verwarnt. \nGrund: {str(reason)} \n \nBei Fragen zu dieser Maßnahme wende dich bitte an {str(skygamer.mention)}', colour = farbton)
            await dmmer.send(embed = dmembed)
            
            await logging.send(embed = warnungenembeded)

    if message.content.startswith('!clear') and modrolle in message.author.roles:
        amount = message.content.split(' ') [1]
        await message.channel.purge(limit=int(amount))
        clearembed = discord.Embed(title = 'Einsatz', description = f'Es wurden {str(amount)} Nachrichten in {str(message.channel.mention)} von {str(message.author.mention)} gelöscht.', colour = farbton)
        await logging.send(embed = clearembed)

        
    if message.content == 'unmute':
        guild = message.guild
        lukas = guild.get_member(615549256119353345)
        await lukas.remove_roles(muted)


@client.event
async def on_message_delete(message):
    logging = client.get_channel(728901938586058823)
    author = message.author.id
    channel = message.channel

    if message.author.id == 728588597984362537:
        return
    else:
        farbton2 = random.choice([Farbe, Farbe1, Farbe2, Farbe3, Farbe3, Farbe5, Farbe6, Farbe7, Farbe8, Farbe9, Farbe10, Farbe11, Farbe12])
        gelöscht = discord.Embed(description =  '**Nachricht Gelöscht**', colour  = farbton2)
        gelöscht.add_field(name='__User:__', value=f'<@{str(author)}>', inline = True)
        gelöscht.add_field(name = '__Channel:__', value=f'<#{str(channel.id)}>', inline = True)
        gelöscht.add_field(name = '__Nachricht:__', value =f'       {str(message.content)}', inline=False )
        await logging.send(embed=gelöscht)
    


#wenn nachrichten editiert werden
@client.event
async def on_message_edit(before, after):
    if  'discord.gg' in after.content:
        #hier könnte deine werbung stehen...
        await after.delete()

    logging = client.get_channel(728901938586058823)
    if before.author.id == 728588597984362537:
        return
    if before.content != after.content:
        farbton3 = random.choice([Farbe, Farbe1, Farbe2, Farbe3, Farbe3, Farbe5, Farbe6, Farbe7, Farbe8, Farbe9, Farbe10, Farbe11, Farbe12])
        editiert = discord.Embed(description =  '**Nachricht Editiert**', colour = farbton3)
        editiert.add_field(name='__User:__', value=f'        <@{str(before.author.id)}>', inline = True)
        editiert.add_field(name = '__Channel:__', value=f'       <#{str(before.channel.id)}>', inline = True)
        editiert.add_field(name = '__Vorher:__', value=f'       {str(before.content)}', inline = False)
        editiert.add_field(name = '__Nachher:__', value =f'       {str(after.content)}', inline=False )
        await logging.send(embed=editiert)

client.run(TOKEN)
