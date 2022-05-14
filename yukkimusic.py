#!/bin/python
import os 

#Credits code by Rendy
#telegram @FFmpegNotInstalled
os.system("clear")
os.system("sleep 2")

print ("\033[1;32mAUTHOR :  \033[1;34mDeleveoper By Rendy")
print ("\033[1;33mTelegram : @FFmpegNotInstalled")
print ("\033[1;34mINSTALL YUKKI MUSIC BOT")
print
print ("INSTALL YUKKI..........")
os.system("sleep 10")
os.system("sudo pip3 install -U pip")
os.system("sudo apt-get install python3-pip ffmpeg -y")
os.system("curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash - && sudo apt-get install nodejs -y && npm i -g npm")
os.system("sleep 10")
os.system("git clone https://github.com/TeamYukki/YukkiMusicBot && cd YukkiMusicBot")
os.system("pip3 install -r requirements.txt")
os.system("cp sample.env .env")
os.system("vi .env")