from datetime import datetime as dt
from time import sleep
from os import system
from tkinter import simpledialog
from random import randrange as rr
from math import ceil

print("PLEASE MAKE SURE xcowsay AND tkinter ARE INSTALLED")

def mainloop(end_time):
    last_diff = -10000
    while 1:
        diff = ceil((end_time - dt.now()).seconds/60)
        print(diff)
        if last_diff == diff:
            sleep(10)
            continue
        last_diff = diff
        if diff == 1440:
            endqutes = ['You made it!', 'Finally over!', 'Time\'s up!', 'Congrats. You\'re done!']
            for i in range(100):
                system(f"xcowsay -t 20 \"{endqutes[rr(len(endqutes))]}\" &")
            quit()
            break
        system(f"xcowsay -t 5 \"{diff} Minutes left\"")

end_time_str = None
while end_time_str is None:
    end_time_str = simpledialog.askstring("Input", "What time will your lesson end (24h, format: \"hh:mm\")?")
    try:
        end_time = dt(dt.now().year, dt.now().month, dt.now().day, int(end_time_str.split(":")[0]), int(end_time_str.split(":")[1]))
        print(f"End-Time: {end_time}")
        break
    except Exception as E:
        print(E)
        continue
mainloop(end_time)


