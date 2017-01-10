#!/usr/bin/env python

# OpenDKIM key rotator
# (c) 2017 Michael Hinz (@flinkflonk)

# parse command line options
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
