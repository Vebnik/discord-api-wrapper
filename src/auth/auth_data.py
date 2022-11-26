from src.tools.get_env import get_env

auth_data = {
  "op": 2,
  "d": {
    "token": get_env('BOT_TOKEN'),
    "properties": {
      "os": "linux",
      "browser": "disco",
      "device": "disco"
    },
  "intents": 33607
  }
}

