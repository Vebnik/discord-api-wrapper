import pprint as pp
import src.tools.logger as logger
import src.commands.commands_scoop as cmds
import src.interface.Message as msg


def commands_find(content: str):

  for command in cmds.commands:
    if command in content:
      return cmds.commands[command]

  return 'Not found commands'


def commands(func):
  def inner(args):
    mesasge = msg.Message(args)

    if mesasge.get_content().startswith('!'):
      func_commands = commands_find(mesasge.get_content())
      func_commands(mesasge)

    return func(args)
    # try:

    # except:
    #   logger.error('Error in commands')
    #   return func(args)

  return inner
