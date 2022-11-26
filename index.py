import src.auth.gateway_connect as Gtw
import src.tools.get_env as env


def init_app():
  Gtw.Gateway()


def main():
  init_app()


if __name__ == '__main__': main()

