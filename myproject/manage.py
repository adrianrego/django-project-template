#!/usr/bin/env python
import os
from django import get_version
from django.core.management import execute_from_command_line, LaxOptionParser
from django.core.management.base import BaseCommand

def has_settings_option():
    parser = LaxOptionParser(usage="%prog subcommand [options] [args]",
                             version=get_version(),
                             option_list=BaseCommand.option_list)
    try:
        options = parser.parse_args(sys.argv[:])[0]
    except:
        return False # Ignore any option errors at this point.
    return bool(options.settings)

if not has_settings_option() and not 'DJANGO_SETTINGS_MODULE' in os.environ:
    # Use local settings if other setting not passed in
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

execute_from_command_line()
