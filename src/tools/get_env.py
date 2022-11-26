from os import getenv
from dotenv import load_dotenv



def get_env(key: str) -> str:
  load_dotenv()
  return getenv(key)