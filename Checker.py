import json
import sys
import time
from datetime import datetime, date
import requests


def saveSettings(settingsDict):
    with open(path_settings, 'w') as outfile:
        json.dump(settingsDict, outfile)
    return

def loadSettings():
    settings = None
    path_settings = 'settings.json'
    try:
        settingsFile = open(path_settings, 'r')
        settingsJson = settingsFile.read()
        settingsFile.close
        settings = json.loads(settingsJson)
    except:
        print('Failed to load ' + path_settings)
        settings = {}
    return settings

# Returns user input with defined number of digits
def userInputDefinedLengthNumber(numberof_digits):
    while True:
        input_str = input()
        if len(input_str) != numberof_digits:
            print('Entered number consists of more or less than ' + str(numberof_digits) + ' digits')
            continue
        if not input_str.isdecimal():
            print('Please enter a NUMBER')
            continue
        return int(input_str)

def userInputNumber():
    while True:
        input_str = input()
        if not input_str.isdecimal():
            print('Please enter a NUMBER')
            continue
        return input_str

####################################################################################################
VERSION = '0.1.3'
path_settings = 'settings.json'
print('Welcome to NetzclubChecker %s' % VERSION)
settings = loadSettings()

# netzclub+ data:
phone_number = settings.get('phone_number', None)
userid = settings.get('userid', None)
session_id = settings.get('session_id', None)

# netzclub data - some params are identifyable in the code as they're ending with '2':
user_id2 = settings.get('user_id2', None)
session_id2 = settings.get('session_id2', None)
account_id = settings.get('account_id', None)
subscription_id = settings.get('subscription_id', None)
password = settings.get('password', None)
####################################################################################################
# Data for 'netzclub+' app: https://play.google.com/store/apps/details?id=net.netzclub.plus
api_base = 'https://netzclub.postr.co.nz'
# Choose your favorite weapon here: https://deviceatlas.com/blog/list-of-user-agent-strings
smartphone_model = 'SM-G960F'
smartphone_manufacturer = 'Samsung'
android_version = 'Android 8.0.0'
version = '23'
sdk_version = '60'
android_sdk_version = '26'
headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; %s; %s Build/R16NW)' % (android_version, smartphone_model),
           'Content-Type': 'application/json',
           'Accept': 'text/plain'
           }
base_get_data = {'version': version, 'sdk_version': sdk_version, 'android_sdk_version': android_sdk_version}
smartphone_get_data = {'model': smartphone_model, 'manufacturer': smartphone_manufacturer, 'brand': smartphone_model,
                       'os': android_version}
####################################################################################################
# Data for 'netzclub' app: https://play.google.com/store/apps/details?id=com.telefonica.netzclub.csc
api_base2 = 'https://rator.netzclub.net/api/v2'
headers2 = {'User-Agent': 'okhttp/4.0.1',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Language': 'lt'
            }

####################################################################################################
if phone_number is None or password is None:
    print('First run - congratulations for using this script dear user')
    print('Please enter your phone number:')
    phone_number = userInputNumber()
    print('Please enter your password for \'netzclub.net/login/\':')
    password = input()
    settings['phone_number'] = phone_number
    settings['password'] = password
    print('Thanks :) Now press ENTER to start')
    input()
print('Checking account %s' % phone_number)

prefix_logging_netzclub_plus = '[netzclub+] '
print(prefix_logging_netzclub_plus + 'Checking netzclub+ account')

timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+0200")

