import time, os
from afplay import afplay
from datetime import datetime

current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ok_counter = 0

def website_blocker():
    websites = [
        "www.facebook.com",
        "facebook.com",
        "www.youtube.com",
        "youtube.com",
        "www.instagram.com",
        "instagram.com",
        "www.reddit.com",
        "reddit.com",
        "www.tiktok.com",
        "tiktok.com"
    ]
    
    hosts_path = "/etc/hosts"
    redirect_ip = "127.0.0.1"

    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in websites:
            entry = f"{redirect_ip} {site}\n"
            if entry not in content:
                file.write(entry)


for _ in range(10):
    # Dialog mit zwei Buttons
    afplay("/Users/conrad/Desktop/Libary/notification.mp3")
    result = os.popen(
        'osascript -e \'display dialog "Mach eine Pause und richte dich auf!" buttons {"Exit", "Snooze", "OK"} default button "OK"\''
    ).read().strip()

    print("AppleScript Ergebnis:", result)

    if "Snooze" in result:
        print("User hat Snooze gewählt → warte 5 Minuten")
        time.sleep(5*60)   # Test: 5 Sekunden, real: 5*60 für 5 Minuten
    else:
        print("User hat OK gedrückt → normal weiter")
        time.sleep(20*60)  # Test: 20 Sekunden, real: 20*60 für 20 Minuten
        ok_counter =+1
        print(ok_counter)
    if "Exit" in result:
        print("User hat Stop gewählt → beende das Programm")
        exit(0)
    