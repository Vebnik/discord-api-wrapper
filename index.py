import asyncio
import multiprocessing as mlp
import src.auth.gateway_connect as Gtw
import src.event.event_listener as Evt


def init_event_listen():
  Evt.Event_Listen()


def init_app():
  Gtw.Gateway()


def main():
  init_app()


if __name__ == '__main__': main()

