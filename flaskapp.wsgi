#!/usr/bin/python3
import sys


sys.path.insert(0, "/var/www/Resume/")

from web import app as application
from web import ENV
application.secret_key = ENV["secret_key"]
