import pprint as pp
import logging
import src.commands.commands_scoop as cmds
import src.interface.Message as msg


def commands_find(content: str):

  for command in cmds.commands:
    if command in content:
      return cmds.commands[command]

  return 'Not found commands'


def commands(func):
  def inner(args):
    try:
      mesasge = msg.Message(args)

      if mesasge.get_content().startswith('!'):
        func_commands = commands_find(mesasge.get_content())
        func_commands(mesasge)

      return func(args)
    except:
      logging.error('Error in commands')
      return func(args)

  return inner
