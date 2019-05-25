import setuptools
import time, sys
from discoIPC import ipc
from infi.systray import SysTrayIcon
import webbrowser
import sys
from os import system, name
import ctypes

def say_hello(systray):
    webbrowser.open('https://discord.gg/hYnAQVg')
    webbrowser.open('http://chillbar.org')
menu_options = (("Chillbar", None, say_hello),)
systray = SysTrayIcon("chillbar.ico", "Chillbar Rich Presence", menu_options)

def quit():
    sys.exit()

def clear(): 
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

activity = {
    'state': 'Best server on Discord',
    'details': '➥ Click to join!',
    'assets': {
        'large_image': 'large',
        'large_text': 'Join now!',
        'small_image': 'small',
        'small_text': 'uwu',
    },
    'timestamps': {}
}

timeElapsed = int(time.time())

client = ipc.DiscordIPC('485406206278631425')
client.connect()



system("title "+"Chillbar Rich Presence")
time.sleep(1)
clear()
print("\n\n\n\n\n\n\n\n\n════════════════════════════════════════════════════════════")
print("╔═╗┬ ┬┬┬  ┬  ┌┐ ┌─┐┬─┐  ┬─┐┬┌─┐┬ ┬  ┌─┐┬─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┌─┐")
print("║  ├─┤││  │  ├┴┐├─┤├┬┘  ├┬┘││  ├─┤  ├─┘├┬┘├┤ └─┐├┤ ││││  ├┤ ")
print("╚═╝┴ ┴┴┴─┘┴─┘└─┘┴ ┴┴└─  ┴└─┴└─┘┴ ┴  ┴  ┴└─└─┘└─┘└─┘┘└┘└─┘└─┘")
print("════════════════════════════════════════════════════════════")
time.sleep(0.8)
print("Website: http://chillbar.org")
time.sleep(0.8)
print("Invite: https://discord.gg/hYnAQVg")
time.sleep(4)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def set_activity():
    activity['timestamps']['start'] = timeElapsed
    return activity

try:
    while True:
        systray.start()
        client.update_activity(set_activity())
        time.sleep(15) # Send data every second seconds
        systray.stop()

except KeyboardInterrupt:
    print('===========================\n')
    print('Quit Chillbar rich presence\n')
    print('===========================\n')
    client.disconnect()
    sys.exit()