#!/usr/bin/env python
# -*- coding: utf-8 -*-


import discord
from discord.ext import commands
import requests
import asyncio


        # seta o prefixo dos comandos #
bot = commands.Bot(command_prefix='!')


        ######################################
        ######################################
                        # qnd o bot inicia #

@bot.event
async def on_ready():
    print('-----------------------------')
    print("Discord " + discord.__version__)
    print('Bot Iniciado!')
    print('Name: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('-----------------------------')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(pass_context=True)
async def gerarpin(ctx):
                if not ctx.message.channel.is_private:
                            r = requests.get("http://detestadocc.000webhostapp.com/NovoPin.php", verify=False)
                            resposta = r.text
                            await bot.say('Aqui está seu PIN, {} : {}'.format(ctx.message.author.mention, resposta))
bot.run(NTAyNTYxMDgxMTUyMjQxNjY2.DqpuPw._xOiAh1HqgKGJ097niDqILQsUYQ)
