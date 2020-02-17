def get_proxy():
    try:
        proxy_url, username, password = open('sensitive_data/proxy.txt', 'r').read().split(';')
        return {
            'proxy_url': proxy_url,
            'urllib3_proxy_kwargs': {
                'username': username,
                'password': password,
            }
        }
    except:
        return None


def get_bot_token():
    return open('sensitive_data/bot_token.txt', 'r').read()