import sys, os, time, webbrowser
os.system('cls')
print(" ▄▄▄       ███▄    █ ▄▄▄█████▓ ██▓     ██████  ▒█████   ▄████▄   ██▓ ▄▄▄       ██▓    ")
print("▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓██▒   ▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▒████▄    ▓██▒    ")
print("▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▒   ░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒▒██  ▀█▄  ▒██░    ")
print("░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██░     ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░░██▄▄▄▄██ ▒██░    ")
print(" ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░██░   ▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░ ▓█   ▓██▒░██████▒")
print(" ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░▓     ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓   ▒▒   ▓▒█░░ ▒░▓  ░")
print("  ▒   ▒▒ ░░ ░░   ░ ▒░    ░     ▒ ░   ░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░  ▒   ▒▒ ░░ ░ ▒  ░")
print("  ░   ▒      ░   ░ ░   ░       ▒ ░   ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░  ░   ▒     ░ ░   ")
print("      ░  ░         ░           ░           ░      ░ ░  ░ ░       ░        ░  ░    ░  ░")
print("                                                       ░                              ")
print("                               ============")
print("                                 REAPER Z")
print("                               ============")
addy = input("Street Address, City, State: ")
print("                               1. Google Maps")
print("                               2. OpenStreet")
print("                               3. MapQuest")
sel = input("Mode: ")
if sel == "1":
    webbrowser.open('https://www.google.com/maps/place/'+addy)
    quit
elif sel == "2":
    webbrowser.open('https://www.openstreetmap.org/search?query='+addy)
    quit
elif sel == "3":
    webbrowser.open('https://www.mapquest.com/search/result?query='+addy)
    quit
else:
    os.system('cls')
    print("[+] Syntax Error!")
    time.sleep(1)
    import reaper