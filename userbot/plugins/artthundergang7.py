"""Plugin made by Thundergang for ThunderUserbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot.utils import admin_cmd

RR = ("───▄▄▄\n"
"─▄▀░▄░▀▄\n"
"─█░█▄▀░█\n"
"─█░▀▄▄▀█▄█▄▀\n"
"▄▄█▄▄▄▄███▀\n")
TT = ("─────────█▄██▄█\n"
"█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n"
"███┼█████▐████▌█████┼███\n"
"█████████▐████▌█████████\n")
YY = ("─▀▀▌───────▐▀▀\n"
"─▄▀░◌░░░░░░░▀▄\n"
"▐░░◌░▄▀██▄█░░░▌\n"
"▐░░░▀████▀▄░░░▌\n"
"═▀▄▄▄▄▄▄▄▄▄▄▄▀═\n")
UU = ("░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"██▀▀▀██▀▀▀▀▀▀██▀▀▀██\n"
"█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█\n"
"█▒▒▒▒▒█▒████▒█▒▒▒▒▒█\n"
"██▄▄▄██▄▄▄▄▄▄██▄▄▄██\n")
II = ("▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░\n"
"▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░\n"
"▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░\n"
"▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░\n"
"░░░░▄▄███▄▄░░░░░█████░\n")

@borg.on(admin_cmd(pattern=r"snail"))
async def nandysnail(snail):
    await snail.edit(RR)
@borg.on(admin_cmd(pattern=r"fort"))
async def nandyfort(fort):
    await fort.edit(TT)
@borg.on(admin_cmd(pattern=r"fish"))
async def nandyfish(fish):
    await fish.edit(YY)
@borg.on(admin_cmd(pattern=r"radio"))
async def nandyradio(radio):
    await radio.edit(UU)
@borg.on(admin_cmd(pattern=r"computer"))
async def nandycomputer(computer):
    await computer.edit(II)