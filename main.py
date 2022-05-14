from colorama import Fore
import ctypes, pyautogui, keyboard, os, time, random
from datetime import datetime

mainColor = Fore.BLUE

ascii_text = """
       ███╗░░██╗████████╗██████╗░██╗
       ████╗░██║╚══██╔══╝██╔══██╗██║
       ██╔██╗██║░░░██║░░░██║░░██║██║
       ██║╚████║░░░██║░░░██║░░██║██║
       ██║░╚███║░░░██║░░░██████╔╝██║
       ╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░╚═╝
"""

def sendCons(arg):
    print(f"\n       {Fore.WHITE}[{mainColor}Console{Fore.WHITE}] {arg}")

class Bot:
    def __init__(this):
        this.count = 0 # count for whatever it is you are doing

    def getPos(this): # get the position of the button
        sendCons("Move your mouse to the user settings icon, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.userSettings = pyautogui.position()
                break;
        time.sleep(0.5)
        sendCons("Move your mouse to the party mode selector, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.partyMode = pyautogui.position()
                break;
        time.sleep(0.5)
        sendCons("Move your mouse to the achievements selector, then press G")
        while True:
            if keyboard.is_pressed('G'):
                this.achBtn = pyautogui.position()
                break;
        time.sleep(0.5)

    
    def sendBot(this):
        pyautogui.moveTo(this.userSettings) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.5)
        pyautogui.moveTo(this.partyMode) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.3)
        pyautogui.moveTo(this.achBtn) # moves mouse to button
        pyautogui.click() # clicks button
        time.sleep(0.7)
        pyautogui.keyDown('esc')
        time.sleep(0.15)
        pyautogui.keyUp('esc')
        
        sendCons("Opened party mode")
        this.count += 1 # add to count
        this.updateConsole() # update console

    def updateConsole(this): # update the console with stats
        os.system('cls') # clear screen
        this.updateTitle() # update title
        print(mainColor + ascii_text) # print ascii art
        sendCons("Starting bot loop") # start the loop of your main task
        sendCons("Hold G to quit") # if user wants to quit press g
        sendCons(f"Opened {this.count} times") # print how many bots you sent
        now = time.time()
        elapsed = str(now - this.started_time).split(".")[0] # elapsed time
        sendCons(f"Elapsed time: {elapsed}s") # print how long you have been running

    def updateTitle(this):
        now = time.time()
        elapsed = str(now - this.started_time).split(".")[0] # elapsed time
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Bot | Opened: {this.count} times | Elapsed: {elapsed}s | Created by @professional-tdi on Github.")
    
    def main(this): # main function
        os.system('cls') # clear screen
        ctypes.windll.kernel32.SetConsoleTitleW("Bot | Created by @professional-tdi on Github.") # basic title with no info
        print(mainColor + ascii_text) # print ascii art
        this.getPos() # get position of button
        sendCons("Go to your discord window, then press G to start botting") # go to proper window to click on
        while True:
            if keyboard.is_pressed('G'):
                break;
        os.system('cls') # clear screen again
        print(mainColor + ascii_text) # print ascii art again

        sendCons("Starting loop") # start the loop of your main task
        sendCons("Hold down G to quit") # if user wants to quit press g
        this.started_time = time.time() # setting started time
        while True:
            if keyboard.is_pressed('G'):
                break;
            this.sendBot() # send bot
            time.sleep(1) # wait 4 seconds
        sendCons(f"Finished opening discord party mode, opened {this.count} times") # finished botting

bot = Bot()
bot.main() # run main function
    

