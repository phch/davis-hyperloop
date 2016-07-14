import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'host', metavar='HOST',
    help='remote host for the TCP connection',
)
parser.add_argument(
    'port', metavar='PORT',
    help='remote port for the TCP connection',
)
parser.add_argument(
    '--log', metavar='LEVEL', help='logging level',
    choices=list('12345'), default=2, # INFO default
)

def parse_args(args):
    return parser.parse_args(args=args)
