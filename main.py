import configparser


def get_key_OAuth() -> str:
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    key = conf.get("API", 'kay_OAuth')
    return key


if __name__ == '__main__':
    get_key_OAuth()
