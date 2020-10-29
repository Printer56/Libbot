import discord
import os

from discord.embeds import Embed

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
        if message.author == self.user:
            return
        # if message.author.id == 372064836848189440:
        #     await message.channel.send("K.")
        
        if message.content.startswith("$"):
            tokens: List[str] = message.content[1:].split(' ')
            if self.enable is False:
                if tokens[0] == "enable":
                    await message.channel.send("Torture mode enabled. Get ready Miles.")
                    self.enable = True
                elif tokens[0] == 'help':
                        await option(message.channel)
                else:
                    await message.channel.send("Torture mode is disabled. Type $enable to turn it on, or type $help.")
            else:
                if tokens[0] == 'help':
                        await option(message.channel)
                elif tokens[0] == 'hello':
                    await message.channel.send("Hello!")
                elif tokens[0] == "disable":
                    await message.channel.send("Disabling torture mode.")
                    self.enable = False
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
        name="$hello",
        value="Echos hello!",
        inline=False
    )
    embed_var.add_field(
        name="$enable",
        value="Enables torture mode.",
        inline=False
    )
    embed_var.add_field(
        name="$disable",
        value="Disables torture mode.",
        inline=False
    )
    await channel.send(embed=embed_var)

client.run(os.getenv('LIBBOT_API_KEY', ''))