import colorama


def connect_log(data):
  print(f'{colorama.Fore.BLUE}-'*20)
  print(f'OpCode: {data["op"]}\nInterval: {data["d"]["heartbeat_interval"]}')
  print(f'{colorama.Fore.BLUE}-'*20)


def info_event(data):
  print(f'{colorama.Fore.BLUE}{data}')


def info(data):
  print(f'{colorama.Fore.GREEN}{data}')


def warn(data):
  pass


def error(data):
  print(f'{colorama.Fore.RED}{data}')