import os
from dotenv import load_dotenv


def main2():
    load_dotenv()
    print(os.environ['TEST_ENV_VAR'])


if __name__ == '__main__':
    main2()
