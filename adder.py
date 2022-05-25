'''
=============ᴍᴀsᴛᴇʀᴍɪɴᴅ ɴᴇᴛᴡᴏʀᴋ ᴏғғɪᴄɪᴀʟ=====================
ᴍᴜᴋᴇsʜ 2.0 ᴍᴇᴍʙᴇʀs ᴀᴅᴅɪɴɢ sᴄʀɪᴘᴛ
ᴄᴏᴅᴇᴅ  ʙʏ  ᴍᴜᴋᴇsʜ - @itz_mst_boy
ᴀᴘᴏʟᴏɢɪᴇs ɪғ ᴀɴʏᴛʜɪɴɢ ɪɴ ᴛʜᴇ ᴄᴏᴅᴇ ɪs ᴅᴜᴍʙ :)
************************************************
'''

# import libraries
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
    # fancy logo
    b = [
  ' ─────╔╗──╔═╦╗',
  ' ╔══╦╦╣╠╦═╣═╣╚╗',
  ' ║║║║║║═╣╩╬═║║║',
  ' ╚╩╩╩═╩╩╩═╩═╩╩╝',
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{rs}')
    #print('=============ᴍᴀsᴛᴇʀᴍɪɴᴅ ɴᴇᴛᴡᴏʀᴋ ᴏғғɪᴄɪᴀʟ==============')
    print(f'{lg}   version : {w}2.0{lg} | author : {w}ᴍᴜᴋᴇsʜ{rs}\n')


# function to clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# create sessions(if any) and check for any banned accounts
# TODO: Remove code input(just to check if an account is banned)
print('\n' + info + lg + ' ᴄʜᴇᴄᴋɪɴɢ ғᴏʀ ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛs...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Checking {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 11849799, '2bdcc0f0b3a04954d1cc1b11d5a1f669')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('ᴏᴋ')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}ɪs ʙᴀɴɴᴇᴅ!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' ʙᴀɴɴᴇᴅ ᴀᴄᴄᴏᴜɴᴛ ʀᴇᴍᴏᴠᴇᴅ[Remove permanently using manager.py]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' sᴇssɪᴏɴs ᴄʀᴇᴀᴛᴇᴅ!')
clr()
banner()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} sᴇssɪᴏɴ sᴛᴏʀᴇᴅ ɪɴ {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} ᴘʀᴇss ᴇɴᴛᴇʀ ᴛᴏ ᴇxɪᴛ...')
    clr()
    banner()
    sys.exit()

# read user details
try:
    # rquest to resume adding
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} ʀᴇsᴜᴍᴇ sᴄʀᴀᴘɪɴɢ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} ᴘᴜʙʟɪᴄ/ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ ʟɪɴᴋ ᴛᴏ sᴄʀᴀᴘᴇ ᴍᴇᴍʙᴇʀs: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} ᴘᴜʙʟɪᴄ/ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ ʟɪɴᴋ ᴛᴏ sᴄʀᴀᴘᴇ  ᴍᴇᴍʙᴇʀs: {r}')
    index = 0
# load all the accounts(phonenumbers)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} Total accounts: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} ᴇɴᴛᴇʀ ɴᴜᴍʙᴇʀ ᴏғ ᴀᴄᴄᴏᴜɴᴛs ᴛᴏ ᴜsᴇ: {r}'))
print(f'{info}{cy} ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴘᴛɪᴏɴ{lg}')
print(f'{cy}[0]{lg} ᴀᴅᴅ ᴛᴏ ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ')
print(f'{cy}[1]{lg} ᴀᴅᴅ ᴛᴏ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ')
choice = int(input(f'{INPUT}{cy} ᴇɴᴛᴇʀ ᴄʜᴏɪᴄᴇ: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} ᴇɴᴛᴇʀ ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ ʟɪɴᴋ : {r}'))
else:
    target = str(input(f'{INPUT}{cy} ᴇɴᴛᴇʀ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ ʟɪɴᴋ: {r}'))
