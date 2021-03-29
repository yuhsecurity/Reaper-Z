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
phone = input("Phone Number: ")
print("                               1. Whitepages")
print("                               2. Canada411")
print("                               3. Google")
sel = input("Mode: ")
if sel == "1":
    webbrowser.open('https://www.whitepages.com/phone/'+phone)
    quit
elif sel == "2":
    webbrowser.open('https://canada411.yellowpages.ca/fs/'+phone)
    quit
elif sel == "3":
    webbrowser.open('https://google.com/search?q='+phone)
    quit
else:
    os.system('cls')
    print("[+] Syntax Error!")
    time.sleep(1)
    import reaper
