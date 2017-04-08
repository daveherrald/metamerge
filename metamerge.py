#!/usr/bin/env python2.7

import getopt
import sys
import re
import collections

def usage():
    print "usage: metamerge.py [-h] -l <local.meta> -d <default.meta> -o <output_file> "
    print "    -l: the local.meta file to be merged into the output file. This file is not modified."
    print "    -d: the default.meta file to be merged into the output file. This file is not modified."
    print "    -o: the output file which will contain the merged results. If the file exists it will be overwritten without warning."
    print "    -h print this message and exit"

def process_meta(meta_file, output_dict):

	header_regex = re.compile('^(\[.*\]).*$')
	non_header_regex = re.compile('^(.+) =')
	empty_line_regex = re.compile('^\s*$')
	
	header = ''

	for line in meta_file.readlines():
		line = line.rstrip()
		m = ''
		n = ''
		o = ''
	
		o = empty_line_regex.match(line)
		if o:
			next
	
		m = header_regex.match (line)
		if m:
			header = m.group(1)
			if header not in output_dict:
				output_dict[header] = collections.OrderedDict()		
			next
	
		n = non_header_regex.match(line)
		if n:
			output_dict[header][n.group(1)] = line

try:
   opts, args = getopt.getopt(sys.argv[1:],"l:d:o:h")
except getopt.GetoptError:
    usage()
    sys.exit(1)

local_meta_fname = ''
default_meta_fname = ''
output_meta_fname = ''

for opt, arg in opts:
    if opt == '-h':
        usage()       
        sys.exit()
    elif opt == '-l':
        local_meta_fname = arg
    elif opt == '-d':
        default_meta_fname = arg
    elif opt == '-o':
        output_meta_fname = arg

if (local_meta_fname == '' or default_meta_fname == '' or output_meta_fname == ''):
	usage()
	sys.exit(1)

default_meta = open(default_meta_fname, "r")
local_meta   = open(local_meta_fname, "r")

output_dict = collections.OrderedDict()

process_meta (default_meta, output_dict)
process_meta (local_meta, output_dict)

default_meta.close()
local_meta.close()

output_meta  = open(output_meta_fname, "w")

for stanza_header in output_dict:
	output_meta.write(stanza_header + "\n")
	for element in output_dict[stanza_header]:
		output_meta.write(output_dict[stanza_header][element] + "\n")
	output_meta.write("\n")

output_meta.close()