login_counter1 = 0
full_login_done = False
while login_counter1 <= 2:
    login_counter1 += 1
    if session_id is None or login_counter1 > 1:
        print(prefix_logging_netzclub_plus + 'Performing full netzclub+ login')
        print(prefix_logging_netzclub_plus + 'Login step 1/2')
        get_vars = {
            'mobile': phone_number,
            'google_ad_id': '',
            'is_limit_ad_tracking_enabled': 'false',
            'model': smartphone_model,
            'manufacturer': smartphone_manufacturer,
            'brand': smartphone_model,
            'os': android_version,
            'mcc': '262',
            'mnc': '3',
            'locale': 'de',
            'timestamp': timestamp
        }
        get_vars.update(base_get_data)
        response = requests.get(
            api_base + '/SendVerify',
            params=get_vars,
            headers=headers
        )
        info = response.json()
        settings['last_SendVerify'] = info
        result = info.get('result', False)
        guid = info.get('guid', None)
        if result is None or guid is None:
            print(prefix_logging_netzclub_plus + 'Fatal Login failure! Did you enter a wrong phone number?')
            sys.exit()
        print(prefix_logging_netzclub_plus + 'Login step 2/2')
        expected_numberof_digits = 4
        print(prefix_logging_netzclub_plus + 'Enter SMS verification (%d digits):' % expected_numberof_digits)
        sms_verification = userInputDefinedLengthNumber(expected_numberof_digits)
        get_vars = {
            'guid': guid,
            'mobile': phone_number,
            'code': sms_verification,
            'google_ad_id': '',
            'is_limit_ad_tracking_enabled': 'false',
            'model': smartphone_model,
            'manufacturer': smartphone_manufacturer,
            'brand': smartphone_model,
            'os': android_version,
            'mcc': '262',
            'mnc': '3',
            'locale': 'de',
            'timestamp': timestamp
        }
        get_vars.update(base_get_data)
        response = requests.get(
            api_base + '/CheckVerificationCode',
            params=get_vars,
            headers=headers
        )
        info = response.json()
        settings['last_CheckVerificationCode'] = info
        session_id = info.get('session', None)
        userid = info.get('user_id', None)
        if session_id is None or userid is None:
            print(prefix_logging_netzclub_plus + 'Login failed --> Did you enter a wrong SMS code?')
            if not info.get('existing_user', True):
                # 2020-02-07: This may happen for users who have never ever used the netzclub+ app. A step might be missing in the script. This will be fixed in a future version.
                print('First time user? Try to login via netzclub+ app one time, then run this script again')
            sys.exit()
        # Save logindata as user entered correct information
        saveSettings(settings)
        print(prefix_logging_netzclub_plus + 'Successfully logged in :)')
        print(prefix_logging_netzclub_plus + 'New sessionid: %s' % session_id)
        # Update this to save it later
        settings['session_id'] = session_id
        settings['userid'] = userid
        # Save users' logindata as it is valid
        saveSettings(settings)
        full_login_done = True
    print(prefix_logging_netzclub_plus + 'Getting cycle information ...')
    get_vars = {
        'hash': session_id,
        'userid': userid,
        'timestamp': timestamp
    }
    response = requests.get(
        api_base + '/GetCollectingInfo',
        params=get_vars,
        headers=headers
    )
    info = response.json()
    settings['last_GetCollectingInfo'] = info
    result = info.get('result', False)
    if not result:
        # Have we already fully logged in before? Then we don't need to do this again --> something went seriously wrong here!
        if full_login_done:
            # This should never happen
            print('Unknown login failure')
            sys.exit()
        print(prefix_logging_netzclub_plus + 'Failure: Maybe old session?')
        continue
    else:
        break
####################################################################################################
print(prefix_logging_netzclub_plus + 'Getting GetGeneralConfig ...')
get_vars = {
    'hash': session_id,
    'userid': userid,
    'wifi': 'true',
    'timestamp': timestamp
}
get_vars.update(base_get_data)
response = requests.get(
    api_base + '/GetGeneralConfig',
    params=get_vars,
    headers=headers
)
info = response.json()
settings['last_GetGeneralConfig'] = info
####################################################################################################
# This is what happens when the user unlocks his smartphone:
print(prefix_logging_netzclub_plus + 'Swiping unlock ...')
get_vars = {
    'userid': userid,
    'hash': session_id,
    'wifi': 'true',
    'timestamp': timestamp,
    'swipe_tracked': 'false',
    'jsondata': '%7B%22type%22%3A%22UserClickSwipeAndContent%22%2C%22clicks%22%3A0%2C%22impressions%22%3A1%2C%22screen_on_impressions%22%3A0%2C%22ad_id%22%3A%22%22%2C%22video_position%22%3A-1%7D',
}
get_vars.update(base_get_data)
response = requests.get(
    api_base + '/UserSwipe',
    # params=get_vars,
    headers=headers
)
info = response.json()
settings['last_UserSwipe'] = info
# TODO: Find out what result means here and why API will often return 'false' at this point
result = info.get('result', False)
if not result:
    # This should never happen
    print('Swipe failed(?)')
else:
    print('Swipe successful')
print('***************************************************************************')
####################################################################################################
# Optional: Get data from other Netzclub app (we only want to get current traffic remaining and max traffic but API returns even more if you want :)
trafficmax_mb = -1
trafficleft_mb = -1
traffic_unit2 = None
cycleEndDate = None
login_counter2 = 0
netzclub_login2_successful = False
prefix_logging_netzclub = '[netzclub] '
print(prefix_logging_netzclub + 'Checking normal netzclub account')
if password is None:
    print(prefix_logging_netzclub + 'Cannot get additional data as password is not given')
