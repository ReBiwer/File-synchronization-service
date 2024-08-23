import configparser


def _get_ConfigParser() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    _read_config_file(config)
    return config


def _read_config_file(parser: configparser.ConfigParser) -> None:
    parser.read('config.ini')


def get_keyOAuth() -> str:
    config = _get_ConfigParser()
    return config.get("API", 'key_OAuth')


def get_name_log_file() -> str:
    config = _get_ConfigParser()
    return config.get('logger', 'name_log_file')
