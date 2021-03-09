import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'axe.! response= {response.status_code}')
        print(f'konten {response.text}')
    else:
        print(f'ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'ada Error{e}')
print('program selesai')

