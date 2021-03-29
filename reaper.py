import sys, os, time, webbrowser
os.system('cls')
def menu():
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
    print("                        1. Name        4. Address")
    print("                        2. Phone       5. IP Address")
    print("                        3. Username    6. Exit      ")
    Type = input("Mode: ")
    if Type == '1':
        import name
    elif Type == '2':
        import phone
    elif Type == '3':
        import user
    elif Type == '4':
        import addy
    elif Type == '5':
        import ip
    elif Type == '6':
        os.system('cls')
        quit
    else:
        os.system('cls')
        print("[+] Syntax Error")
        time.sleep(1)
        menu()
menu() 