else:
    full_login_done = False
    while login_counter2 <= 2:
        login_counter2 += 1
        if user_id2 is None or session_id2 is None or account_id is None or subscription_id is None or login_counter2 > 1:
            # 2020-02-02: Seems like their API is more stable than their website - it did still work while website login was impossible because of 504 gateway timeout: https://www.netzclub.net/selfcare/
            print(prefix_logging_netzclub + 'Performing full netzclub login')
            response = requests.post(
                api_base2 + '/auth/login',
                json={'username': phone_number, 'password': password},
                headers=headers2
            )
            info = response.json()
            settings['last_get_counter'] = info
            account_id = info.get('accountId', None)
            user_id2 = info.get('userId', None)
            session_id2 = info.get('accessToken', None)
            subscription_id = info.get('subscriptionId', None)
            if account_id is None or user_id2 is None or session_id2 is None or subscription_id is None:
                print(prefix_logging_netzclub + 'Unable to login --> Continuing execution but I won\'t be able to display all information of your account :(')
                break
            print(prefix_logging_netzclub + 'Login successful :)')
            settings['account_id'] = account_id
            settings['user_id2'] = user_id2
            settings['session_id2'] = session_id2
            settings['subscription_id'] = subscription_id
            saveSettings(settings)
            full_login_done = True
        # Authorize the following requests
        headers2['Authorization'] = 'Bearer ' + session_id2
        # print('Getting account balance ...')
        # response = requests.get(
        #     api_base + '/user/get-balance/' + accountid2,
        #     headers=headers
        # )
        # info = response.json()
        # settings['last_get_balance'] = info
        print(prefix_logging_netzclub + 'Obtaining traffic data ...')
        # 2020-02-02: Website/API is slow so this request will sometimes end up in a timeout
        try:
            response = requests.get(
                api_base2 + '/user/get-counter/' + subscription_id,
                headers=headers2
            )
        except:
            print(prefix_logging_netzclub + 'Failed to get traffic data ... try again next time')
            break
        info = response.json()
        settings['last_get-counter'] = info
        errormessage = info.get('message', None)
        if errormessage is not None:
            if full_login_done:
                # This should never happen
                print('Unknown login failure')
                break
            print(prefix_logging_netzclub + 'Possibly bad session --> Full login required')
            continue
        traffic_info_netzclub = info['counter'][0]
        trafficmax_mb = traffic_info_netzclub['total']
        trafficleft_mb = traffic_info_netzclub['left']
        traffic_unit2 = traffic_info_netzclub['unit']
        cycleEndDate = traffic_info_netzclub['cycleEndDate']
        if traffic_unit2 == 'Megabytes':
            # Use same unit that netzclub+ API is using.
            traffic_unit2 = 'MB'
        netzclub_login2_successful = True
        break
####################################################################################################
# Save settings
saveSettings(settings)

traffic_info = settings['last_GetCollectingInfo']
countdown_info = traffic_info['countdown'][0]
howmuch_extra_traffic_now = traffic_info['additional_earnings_amount']
last_time_extra_traffic = traffic_info.get('last_rewarded', None)
last_time_active = traffic_info.get('last_active', None)

days_until_more_traffic = traffic_info['days_left']
howmuch_extra_traffic_then = countdown_info['value']
traffic_unit1 = countdown_info['currency']

future_timestamp = datetime.now().timestamp() + days_until_more_traffic * 24 * 60 * 60
date_when_more_traffic = datetime.fromtimestamp(future_timestamp).strftime("%d.%m.%Y um %H:%M:%S Uhr")

print('***************************************************************************')
# TODO: Maybe make the dates nicer --> German
if trafficmax_mb > -1 and trafficleft_mb > -1 and traffic_unit2 is not None:
    print(prefix_logging_netzclub + 'Traffic left: %d%s/%d%s' % (trafficleft_mb, traffic_unit2, trafficmax_mb, traffic_unit2))
print(prefix_logging_netzclub_plus + 'Your extra traffic now: %d%s' % (howmuch_extra_traffic_now, traffic_unit1))
print(prefix_logging_netzclub_plus + 'You will get %d%s extra traffic in %d days on the %s' % (
    howmuch_extra_traffic_then, traffic_unit1, days_until_more_traffic, date_when_more_traffic))
print(prefix_logging_netzclub_plus + 'Last time extra traffic: %s' % last_time_extra_traffic)
print(prefix_logging_netzclub_plus + 'Last time active: %s' % last_time_active)
print('***************************************************************************')
close_seconds = 20
print('Closing in %d seconds' % close_seconds)
time.sleep(close_seconds)

sys.exit()
