from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

try:
    import requests
except ImportError:
    print(f'{lg}[i] ɪɴsᴛᴀʟʟɪɴɢ ᴍᴏᴅᴜʟᴇ - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # ᴍᴜᴋᴇsʜ ʟᴏɢᴏ
    b = [
    

  ' ─────╔╗──╔═╦╗  ',
  ' ╔══╦╦╣╠╦═╣═╣╚╗ ',
  ' ║║║║║║═╣╩╬═║║║ ',
  ' ╚╩╩╩═╩╩╩═╩═╩╩╝ ',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============ᴍᴀsᴛᴇʀᴍɪɴᴅ ɴᴇᴛᴡᴏʀᴋ ᴏғғɪᴄɪᴀʟ==============')
    print(f'   ᴠᴇʀsɪᴏɴ: 2.0 | ᴀᴜᴛʜᴏʀ: ᴍᴜᴋᴇsʜ{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] ᴀᴅᴅ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛs ʙʙ'+n)
    print(lg+'[2] ғɪʟᴛᴇʀ ᴀʟʟ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛs'+n)
    print(lg+'[3] ᴅᴇʟᴇᴛᴇ sᴘᴇᴄɪғɪᴄ ᴀᴄᴄᴏᴜɴᴛs'+n)
    print(lg+'[4] ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ sᴄʀɪᴘᴛ ᴅᴏɴᴛ ᴜsᴇ'+n)
    print(lg+'[5] ᴇxɪᴛ'+n)
    a = int(input('\nᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ ʙʙ'))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{gr} [~] ᴇɴᴛᴇʀ  ɴᴜᴍʙᴇʀ ᴏғ ᴀᴄᴄᴏᴜɴᴛs ᴛᴏ ᴀᴅᴅ ᴇɢ(2 ᴏʀ 3): {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{ye} [~] ᴇɴᴛᴇʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ʙʙ: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{cy} [i] sᴀᴠᴇᴅ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛs ɪɴ vars.txt')
            clr()
            print(f'\n{gr} [*] ʟᴏɢɢɪɴɢ ɪɴ ғʀᴏᴍ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛs\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 11849799 , '2bdcc0f0b3a04954d1cc1b11d5a1f669')
                c.start(number)
                print(f'{ye}[+] ʟᴏɢɪɴ sᴜᴄᴄᴇssғᴜʟ ᴊᴏɪɴ @mr_sukkun')
                c.disconnect()
            input(f'\n ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴀᴄᴄᴏᴜɴᴛs ʙʙ! ᴘʟᴇᴀsᴇ ᴀᴅᴅ sᴏᴍᴇ ᴀɴᴅ ʀᴇᴛʀʏ')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 11849799 , '2bdcc0f0b3a04954d1cc1b11d5a1f669')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{blue}[+] {phone} ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' ɪs ʙᴀɴɴᴇᴅ 😞!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'ᴄᴏɴɢʀᴀᴛs! ɴᴏ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛs')
                input('\nᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] ᴀʟʟ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ʀᴇᴍᴏᴠᴇᴅ'+n)
                input('\nᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ  ɢᴏ ᴛᴏ  ᴍᴀɪɴ ᴍᴇɴᴜ...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{ye}[i] ᴄʜᴏᴏsᴇ ᴀɴ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] ᴇɴᴛᴇʀ ᴀ ᴄʜᴏɪᴄᴇ ʙʙ: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] ᴀᴄᴄᴏᴜɴᴛ ᴅᴇʟᴇᴛᴇᴅ{n}')
        input(f'\nᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏ ᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
        f.close()
    elif a == 4:
        # ᴛʜᴀɴᴋs ᴛᴏ github.com/Itz-mst-boy ғᴏʀ ᴛʜᴇ sɴɪᴘᴘᴇᴛ ʙᴇʟᴏᴡ
        print(f'\n{lg}[i] ᴄʜᴇᴄᴋɪɴɢ ғᴏʀ ᴜᴘᴅᴀᴛᴇs...')
        try:
            # https://raw.githubusercontent.com/Itz-mst-boy/termux/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/Itz-mst-boy/termux/main/version.txt')
        except:
            print(f'{r} ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ᴛʜᴇ  ɪɴᴛᴇʀɴᴇᴛ')
            print(f'{r} ᴘʟᴇᴀsᴇ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴀɴᴅ ʀᴇᴛʀʏ')
            exit()
        if float(version.text) > 0.9:
            prompt = str(input(f'{lg}[~] ᴜᴘᴅᴀᴛᴇ ᴀᴠᴀɪʟᴀʙʟᴇ[Version {version.text}]. ᴅᴏᴡɴʟᴏᴀᴅ?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴜᴘᴅᴀᴛᴇs...')
                if os.name == 'nt':
                    os.system('del adder.py')
                    os.system('del manager.py')
                else:
                    os.system('rm adder.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Itz-mst-boy/termux/main/rexadder.py')
                os.system('curl -l -O https://raw.githubusercontent.com/Itz-mst-boy/termux/main/rexmanager.py')
                print(f'{gr}[*] ᴜᴘᴅᴀᴛᴇᴅ ᴛᴏ ᴠᴇʀsɪᴏɴ: {version.text}')
                input('ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴇxɪᴛ...')
                exit()
            else:
                print(f'{lg}[!] ᴜᴘᴅᴀᴛᴇ ᴀʙᴏʀᴛᴇᴅ.')
                input('ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
        else:
            print(f'{lg}[i] ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ  ᴜᴘᴅᴀᴛᴇᴅ  ᴡʜʏ ʙᴜʟʟʏɪɴɢ ᴍᴇ ғᴜᴄᴋ')
            input('ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ɢᴏᴛᴏ ᴍᴀɪɴ ᴍᴇɴᴜ...')
    elif a == 5:
        clr()
        banner()
        exit()
