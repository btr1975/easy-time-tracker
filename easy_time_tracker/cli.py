"""
easy_time_tracker CLI
"""
from argparse import ArgumentParser
from .easy_time_tracker import EasyTimeTracker


def cli() -> None:  # pragma: no cover
    """Function to run the command line
    :rtype: None
    :returns: None
    """
    arg_parser = ArgumentParser(description='easy-time-tracker')
    subparsers = arg_parser.add_subparsers(title='commands', description='Valid commands: a single command is required',
                                           help='CLI Help', dest='a single command please see the -h option')
    subparsers.required = True

    # This is the sub parser to start the clock for a time record
    arg_parser_start = subparsers.add_parser('start', help='Start the clock')
    arg_parser_start.set_defaults(which_sub='start')
    arg_parser_start.add_argument('-d', '--description', help='Description of the time')
    arg_parser_start.add_argument('-p', '--people', nargs='+', default=[], help='List of people')

    # This is the sub parser to stop the clock for a time record
    arg_parser_stop = subparsers.add_parser('stop', help='Stop the clock')
    arg_parser_stop.set_defaults(which_sub='stop')

    args = arg_parser.parse_args()

    try:
        ett_obj =EasyTimeTracker()
        if args.which_sub == 'start':
            ett_obj.start_time_record(args.description, args.people)

        elif args.which_sub == 'stop':
            ett_obj.end_time_record()

    except AttributeError as e:  # pylint: disable=invalid-name
        print(f'\n !!! {e} !!! \n')
        arg_parser.print_help()

    except FileNotFoundError as e:  # pylint: disable=invalid-name
        print(f'\n !!! {e} !!! \n')
        arg_parser.print_help()

    except Exception as e:  # pylint: disable=broad-except,invalid-name
        print(f'\n !!! {e} !!! \n')
        arg_parser.print_help()
