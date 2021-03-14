import discord, os, asyncio, data

bot = discord.Client()
channel = None
responses = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AA AB AC AD AE AF AG 2A'.split()

async def update():
    while True:
        sheet = data.get()
        
        changed = False
        while int(sheet[0][0]) > int(sheet[0][1]):
            row = int(sheet[0][1])
            changed = True
            for i in range(0, len(sheet[row]), 2):
                if sheet[row - 1][i] != sheet[row][i]:
                    await channel.send(f'**{sheet[row][i + 1]}** has bid **{sheet[row][i]}** on response **{responses[i // 2]}**!')
                    break
            sheet[0][1] = row + 1

        if changed:
            data.set(sheet[0][1])
        
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    global channel
    channel = bot.get_channel(int(os.getenv('CHANNEL')))
    bot.loop.create_task(update())

bot.run(os.getenv('TOKEN'))