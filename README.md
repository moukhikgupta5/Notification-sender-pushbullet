# Notification-sender-pushbullet

A simple Flask API to update our firebase database and alert user by sending notifications on the mobile device.

## Prerequisites
1. Get your firebase credentials/configuration file for python and Database URL from the firebase console and put it in the root folder.
2. Replace firebase.json with the actual link to the file in "app.py".
3. Replace DATABASE_URL with the actual URL in "app.py"

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```
The application will be started and it will start running on port - [6486](http://127.0.0.1:6486/)