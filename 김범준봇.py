import discord
import random
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong')

    if message.content.startswith("ㄴ프사"):
      
      embed = discord.Embed(title = f"{message.author}" + "님의 프사", color= 0x0000ff)
      embed.set_image(url=message.author.avatar_url)
      await message.channel.send(embed=embed)
    
    if message.content.startswith("ㄴ카피"):
         await message.channel.send(message.content[4:])

    if message.content == ("ㄴ서버"):
        embed = discord.Embed(color =0x0000ff )
        icon_= str(message.guild.icon_url)
        embed.add_field(name="서버이름",value=f"{(message.guild.name)}",inline=False)
       
        embed.add_field(name="서버생성시간",value=f"{message.guild.created_at.strftime('%Y-%m-%d %H/%M/%S')}")
     


        embed.add_field(name="서버멤버수",value=f"{message.guild.member_count}" + "명",inline=False)
        embed.set_thumbnail(url=icon_)
        await message.channel.send(embed=embed)

    if message.content == "ㄴ랜덤":
               await message.channel.send("1부터 100 까지수중 아무수나 부릅니다.")
               await asyncio.sleep(1)
               await message.channel.send(random.randint(1,100))
    
    if message.content.startswith("ㄴ핑"):
        embed = discord.Embed(title = ':ping_pong: 퐁!', description = str(client.latency*100) + 'ms', color = 0x00ff00)
        await message.channel.send(embed=embed)
    

client.run('ODYyMjk5ODgyNjg1NDY0NTc2.YOWVWA.uMnN7lRuBCTLlSs_vbRBizLrO4o')