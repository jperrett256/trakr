import argparse

parser = argparse.ArgumentParser(   prog='trakr',           \
                                    description='Tracks time spent.')
subparsers = parser.add_subparsers( required=True,          \
                                    dest='cmd',             \
                                    metavar='command')

# parse task subcommand
parser_task = subparsers.add_parser('task',                 \
                                    description='''
                                        Manages task names.
                                        Will show all tasks if run without arguments.
                                    ''',                    \
                                    help='manage tasks')

group_task_options = parser_task.add_mutually_exclusive_group()
group_task_options.add_argument('-c', '--create',           \
                                metavar='name',             \
                                help='create new task')
group_task_options.add_argument('-d', '--delete',           \
                                metavar='name',             \
                                help='delete a task')
group_task_options.add_argument('-D', '--force-delete',     \
                                metavar='name',             \
                                help='force delete a task')
group_task_options.add_argument('-m', '--rename',           \
                                metavar='name',             \
                                help='rename current task')

# parse switch subcommand
parser_switch = subparsers.add_parser(  'switch',           \
                                        help='change current task')

parser_switch.add_argument( 'name',                         \
                            help='task name to switch to')

parser_switch.add_argument( '-c', '--create',               \
                            action='store_true',            \
                            help='create task if it does not exist')

# parse log subcommand
parser_log = subparsers.add_parser( 'log',                  \
                                    help='show previous session data for current task')

# parse session subcommand
parser_session = subparsers.add_parser( 'session',          \
                                        help='manage ongoing sessions')

parser_session_cmds = parser_session.add_subparsers(title='options',        \
                                                    dest='session_cmd',     \
                                                    metavar='subcommand')

parser_session_info =   \
    parser_session_cmds.add_parser( 'info',         \
                                    help='show current session')

parser_session_info.add_argument('-a', '--all',                  \
                            action='store_true',            \
                            help='show all ongoing sessions')

parser_session_cmds.add_parser( 'start',            \
                                help='start new session or resume current session')

parser_session_cmds.add_parser( 'pause',            \
                                help='pause current session')

parser_session_cmds.add_parser( 'stop',             \
                                help='stop current session')

# parse edit subcommand
parser_edit = subparsers.add_parser('edit',             \
                                    description='TODO', \
                                    help='edit session data')

# TODO add more for edit subcommand

# TODO move parser to separate module?

args = parser.parse_args()

print(args)
