import urllib.request

url = 'https://blog.python.org/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = str(res.read())

if 'security' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります')
    print('https://blog.python.org/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')