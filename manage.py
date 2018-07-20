from core.lib.crud import create
from core.lib.crud import _compile
from core.views import index as gui

import argparse
import sys


version = '1.0.0-alpha.2'


parser = argparse.ArgumentParser()
parser.add_argument('task')

args = parser.parse_args()

if args.task == 'version' or args.task == 'v':
    print('Remarkable: v'+version)
    print('Python: v'+sys.version)

elif args.task == 'start' or args.task == 'open':
    gui.index()

elif 'compile=' in args.task:
    project = args.task.split('compile=')[1]
    _compile.compile(project)

elif 'create=' in args.task:
    project = args.task.split('create=')[1]
    create.project(project)