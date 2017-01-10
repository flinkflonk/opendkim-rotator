#!/usr/bin/env python

# OpenDKIM key rotator
# (c) 2017 Michael Hinz (@flinkflonk)

# predefined paths:
# /etc/opendkim.conf - configuration file for OpenDKIM
#   all info on other files comes from this configuration file,
#   so make sure it exists and is valid. Getting OpenDKIM running
#   is not part of the instructions for opendkim-rotator.
# /var/cache/opendkim-rotator - path where the database resides

# parse command line options
# -t: test - setup test paths for opendkim and DB directories
# -d: DNS-backend
#   "nsd": nsd
#   "bind": bind
#   "txt": instructions in text format for manual configuration
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
