import configparser


def _get_ConfigParser() -> configparser.ConfigParser:
    return configparser.ConfigParser()


def _read_config_file(parser: configparser.ConfigParser) -> None:
    parser.read('config.ini')


def get_keyOAuth() -> str:
    config = _get_ConfigParser()
    _read_config_file(config)
    return config.get("API", 'kay_OAuth')

