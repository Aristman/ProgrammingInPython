from requests import get
import datetime

def calc_age(uid):
    result = {}
    user_keys = {
        'v': '5.71',
        'access_token': '4fd4e06b4fd4e06b4fd4e06b724fa694a844fd44fd4e06b110f89c9869308975cfcef33',
        'user_ids': str(uid)
    }
    user_url = 'https://api.vk.com/method/users.get'
    user_request = get(user_url, params=user_keys)
    frends_url = 'https://api.vk.com/method/friends.get'
    frends_keys = {
        'v': '5.71',
        'access_token': '4fd4e06b4fd4e06b4fd4e06b724fa694a844fd44fd4e06b110f89c9869308975cfcef33',
        'user_id': str(user_request.json()['response'][0]['id']),
        'fields': 'bdate'
    }
    frends_request = get(frends_url, frends_keys)
    for frend in frends_request.json()['response']['items']:
        if 'bdate' in frend.keys():
            frend_bdate = frend['bdate'].split('.')
            if len(frend_bdate) == 3:
                age = datetime.date.today().year - int(frend_bdate[2])
                result[age] = result.get(age, 0) + 1
    result = sorted(
        sorted(
            list(
                zip(result.keys(),
                    result.values()
                    )
            )
        ), key=lambda x: x[1], reverse=True)
    return result

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
