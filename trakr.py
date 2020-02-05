import argparse

parser = argparse.ArgumentParser(   prog='trakr',       \
                                    description='Tracks time spent.')
subparsers = parser.add_subparsers( required=True,      \
                                    dest='cmd',         \
                                    title='commands',   \
                                    help='additional help') # TODO fix help

# parse task subcommand
parser_task = subparsers.add_parser('task')
parser_task.add_argument('name', nargs='?')

group_task_options = parser_task.add_mutually_exclusive_group()
group_task_options.add_argument('-d', action='store_true',  \
                                help='delete current task')
group_task_options.add_argument('-D', action='store_true',  \
                                help='force delete current task')
group_task_options.add_argument('-m', action='store_true',  \
                                help='rename current task')

# parse switch subcommand
parser_switch = subparsers.add_parser('switch')

parser_log = subparsers.add_parser('log')

parser_session = subparsers.add_parser('session')

parser_edit = subparsers.add_parser('edit')

args = parser.parse_args()

print(args)
