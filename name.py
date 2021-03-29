import sys, os, time, signal, webbrowser, platform, subprocess
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
Name = input("Full Name: ")
print("                    1. Whitepages            4. Google")
print("                    2. Spokeo                5. Doxbin")
print("                    3. Twitter               6. YouTube")
num = input("Mode: ")
if num == "1":
    webbrowser.open('https://www.whitepages.com/name/'+Name)
    import reaper
elif num == "2":
    webbrowser.open('https://www.spokeo.com/'+Name)
    import reaper
elif num == "3":
    webbrowser.open('https://www.twitter.com/search?f=users&vertical=default&q='+Name)
    import reaper
elif num == "4":
    webbrowser.open('https://www.google.com/search?q='+Name)
    import reaper
elif num == "5":
    webbrowser.open('https://www.google.com/search?q=site:doxbin.org '+Name)
    import reaper
elif num == "6":
    webbrowser.open('https://www.linkedin.com/pub/dir/'+Name)
    import reaper
else:
    os.system('cls')
    print("[+] Syntax Error!")
    time.sleep(1)
    