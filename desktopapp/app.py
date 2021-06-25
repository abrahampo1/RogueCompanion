# SCRIPT BY ABRAHAMPO1 FOR ROGUECOMPANION
# https://github.com/abrahampo1/RogueCompanion
#
# ACTUALLY WORKING ON SKILL OVERLAYS AND IS DISABLED TO PREVENT FAKE VIRUS FLAGS


from asyncio.windows_events import NULL
import eel
from urllib.request import urlopen
import os
import requests
import time
import threading
import json
import socket
import sys
import subprocess
import logging
#from win32gui import GetWindowText, GetForegroundWindow
#from datetime import datetime
#from pynput.mouse import Listener
#import keyboard


global currentskill
currentskill = ""
logging.basicConfig(filename='std.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
version = 1.53
global windowopen #Set a variable to know when close the program on lose webhook
url_web = "https://rogue.cpsoftware.es"

# class Keylogger:
#     def __init__(self, interval, report_method="email"):
#         self.interval = interval
#         self.report_method = report_method
#         self.log = ""
#         self.start_dt = datetime.now()
#         self.end_dt = datetime.now()

#     def start(self):
#         self.start_dt = datetime.now()
#         keyboard.on_release(callback=self.callback)
#         self.report()
#         keyboard.wait()

#     def report(self):
#         if self.log:
#             self.end_dt = datetime.now()
#             if self.report_method == "file":
#                 self.report_to_file()
#             self.start_dt = datetime.now()
#         self.log = ""
#         timer = Timer(interval=self.interval, function=self.report)
#         timer.daemon = True
#         timer.start()

#     def report_to_file(self):
#         url_base = url_web + "/api.php"
#         url = url_base                                          #Connect to CPCloudService and send analitics data (the current window of the user to check bugs on skill overlay)
#         myobj = {
#             'api': data["api"],
#             'window' : GetWindowText(GetForegroundWindow())
#         }
#         x = requests.post(url, data=myobj)

#     def callback(self, event):                                  #Check what skill are being used and save the skill for receive a click
#         name = event.name
#         global currentskill
#         if name == "1":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "2":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "3":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "4":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "5":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "6":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "7":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "8":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "9":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "0":
#             print("Skill " + name)
#             if currentskill == name:
#                 currentskill = ""
#             else:
#                 currentskill = name
#         if name == "re pag":                                    #re pag is the kill button of the program
#             os.system("C:\Windows\System32/taskkill /F /IM Python.exe")
#             os.system("C:\Windows\System32/taskkill /F /IM RogueCompanion.exe")
#         self.log += name
# def mouseevent():
#     def on_click(x, y, button, pressed):
#         global currentskill
#         if pressed:
#             if GetWindowText(GetForegroundWindow()) == "Roblox":
#                 if(format(button) == "Button.left"):
#                     if(currentskill != ""):
#                         logging.info('CLICK! ({0}, {1}) con {2}'.format(x, y, button)+" en el Roblox con la skill " + currentskill + " seleccionada!")
#                         useskill(currentskill)                 #Use the skill selected
#             else:
#                 currentskill = ""

#     with Listener( on_click=on_click) as listener:
#         listener.join()


def buildapi():  # Get an API on CPCLoudService to verify the instance
    logger.info("Building the API conection...")
    url_base = url_web + "/api.php"
    url = url_base
    ip = requests.get('https://api.ipify.org').text
    print(ip)
    myobj = {
        'ip': ip,  # The program send PUBLIC ip address for verification purposes
        'getapi': '',
        # Hostname refeers to computer NAME (desktop-12345)
        'hostname': socket.gethostname()
    }
    x = requests.post(url, data=myobj)
    apikey = x.text  # The API key
    print(x.text)
    data = []
    data = {"version": version, "api": apikey}
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    return data  # Return JSON formatted text


def validarapi(api):
    logger.info("starting...")
    url_base = url_web + "/api.php"
    url = url_base
    myobj = {
        'validar': api,  # Verify the API, if can't build a new one
    }
    x = requests.post(url, data=myobj)
    if x.text == "OK":
        logger.info("STARTED!")
        return True
    else:
        return False


try:
    jsonurl = 'https://raw.githubusercontent.com/abrahampo1/RogueCompanion/master/version.json'
    response = requests.get(jsonurl)
    version_json = response.json()

    print(version_json["version"])
    if version_json["version"] > version:  # Detect new version and run updater.exe
        path = format(
            "START "+os.path.realpath(os.path.dirname(sys.argv[0])) + "/updater.exe")
        subprocess.run(path, shell=True)
        try:
            raise SystemExit
        except:  # if the program cant close, just force close Python
            os.system("C:\Windows\System32/taskkill /F /IM Python.exe")
    try:
        f = open("data.txt")
        data = json.load(f)
        if validarapi(data["api"]) == False:
            logger.info("I cant start, trying again...")
            data = buildapi()
    except:
        # if the program dont detect savedata file, build one
        data = buildapi()
except:
    print("FALLO AL ACTUALIZARSE")


def conectar():
    while True:
        try:
            url_base = url_web + "/api.php"
            url = url_base+"?data=1"
            myobj = {
                'api': data["api"],
            }
            # verify program property (verify that api key is used on the same computer, if not, close all)
            x = requests.post(url, data=myobj)
            if(x.text == "1"):
                url = url_base+"?on=1"
                x = requests.post(url)
                krbx()

            time.sleep(0.5)
        except:
            print("Connection API error")
            break




def useskill(skill):
    eel.skills(skill)


@eel.expose
def get_mana_bar():
    print("mana")


@eel.expose
def closemana():
    subprocess.run(
        'C:\Windows\System32/taskkill /F /IM manaoverlay.exe', shell=True)


@eel.expose
def krbx():
    subprocess.run(
        "C:\Windows\System32/taskkill /F /IM RobloxPlayerBeta.exe", shell=True)


@eel.expose
def set_mana_bar(src, w="200", h="600", px="10", py="10", op="100"):
    print("mana")
    if os.path.isfile("manaoverlay.exe"):
        logger.info("manaoverlay exists...")

        try:
            subprocess.run(
                'C:\Windows\System32/taskkill /F /IM manaoverlay.exe', shell=True)
        except:
            logger.info("opening manaoverlay...")
        path = format(os.path.realpath(os.path.dirname(
            sys.argv[0]))) + "\manaoverlay.exe "+w+" "+h+" "+px+" "+py+" "+src+" "+op
        subprocess.run("START "+path, shell=True)
    else:
        print("Faltan Archivos. Reinstala el programa.")


@eel.expose
def set_skill_overlay(src, w="200", h="600", px="10", py="10", op="100", r="255", g="255", b="255", config="false", close="false", timeout="0", skill="Lighting Elbow"):
    print("skilloverlay")
    if os.path.isfile("skilloverlay.exe"):
        logger.info("skilloverlay exists...")
    else:
        print("SkillOverlay Doesnt exists")
    url_base = url_web + "/api.php"
    url = url_base
    myobj = {
        'api': data["api"],
        'skill': skill,
        'timeout': timeout
    }
    x = requests.post(url, data=myobj)
    global currentskill
    currentskill = ""
    if(close == "true"):
        subprocess.run(
            'C:\Windows\System32/taskkill /F /IM skilloverlay.exe', shell=True)
    path = format(os.path.realpath(os.path.dirname(
        sys.argv[0]))) + "\skilloverlay.exe "+w+" "+h+" "+px+" "+py+" "+src+" "+op+" "+r+" "+g+" "+b+" "+config
    #path = os.path.realpath(os.path.dirname(sys.argv[0])) + "\skilloverlay.exe 200 600 100 100 120 100"
    subprocess.run('START "" ' + path, shell=True)
    print(path)


@eel.expose
def loadalt(alt, job, userjoin=""):
    path = os.path.realpath(os.path.dirname(
        sys.argv[0])) + '/rbxaccmanager/"RBX Alt Manager.exe" '+alt+" "+job+" "+userjoin
    subprocess.run('START ' + path, shell=True)
    print("Started: "+path)


@eel.expose
def ver():
    eel.ver(version)


@eel.expose
def refreshaltdata():
    load()

@eel.expose
def load():
    global windowopen
    windowopen = 1
    print("loaded")
    ver()
    try:
        url_base = url_web + "/api.php"
        url = url_base
        f = open("AccountData.json")
        jsontext = f.read()
        eel.altdatajson(jsontext)
        usernames = ""
        for username in jsontext:
            usernames = usernames + ";" + username["Username"]  #SAVE ONLY USERNAMES
        
        myobj = {
            'api': data["api"],
            'accounts': usernames, #SAVE ONLY USERNAMES ON CPCLOUDSERVICES FOR EASIER BACKUP ON THE FUTURE
        }
        x = requests.post(url, data=myobj)
        print(x.text)
    except:
        print("I cant open alt data")


b = threading.Thread(name='background', target=conectar)
b.start()  # Starting new thread with background data managment
# skillogger = Keylogger(interval=10, report_method="file")-
# k = threading.Thread(name='keyboard', target=skillogger.start)            #Disabled Due a multiple Bugs
# k.start()
# m = threading.Thread(name='mouse', target=mouseevent)
# m.start()


def close_callback(route, websockets):  # Kill the instances when program close
    if not websockets:
        global windowopen
        windowopen = 0
        i = 0
        print("closed")
        while i != 5:
            eel.sleep(1)
            i = i+1
            if windowopen == 1:
                break
        if windowopen == 0:
            print("OK CLOSING")
            subprocess.run(
                'C:\Windows\System32/taskkill /F /IM manaoverlay.exe', shell=True)
            subprocess.run(
                "C:\Windows\System32/taskkill /F /IM Python.exe", shell=True)
            subprocess.run(
                "C:\Windows\System32/taskkill /F /IM RogueCompanion.exe", shell=True)

eel.init('web')
eel.start('index.html', port=8575, close_callback=close_callback)
