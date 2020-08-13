"""
Developed by Laureline. 04.07.2020 13:17
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

with open("warningseng.json", "r") as eng_file:
    enggrund = json.load(eng_file)

with open("muteeng.json", "r") as mute_file:
    mutegrund = json.load(mute_file)



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
    print ('logged in')


@client.event
async def on_message(message):
    guild = client.get_guild(581785829857296395)
    modrolle = discord.utils.get(guild.roles, id = 717391327947653220)
    mutedrole = discord.utils.get(guild.roles, id = 720720582689423372)
    logging = client.get_channel(728901938586058823)

#mute
    if message.content.startswith('!mute') and modrolle in message.author.roles and not message.content.startswith('!mute eng'):

        messageauthor = message.author
        try:
            mention = message.content.split(' ')[1]
        except:
            await message.channel.send('Um einen User zu muten, musst du !mute [user] [reason] schreiben.')
            return
        tester = False

        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User zu muten, musst du !mute [user] [reason] schreiben.')
            return
        if tester:
            try:
                autor = mention.replace('<', '')
                autor2 = autor.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                autor5 = int(autor4)
                author_id = str(autor5)
            except:
                await message.channel.send('Um einen User zu muten, musst du !mute [user] [reason] schreiben.')
                return
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

            mutedembed = discord.Embed(title = 'Mute', description = f"Der User <@{str(autor5)}> wurde verwarnt und gemutet.", colour = 0x151515)
            mutedembed.add_field(name = f"Grund:", value = f"{str(reason)}", inline = True)
            mutedembed.add_field(name = f"\n Moderator:", value = f"{messageauthor.mention} \n", inline = True)
            mutedembed.set_footer(text = uhrzeit)
            await logging.send(embed = mutedembed)

            muted = discord.Embed(title = "Achtung!", description = f"Du wurdest von der Server-Moderation für 24 Stunden gemutet. \nGrund: {str(reason)} \n \nBei Fragen zu dieser Maßnahme wende dich bitte an {str(skygamer.mention)}", colour = 0x151515)
            await member.send(embed = muted)
            time = 86400
            await asyncio.sleep(time)
            await member.remove_roles(mutedrole)

#warn
    if message.content.startswith('!warn') and modrolle in message.author.roles and not message.content.startswith('!warn eng'):
        try:
            mention = message.content.split(' ')[1]
        except:
            await message.channel.send('Um einen User zu warnen, musst du !warn [user] [reason] schreiben.')
            return
        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User zu warnen, musst du !warn [user] [reason] schreiben.')
        if tester:
            try:
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
            except:
                await message.channel.send('Um einen User zu warnen, musst du !warn [user] [reason] schreiben.')
                return

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

            warnungenembeded = discord.Embed(title = 'Warn', description = f'Der User {str(mention)} wurde verwarnt.', colour = 0x151515)
            warnungenembeded.add_field(name = "Grund: ", value = f"{str(reason)}", inline=True)
            warnungenembeded.add_field(name = "Moderator: ", value = f"{message.author.mention} \n", inline=True)
            warnungenembeded.set_footer(text = '\n' + uhrzeit)
            dmembed = discord.Embed(title = "Achtung!", description = f'Du wurdest von der Server-Moderation verwarnt. \nGrund: {str(reason)} \n \nBei Fragen zu dieser Maßnahme wende dich bitte an {str(skygamer.mention)}', colour = 0x151515)
            await dmmer.send(embed = dmembed)
            
            await logging.send(embed = warnungenembeded)


#MUTE ENGLISCH CMMD
    if message.content.startswith('!mute eng') and modrolle in message.author.roles:
        try:
            mention = message.content.split('eng ')[1]
        except:
            await message.channel.send('Um einen User auf englisch zu muten, müssen Ssie !mute eng [user] [reason] schreiben.')
            return
        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User auf englisch zu muten, müssen Sie !mute eng [user] [reason] schreiben.')
        if tester:
            mention = message.content.split('eng ')[1]
            try:
                reason = mention.split('> ') [1]
                mention = mention.split('> ') [0]
                mention = mention.replace('!', '')
                autor1 = mention.replace('<', '')
                autor2 = autor1.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                author_id = autor4
            except:
                await message.channel.send('Um einen User auf englisch zu muten, müssen Sie !mute eng [user] [reason] schreiben.')
                return
            member = guild.get_member(author_id)
            print('meine damen, meine herrn')
            print (member)
            print (author_id)
            global authorUser
            authorUser = author_id
            dmautor = int(autor4)
            guild = message.guild

            if author_id in warnings:
                currentValue = warnings[author_id]
                warnings[author_id] = currentValue + 1
            else:
                warnings[author_id] = 1

            with open(("warningcount.json"), "w") as warning_count_file:
                warning_count_file.write(json.dumps(warnings))

            if author_id in datum:
                day = datum[author_id]
                datum[author_id] = day + tag + '--> \n '
            else:
                datum[author_id] = tag + '--> \n '

            with open(("datum.json"), "w") as datum_file:
                datum_file.write(json.dumps(datum))

            skygamer = guild.get_member(605731050823614504)
            dmmer = guild.get_member(dmautor)
            warnungenembeded = discord.Embed(title = 'Mute', description = f'Der User {str(mention)}> wurde verwarnt und gemutet.', colour = 0x151515)
            warnungenembeded.add_field(name = "Grund: ", value = f"{str(reason)}", inline=True)
            warnungenembeded.add_field(name = "Moderator: ", value = f"{message.author.mention} \n", inline=True)
            warnungenembeded.set_footer(text = '\n' + uhrzeit)
            dmembed = discord.Embed(title = "Attention!", description = f'You have been muted for 24 hours by the server moderator.  \nReason: {str(reason)} \n \nIf you have any questions about this measure, please contact {str(skygamer.mention)}', colour = 0x151515)
            await dmmer.send(embed = dmembed)
            print ('ja lul ey')

            await logging.send(embed = warnungenembeded)
            await message.channel.send ('Bitte wiederholen sie den Grund auf deutsch:')
            author = message.author.id
            print ('feucht und fettig')
            
            if author in mutegrund:
                currentValue = mutegrund[author]
                mutegrund[author] = currentValue + 1
            else:
                mutegrund[author] = 1

            with open(("muteeng.json"), "w") as mute_file:
                mute_file.write(json.dumps(mutegrund))
            await dmmer.add_roles(mutedrole)
            time = 86400
            await asyncio.sleep(time)
            await member.remove_roles(mutedrole)


    if message.author.id in mutegrund:
        if  mutegrund[message.author.id] >= 1 and not '!warn' in message.content or '!mute' in message.content:
            reason = message.content
            author = authorUser
            erfolgsembed = discord.Embed(description=f'Der User wurde verwarnt und gemutet.', colour=0x151515)
            print ('abermals erfolgreich')
            await message.channel.send(embed = erfolgsembed)
            author_id = message.author.id
            if author_id in mutegrund:
                currentValue = mutegrund[author_id]
                mutegrund[author_id] = currentValue - 1
            else:
                mutegrund[author_id] = 0
            
            with open(("muteeng.json"), "w") as mute_file:
                mute_file.write(json.dumps(mutegrund))

            if author in reasons:
                wieso = reasons[author]
                reasons[author] = wieso + reason + ' + __Mute__ '+' \n '

            else:
                reasons[author] =  reason + ' + __Mute__ '+ ' \n '

            with open(("reason.json"), "w") as reason_file:
                reason_file.write(json.dumps(reasons))


    if message.content.startswith('!warn eng') and modrolle in message.author.roles:
        try:
            mention = message.content.split('eng ')[1]
        except:
            await message.channel.send('Um einen User auf englisch zu warnen, müssen Sie !warn eng [user] [reason] schreiben.')
            return

        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einen User auf englisch zu warnen, müssen Sie !warn eng [user] [reason] schreiben.')
        if tester:
            try:
                mention = message.content.split('eng ')[1]
                reason = mention.split('> ') [1]
                mention = mention.split('> ') [0]
                mention = mention.replace('!', '')
                autor1 = mention.replace('<', '')
                autor2 = autor1.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                author_id = autor4
                authorUser = author_id
                dmautor = int(autor4)
                guild = message.guild
            except:
                await message.channel.send('Um einen User auf englisch zu warnen, müssen Sie !warn eng [user] [reason] schreiben.')
                return
            if author_id in warnings:
                currentValue = warnings[author_id]
                warnings[author_id] = currentValue + 1
            else:
                warnings[author_id] = 1

            with open(("warningcount.json"), "w") as warning_count_file:
                warning_count_file.write(json.dumps(warnings))

            if author_id in datum:
                day = datum[author_id]
                datum[author_id] = day + tag + '--> \n '
            else:
                datum[author_id] = tag + '--> \n '

            with open(("datum.json"), "w") as datum_file:
                datum_file.write(json.dumps(datum))

            skygamer = guild.get_member(605731050823614504)
            dmmer = guild.get_member(dmautor)
            warnungenembeded = discord.Embed(title = 'Warn', description = f'Der User {str(mention)}> wurde verwarnt.', colour = 0x151515)
            warnungenembeded.add_field(name = "Grund: ", value = f"{str(reason)}", inline=True)
            warnungenembeded.add_field(name = "Moderator: ", value = f"{message.author.mention} \n", inline=True)
            warnungenembeded.set_footer(text = '\n' + uhrzeit)
            dmembed = discord.Embed(title = "Attention!", description = f'You have been warned by the server moderator.  \nReason: {str(reason)} \n \nIf you have any questions about this measure, please contact {str(skygamer.mention)}', colour = 0x151515)
            await dmmer.send(embed = dmembed)
            print ('ja lul ey')

            await logging.send(embed = warnungenembeded)
            await message.channel.send ('Bitte wiederholen sie den Grund auf deutsch:')
            author = message.author.id
            print ('feucht und fettig')
            
            if author in enggrund:
                currentValue = enggrund[author]
                enggrund[author] = currentValue + 1
            else:
                enggrund[author] = 1

            with open(("warningseng.json"), "w") as eng_file:
                eng_file.write(json.dumps(enggrund))

    if message.author.id in enggrund:
        if  enggrund[message.author.id] >= 1 and not '!warn' in message.content:
            reason = message.content
            author = authorUser
            erfolgsembed = discord.Embed(description=f'Der User wurde verwarnt.', colour=0x151515)
            print ('abermals erfolgreich')
            await message.channel.send(embed = erfolgsembed)
            author_id = message.author.id
            if author_id in enggrund:
                currentValue = enggrund[author_id]
                enggrund[author_id] = currentValue - 1
            else:
                enggrund[author_id] = 0
            
            with open(("warningseng.json"), "w") as eng_file:
                eng_file.write(json.dumps(enggrund))

            if author in reasons:
                wieso = reasons[author]
                reasons[author] = wieso + reason + ' \n '
            else:
                reasons[author] =  reason + ' \n '

            with open(("reason.json"), "w") as reason_file:
                reason_file.write(json.dumps(reasons))

#CLEAR WARNINGS CMMD

    if message.content.startswith('!clear warns') and modrolle in message.author.roles:

        try:
            mention = message.content.split('warns ')[1]
        except:
            await message.channel.send('Um die warnings eines users zu clearen müssen Sie !clear warns [user] schreiben.')
            return
        tester = True
        if tester:
            try:
                mention = message.content.split('warns ')[1]
                mention = mention.split('> ') [0]
                mention = mention.replace('!', '')
                autor1 = mention.replace('<', '')
                autor2 = autor1.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                author_id = autor4
                dmautor = int(autor4)
                guild = message.guild
            except:
                await message.channel.send('Um die warnings eines users zu clearen müssen Sie !clear warns [user] schreiben.')
                return
            
            if author_id in warnings:
                warningsremove = warnings[author_id]
                print (warningsremove)
                warnings[author_id] = warningsremove - warningsremove
            else:
                await message.channel.send('Dieser User wurde momentan weder gemutet noch gewarnt.')
                return
            with open(("warningcount.json"), "w") as warning_count_file:
                warning_count_file.write(json.dumps(warnings))


            if author_id in datum:
                datumremove = datum[author_id]
                print (datumremove)
                datum[author_id] = datumremove.replace(datumremove, '')
                datum[author_id]
            else:
                await message.channel.send('Dieser User wurde momentan weder gemutet noch gewarnt.')
                return
            with open(("datum.json"), "w") as datum_file:
                datum_file.write(json.dumps(datum))


            if author_id in reasons:
                reasonsremove = reasons[author_id]
                print (reasonsremove)
                reasons[author_id] = reasonsremove.replace(reasonsremove, '')
                reasons[author_id]
            else:
                await message.channel.send('Dieser User wurde momentan weder gemutet noch gewarnt.')
                return
            with open(("reason.json"), "w") as reasons_file:
                reasons_file.write(json.dumps(reasons))
            warnclearembed = discord.Embed(description=f'Die Warnings des Users <@{str(author_id)}> wurden erfolgreich entfernt.', colour=0x6E6E6E)
            await message.channel.send(embed=warnclearembed)


#INFO COMMAND
    if message.content.startswith('!info') and modrolle in message.autor.roles:
        
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
        embed = discord.Embed(title='{}'.format(member),description='{}'.format(member.mention),color= 0x2EFEF7)
        embed.add_field(name='Server beigetreten:', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),inline=True)
        embed.add_field(name='Account erstellt:', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),inline=True)
        embed.add_field(name='Nickname:', value =member.nick, inline = True)
        if datumzeit == '':
            datumzeit = 'None'
        if gründe == '':
            gründe = 'None'
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


    if message.content.startswith('!unmute') and modrolle in message.autor.roles:
        try:
            mention = message.content.split(' ')[1]
            tester = True
        except:
            await message.channel.send('Um einen User zu entmuten musst du !unmute [user] schreiben.')
            return
        tester = False

        if tester:
            mention = message.content.split(' ')[1]
            try:
                mention = mention.split('> ') [0]
                mention = mention.replace('!', '')
                autor1 = mention.replace('<', '')
                autor2 = autor1.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                author_id = autor4
            except:
                await message.channel.send('Um einen User zu entmuten musst du !unmute [user] schreiben.')
                return
            member = guild.get_member(author_id)
            await member.remove_roles(mutedrole)
            unmutembed = discord.Embed(description=f'Der User <@{author_id}> wurde erfolgreich entmutet.', colour=0x6E6E6E)
            await message.channel.send(embed=unmutembed)
            
            
    if message.content.startswith('!dm') and modrolle in message.author.roles:
        

        try:
            mention = message.content.split(' ')[1]
        except:
            await message.channel.send('Um einem User eine DM zu schreiben musst du !dm [user] [nachricht] schreiben.')
            return
        tester = False
        try:
            reason = message.content.split('> ') [1]
            tester = True
        except:
            await message.channel.send('Um einem User eine DM zu schreiben musst du !dm [user] [nachricht] schreiben.')
        if tester:
            mention = message.content.split(' ')[1]
            try:
                mention = mention.split('> ') [0]
                mention = mention.replace('!', '')
                autor1 = mention.replace('<', '')
                autor2 = autor1.replace('>', '')
                autor3 = autor2.replace('!', '')
                autor4 = autor3.replace('@', '')
                author_id = int(autor4)
                
            except:
                await message.channel.send('Um einem User eine DM zu schreiben musst du !dm [user] [nachricht] schreiben.')
    
                return
                
            member = guild.get_member(author_id)
            
            dmnachricht = discord.Embed(description=reason, colour=0x23DF0F)
            await member.send(embed = dmnachricht)
            unmutembed = discord.Embed(description=f'Dem User <@{author_id}> wurde erfolgreich eine DM geschickt.', colur = 0x6E6E6E)
            await message.channel.send(embed=unmutembed)


@client.event
async def on_message_delete(message):
    logging = client.get_channel(728901938586058823)
    author = message.author.id
    channel = message.channel

    if message.author.id == 728588597984362537:
        return

    else:
        farbton2 = 0x6E6E6E
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
        farbton3 = 0x6E6E6E
        editiert = discord.Embed(description =  '**Nachricht Editiert**', colour = farbton3)
        editiert.add_field(name='__User:__', value=f'        <@{str(before.author.id)}>', inline = True)
        editiert.add_field(name = '__Channel:__', value=f'       <#{str(before.channel.id)}>', inline = True)
        editiert.add_field(name = '__Vorher:__', value=f'       {str(before.content)}', inline = False)
        editiert.add_field(name = '__Nachher:__', value =f'       {str(after.content)}', inline=False )
        await logging.send(embed=editiert)


@client.event
async def on_member_join(member):
    member1 = member
    member = str(member1).split('#')[0]
    farbton4 = 0x04B404
    logging = client.get_channel(728901938586058823)
    joinembed = discord.Embed(description = f':DE_ArrowJoin: **{member}** ist dem Server beigetreten. \n{member1.mention}', colour = farbton4)
    await logging.send(embed=joinembed)
    
    welcome = discord.Embed(title=''':flag_de: *__German:__*
Herzlich Willkommen,''', description = '''
    am offiziellen Discord-Server von __Z-Software__ und __Aerosoft__ rund um den **__Autobahn-Polizei Simulator 3__**.
    Bitte mach dich zum Beginn mit unseren Regeln (<#681876950809444371>) vertraut.
    Außerdem solltest du einen Blick in <#723611371660378173> werfen.
    Dort findest du alle interessanten Informationen, Fragen und Antworten, sowie wissenswerte Details rund um den 3. Teil der Polizei-Simulation.
    Somit  werden dir bereits am Anfang viele deiner Fragen beantwortet.
    Nun aber genug der Worte und viel Spaß am Server!
    Dein Entwicklungs-Team
''', colour = 0xFF0000 )
    englischembed = discord.Embed(title=''':flag_gb: *__English:__*
Welcome,''', description='''
    at the official discord server of __Z-Software__ and __Aerosoft__ around the **__Autobahn-Police Simulator 3__**.
    Please make yourself familiar with our rules (<#681876950809444371>).
    You should also have a look at <#723611371660378173>.
    There you will find all interesting information, questions and answers, as well as interesting details about the 3rd part of the police simulation.
    Thus, many of your questions will be answered right at the beginning.
    But now enough words and enjoy the server!
    Your development team
    ''', colour=0x0404B4)
    try:
        await member.send(embed=welcome)
        await member.send(embed=englischembed)
    except:
        pass
        
        

@client.event
async def on_member_remove(member):
    member = member
    member = str(member).split('#')[0]
    farbton3 = 0xDF0101
    logging = client.get_channel(728901938586058823)
    leaveembed = discord.Embed(description = f' **{member}** hat den Server verlassen.', colour = farbton3)
    await logging.send(embed = leaveembed)
    goodbye = discord.Embed(title='', description='', colour=farbton3)
    try:
        await member.send(embed=goodbye)
    except:
        pass






client.run(TOKEN)
