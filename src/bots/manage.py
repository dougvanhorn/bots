#!/usr/bin/env python

from pathlib import Path
import importlib
import os
import sys

from django.core.management import execute_from_command_line

from bots import botsglobal
from bots import botsinit


SETTINGS_MODULE_PREFIX = 'bots.config.settings.'
CONFIG_FILENAME = Path('.django_settings_module')

# Get a fully qualified path for the config file.
# This will let us run manage from outside this directory.
project_root = Path(__file__).parent.parent.parent
config_file = project_root / CONFIG_FILENAME


def read_settings_module():
    settings_module = config_file.read_text()
    settings_module = settings_module.strip()
    return settings_module


def write_settings_module(module):
    config_file.write_text(module)


def prompt_settings_module():
    module = input("Settings Module {}".format(SETTINGS_MODULE_PREFIX))
    module = module.strip()
    return '{}{}'.format(SETTINGS_MODULE_PREFIX, module)


settings_module = ''
try:
    settings_module = read_settings_module()

# When we can't open the file, let's try to create one.
except IOError as e:
    settings_module = prompt_settings_module()
    write_settings_module(settings_module)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    botsinit.generalinit('config')
    #os.chdir(botsglobal.ini.get('directories', 'botspath'))
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
