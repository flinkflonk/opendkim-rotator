#!/usr/bin/env python

# OpenDKIM key rotator
# (c) 2017 Michael Hinz (@flinkflonk)

import os
import os.path
import sqlite3

# predefined paths:
# /etc/opendkim.conf - configuration file for OpenDKIM
#   all info on other files comes from this configuration file,
#   so make sure it exists and is valid. Getting OpenDKIM running
#   is not part of the instructions for opendkim-rotator.
# /var/cache/opendkim-rotator - path where the database resides
CONFIG_FILE = '/etc/opendkim.conf'
DB_PATH = '/var/cache/opendkim-rotator'

# parse command line options
# -t: test - setup test paths for opendkim and DB directories
# -d: DNS-backend
#   "nsd": nsd
#   "bind": bind
#   "txt": instructions in text format for manual configuration

# for now, just use test data, this is later activated by the -t flag
CONFIG_FILE = './test/opendkim.conf'
DB_PATH = './test'

# if the config file doesn't exist, bail out
if not os.path.isfile(CONFIG_FILE):
  print "no config file found (expected file: %s)" % CONFIG_FILE
  exit(1)

# if the DB path doesn't exist, create it
if not os.path.isdir(DB_PATH):
  os.makedirs(DB_PATH)

# append the actual database filename
DB_PATH += '/db.sqlite3'

# if the DB doesn't exist, create it
if not os.path.isfile(DB_PATH):
  db = sqlite3.connect(DB_PATH)
  db.execute('''create table keys (created text, selector text(4), domain text, key text)''')
else:
  db = sqlite3.connect(DB_PATH)

# read config file

# read keyfile
# for each domain in file:
#   if domain doesn't exist in DB:
#     add to key/selector to DB with default values
#   create a new selector
#   create a new key
#   append the new selector/key to the keyfile
#   send info about the new selector/key to DNS
#   add new key/selector to DB
#   make previous key/selector the active one in SigningFile
# for each domain in DB:
#   for each key for that domain:
#     if key is older than threshold (three months?):
#       delete key from database
#       delete key from keyfile
# (eventually) reload nameserver
# (eventually) reload OpenDKIM