print(f'{grey}_'*50)
#status_choice = str(input(f'{INPUT}{cy} ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ ᴀᴅᴅ ᴀᴄᴛɪᴠᴇ ᴍᴇᴍʙᴇʀs?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('vars.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} ᴇɴᴛᴇʀ ᴅᴇʟᴀʏ ᴛɪᴍᴇ ᴘᴇʀ ʀᴇǫᴜᴇsᴛ{w}[{lg}0 ғᴏʀ ɴᴏɴᴇ{w}]: {r}'))
#print(f'{info}{lg} ᴊᴏɪɴɪɴɢ ɢʀᴏᴜᴘ ғʀᴏᴍ {w}{number_of_accs} ᴀᴄᴄᴏᴜɴᴛs...')
#print(f'{grey}-'*50)
print(f'{success}{lg} -- ᴀᴅᴅɪɴɢ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ {w}{len(to_use)}{lg} ᴀᴄᴄᴏᴜɴᴛ(s) --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 11849799 , '2bdcc0f0b3a04954d1cc1b11d5a1f669')
    print(f'{plus}{grey} User: {cy}{acc[0]}{lg} -- {cy}sᴛᴀʀᴛɪɴɢ sᴇssɪᴏɴ... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴛᴏ sᴄʀᴀᴘᴇ')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴛᴏ sᴄʀᴀᴘᴇ')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴛᴏ ᴀᴅᴅ')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- ᴊᴏɪɴᴇᴅ ɢʀᴏᴜᴘ ᴛᴏ ᴀᴅᴅ')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} User: {cy}{acc_name}{lg} -- ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}ʀᴇᴛʀɪᴇᴠɪɴɢ ᴇɴᴛɪᴛɪᴇs...')
    #c.get_dialogs()
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, limit = 5500)
    except Exception as e:
        print(f'{error}{r} ᴄᴏᴜʟᴅɴ'ᴛ sᴄʀᴀᴘᴇ ᴍᴇᴍʙᴇʀs')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} ɴᴏ ᴍᴇᴍʙᴇʀs ᴛᴏ ᴀᴅᴅ!')
        continue
    print(f'{info}{lg} Start: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} ᴛᴏᴏ ᴍᴀɴʏ ᴘᴇᴇʀ  ғʟᴏᴏᴅ ᴇʀʀᴏʀs!ᴄʟᴏsɪɴɢ sᴇssɪᴏɴ...')
            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} User: {cy}{acc_name}{lg} -- sʟᴇᴇᴘ 1 sᴇᴄᴏɴᴅ')
            adding_status += 1
            print(f'{info}{grey} User: {cy}{acc_name}{lg} -- sʟᴇᴇᴘ {w}{sleep_time} {lg}sᴇᴄᴏɴᴅ(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}ᴜsᴇʀ ᴘʀɪᴠᴀᴄʏ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴇʀʀᴏʀ ʙᴄ')
            continue
        except PeerFloodError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}ᴘᴇᴇʀ ғʟᴏᴏᴅ ᴇʀʀᴏʀ.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} ᴄᴀɴ'ᴛ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ. ᴄᴏɴᴛᴀᴄᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴍᴇᴍʙᴇʀs ᴀᴅᴅɪɴɢ')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} ᴜsᴇʀ: {cy}{acc_name}{lg} -- {r}ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴡʀɪᴛɪɴɢ ɪɴ ɢʀᴏᴜᴘs')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}ᴄʜᴀᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɴᴇᴇᴅᴇᴅ ᴛᴏ ᴀᴅᴅ')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} ᴇʀʀᴏʀ ɪɴ ᴇɴᴛɪᴛʏ')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- ᴀᴅᴅɪɴɢ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} ᴀᴅᴅɪɴɢ sᴇssɪᴏɴ ᴇɴᴅᴇᴅ")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
