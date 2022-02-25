import platform, os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = os.environ.get("ENV_FILE_LOCATION") or join(dirname(__file__), './app/configs/.env.dev')

if not Path(dotenv_path).exists():
    dotenv_path = join(dirname(__file__), './app/configs/.env.dev')

load_dotenv(dotenv_path)


PROJECT_NAME = 'SampleApplication'
PREFIX_NAME = 'SA'
SUFFIX_NAME = os.getenv(f"{PREFIX_NAME}_SUFFIX_NAME") or ""
VERSION = '1.0'
DEBUG = True

SECRET_KEY = os.environ.get(f"{PREFIX_NAME}_SECRET") or os.getenv(f"{PREFIX_NAME}_SECRET")

SYSTEM = platform.system().lower()
if SYSTEM=='windows':
    FILEPATH_SEPERATOR = '\\'
elif SYSTEM in ['linux', 'darwin']:   
    FILEPATH_SEPERATOR = '/'
