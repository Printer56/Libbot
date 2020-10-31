import discord
import os
import random

from discord.embeds import Embed
from discord.member import Member
from discord.guild import Guild

# Constant for the Discord UID
UID = 0

class MyClient(discord.Client):
    enable = False

    async def on_ready(self) -> None:
        """
        Confirms login
        """
        print("We have logged in as", self.user)

    async def on_message(self, message) -> None:
        """
        Returns a message easy
        """
        # only sends a message if the command user isnt the bot itself
        channel = message.channel
        if message.author == self.user:
            return
        elif message.author.id == UID:
            tokens = message.content.split(' ')
            if message.content.startswith("$"):
                # temporary override when nobody is around to guinea pig for me and i have to test myself
                if message.content == "$override":
                    await message.channel.send("Overriden. Torture mode enabled.")
                    self.enable = True
                elif message.content == "$doverride":
                    await message.channel.send("Overriden. Torture mode disabled.")
                    self.enable = False
                await message.channel.send("I don't listen to you lol")
            else:
                if self.enable == True:
                    num = random.randint(1, 2)
                    if num == 1:
                        await message.channel.send("K.")
                    else:
                        await message.channel.send(":neutral_face:")
            if random.randint(1, 15) == 15 and self.enable == True:
                await message.channel.send("Deleting message loser")
                await message.delete()
        
        elif message.content.startswith("$"):
            tokens: List[str] = message.content[1:].split(' ')
            if self.enable is False:
                if tokens[0] == "enable":
                    await message.channel.send("Torture Mode enabled. Get ready Miles.")
                    self.enable = True
                elif tokens[0] == 'help':
                    await option(message.channel)
                elif tokens[0] == 'status':
                    await message.channel.send("I'm up and running, Torture Mode disabled.")
                else:
                    await message.channel.send("Torture Mode is disabled. Type $enable to turn it on, or type $help.")
            else:
                if tokens[0] == 'help':
                        await option(message.channel)
                elif tokens[0] == 'hello':
                    await message.channel.send("Hello!")
                elif tokens[0] == "disable":
                    await message.channel.send("Disabling Torture Mode.")
                    self.enable = False
                elif tokens[0] == 'status':
                    await message.channel.send("I'm up and running, and ready to torture!")
                elif tokens[0] == 'nickname':
                    user = await channel.guild.fetch_member(UID)
                    await nick_change(user, channel.guild)
                    await message.channel.send("Nickname changed successfully!")
                else:
                    await message.channel.send("Invalid command. Check your spelling or type $help for a list of options")

client = MyClient()

async def option(channel) -> None:
    embed_var = Embed(
        title="Help!",
        description="Torture methods:",
        color=0xf76902
    )
    embed_var.add_field(
        name="$status",
        value="Confirms that I'm up and running, and displays the status of Torture Mode.",
        inline=False
    )
    embed_var.add_field(
        name="$enable",
        value="Enables Torture Mode.",
        inline=False
    )
    embed_var.add_field(
        name="$disable",
        value="Disables Torture Mode.",
        inline=False
    )
    embed_var.add_field(
        name="$hello",
        value="Echos hello! (Torture Mode required)",
        inline=False
    )
    embed_var.add_field(
        name="$nickname",
        value="Changes the nickname of the victim wink wink. (Torture Mode required)",
        inline=False
    )
    await channel.send(embed=embed_var)

async def nick_change(user, guild):
    """
    Randomly changes the nickname of the victim when called.
    """
    nick_list = []
    num = random.randint(0, len(nick_list) - 1)
    return await user.edit(nick=nick_list[num])
    

client.run(os.getenv('LIBBOT_API_KEY', ''))