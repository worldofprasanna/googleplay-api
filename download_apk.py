import sys
import os
from gpapi.googleplay import GooglePlayAPI

def main():
  username = os.environ['GMAIL_USERNAME']
  password = os.environ['GMAIL_PASSWORD']
  storagepath = os.environ['STORAGE_PATH']
  appid = os.environ['APP_ID']
  server = GooglePlayAPI('en_US', 'America/New York', 'bacon')
  try:
    server.login(email=username, password=password)
    download = server.download(appid, expansion_files=False)
    apkpath = os.path.join(storagepath, download['docId'] + '.apk')
    if not os.path.isdir(storagepath):
      os.makedirs(storagepath)
    with open(apkpath, 'wb') as first:
      print('Downloading ' + download['docId'] + '.apk.....')
      for chunk in download.get('file').get('data'):
        first.write(chunk)
    print('APK downloaded and stored at ' + apkpath)
  except Exception as err:
    print("Login failed. Ensure that correct credentials are provided. {0}".format(err))
    sys.exit(1)

main()
