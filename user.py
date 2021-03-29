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
username = input("Username: ")
print("                    1. Twitter             4. Discord")
print("                    2. Instagram           5. Google")
print("                    3. Steam               6. YouTube")
sel = input("Mode: ")
if sel == "1":
    webbrowser.open('https://www.twitter.com/search?f=users&vertical=default&q='+username)
    import reaper
elif sel == "2":
    webbrowser.open('https://searchusers.com/search/'+username)
    import reaper
elif sel == "3":
    webbrowser.open('https://steamcommunity.com/search/users/#text='+username)
    import reaper
elif sel == "4":
    webbrowser.open('https://discordhub.com/user/search?&user_search_bar='+username)
    import reaper
elif sel == "5":
    webbrowser.open('https://www.google.com/search?q='+username)
    import reaper
elif sel == "6":
    webbrowser.open('https://www.youtube.com/results?search_query='+username)
    import reaper
else:
    os.system('cls')
    print("[+] Syntax Error!")
    time.sleep(1)
    import reaper