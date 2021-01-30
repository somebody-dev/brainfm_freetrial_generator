try:
    import requests
    import random
    import string
    import colorama 
    colorama.init(autoreset=True)

except:
    import os
    os.system('pip install requests')
    os.system('pip install colorama')

req = requests.Session()

ip = ""

def get_ip():
    ip = requests.get('https://api.ipify.org?format=text').text

def create_account():
    while True:
        get_ip()
        cookie = req.get('https://brain.fm/')
        cookie.cookies = req.cookies
        cookie.headers = req.headers
        email = ''.join(random.choice(string.ascii_letters) for i in range(10)) + '@zebins.com'
        other_cookie = req.post('https://brain.fm/user/isEmailTaken', json={'email' : email, 'ip' : ip})
        other_cookie.cookies = req.cookies
        password = ''.join(random.choice(string.ascii_letters) for i in range(10))
        headers = {
            'Host': 'www.brain.fm',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept' : 'application/json, text/plain, */*',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.brain.fm/',
            'Content-Type': 'application/json;charset=utf-8',
            'Content' : '-Length: 156',
            'Origin' : 'https://www.brain.fm',
            'Connection' : 'keep-alive',
            'TE' : 'Trailers',
            'Pragma': 'no-cache',
            'Cache-Control' : 'no-cache'
        }
        req.headers = headers
        json = {
            'consent' : '',
            'email' : email,
            'ip' : ip,
            'name' : ''.join(random.choice(string.ascii_letters) for i in range(7)),
            'partnerId' : '',
            'password' : password,
            'type' : 'SIGNUP'
        }
        account = req.post('https://brain.fm/signup', json=json)
        if account.status_code == 200:
            print(colorama.Fore.GREEN + email + ":" + password)

        else:
            print('Could not reach API.')
            

if __name__ == '__main__':
    create_account()
