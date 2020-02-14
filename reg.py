import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()

txtid = input('Masukan Link Live : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/" + slink)
print(socketstring)
botauthtoken2 = '3939cfabcc505de2b5dc51f367bdf75a65ea2731' #token lu disini
mypesan = '{"live_id":'+slink+',"token":"'+botauthtoken2+'","event":"live_join"}'###### end


def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Hallo DEKA datang !! UYY 馃構"}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = [
         '馃き馃き馃き', '馃檮馃檮馃檮', '馃槤馃槤馃槤', '馃槆馃槆馃槆', '馃槍馃槍馃槍', '馃様馃様馃様', '馃ズ馃ズ馃ズ']
        ya = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"IYA ' + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"TIDAK ' + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"MUNGKIN AJA ' + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"G ' + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 'd' and psn[-1:] == '?':
            kambeng = random.choice(listjawaban)
            print(kambeng)
            ws.send(kambeng)
        ljoin = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Hei ' + nick + ' welcome !! kamu jelek馃槼"}'
        #lsjoin = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Hayooo ' + nick + ' Ngeghost"}'
        llike = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"makasih cinta boongnya akak ' + nick + ' uyy  鉂ｏ笍"}'
        tidur = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Goodbye Deka parkun dulu 馃槝"}'
        bangun = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Hei im back"}'
        ping = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Apa ' + nick + ' Manggil虏 Sokap !! 馃槒"}'
        makasih = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + ' unchhh sama sama zheyeng 馃槝"}'
        jawab = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":" Deka disini akak  ' + nick + '  zheyeng 馃槝 "}'
        rank = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Liat rank sendiri aja dih"}'
        if evn == 'live_message' and (psn == '#status' or psn == '#durasi' or psn == '#info'):
            createdl = response2.json()['results'][0]['created']
            tanggal = datetime.today()
            cre = createdl[:-17]
            crea = createdl[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timehl2 = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"room ini sudah online selama馃挄馃挮 ' + str(timehl2) + ' 馃挄馃挮"}')
        if evn == 'live_join':
            if status == 'bangun':
                ws.send(ljoin)
            if evn == 'live_shadowjoin':
                ws.send(lsjoin)
        if evn == 'live_like' and status == 'bangun':
            ws.send(llike)
        if evn == 'live_message' and psn == '#off' and status == 'bangun':
            status = 'tidur'
            ws.send(tidur)
        if evn == 'live_message' and psn == '#rank':
            headers3 = {'User-Agent': 'Mozilla/5.0'}
            response3 = requests.get('https://id-api.spooncast.net/lives/popular/', headers=headers3)
            ws.send(rank)
        if evn == 'live_message' and psn[:-3] == '#rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn[:-2] == '#rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn == '#me':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = tag
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn[:4] == '#cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = psn[5:]
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn == '#on' and status == 'tidur':
            status = 'bangun'
            ws.send(bangun)
        if evn == 'live_message' and psn == 'deka':
            ws.send(ping)
        if evn == 'live_message' and psn == 'Makasih':
                ws.send(makasih)
        if evn == 'live_message' and psn == 'deka鈥忊�忊�� 鈥�':
            ws.send(jawab)
        if evn == 'live_message':
            if psn == 'deka keluar' and uid == '210900010':
                ws.close()
def on_close(ws): #on close of the bot.
    print ("### closed ###")
    
def on_open(ws): #when the bot initially connects.
 print ("open")
 time.sleep(1)
 ws.send(mypesan)
 time.sleep(1)
 gblk = """
 Connected
 """
 print(gblk)
 time.sleep(1)

if __name__ == "__main__":
 
 websocket.enableTrace(True)
 ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,                                           
                              on_message = on_message,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever