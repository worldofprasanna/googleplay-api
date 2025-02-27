# Google play python API [![Build Status](https://travis-ci.org/NoMore201/googleplay-api.svg?branch=master)](https://travis-ci.org/NoMore201/googleplay-api)

This fork is mainly to fix the [issue](https://github.com/NoMore201/googleplay-api/issues/98) with login. 

This needs 2 changes to be done,

1. Install this package from pypi using `pip install gpapi-login-fix`

2. To disable captcha security you have to unlock it using this [url](https://accounts.google.com/b/0/DisplayUnlockCaptcha)

To test the download apk use this command,

```
GMAIL_USERNAME=<> GMAIL_PASSWORD=<> APP_ID=<> STORAGE_PATH=<> python download_apk.py
```

This project contains an unofficial API for google play interactions. The code mainly comes from
[GooglePlayAPI project](https://github.com/egirault/googleplay-api/) which is not
maintained anymore. The code was updated with some important changes:

* ac2dm authentication with checkin and device info upload
* updated search and download calls
* select the device you want to fake from a list of pre-defined values (check `device.properties`)
(defaults to a OnePlus One)

# Build

This is the recommended way to build the package, since setuptools will take care of
generating the `googleplay_pb2.py` file needed by the library (check the `setup.py`)

```
$ python setup.py build
```

# Usage

Check scripts in `test` directory for more examples on how to use this API.

```
from gpapi.googleplay import GooglePlayAPI

mail = "mymail@google.com"
passwd = "mypasswd"

api = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="hero2lte")
api.login(email=mail, password=passwd)

result = server.search("firefox")

for doc in result:
    print("doc: {}".format(doc["docid"]))
    for cluster in doc["child"]:
        print("\tcluster: {}".format(cluster["docid"]))
        for app in cluster["child"]:
            print("\t\tapp: {}".format(app["docid"]))
```

For first time logins, you should only provide email and password.
The module will take care of initalizing the api, upload device information
to the google account you supplied, and retrieving 
a Google Service Framework ID (which, from now on, will be the android ID of your fake device).

For the next logins you **should** save the gsfId and the authSubToken, and provide them as parameters
to the login function. If you login again with email and password, this is the equivalent of
re-initalizing your android device with a google account, invalidating previous gsfId and authSubToken.
