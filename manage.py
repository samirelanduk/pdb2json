#!/usr/bin/env python
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pdb2json")
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
