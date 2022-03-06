import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def main():
    print("Hello World!")
    config = read_config()
    print(config["Machine"]["name"])


if __name__ == "__main__":
    main()
