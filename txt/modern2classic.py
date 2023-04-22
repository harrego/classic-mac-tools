#!/usr/bin/env python3

import argparse
import os.path

parser = argparse.ArgumentParser(
	description="Convert a modern macOS text file to a classic Mac OS text file."
)
parser.add_argument("input",
	type=str,
	help="modern file input"
)
parser.add_argument("output",
	type=str,
	help="classic file output"
)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

input_file_name = args.input
output_file_name = args.output

if not os.path.isfile(input_file_name):
	print(f"[error] file not found: {input_file_name}")
	exit(1)

total_bytes = 0
def write_i(byte):
	global total_bytes
	output_file.write(byte.to_bytes(1, byteorder="big"))
	total_bytes += 1

def write_c(char):
	global total_bytes
	output_file.write(ord(char).to_bytes(1, byteorder="big"))
	total_bytes += 1

post_file = open(input_file_name, "r")
content = post_file.read()
post_file.close()

if args.verbose:
	print(f"[info] writing to {output_file_name}")
with open(output_file_name, "wb") as output_file:

	for char in list(content):
		ascii_code = ord(char)
		if ascii_code >= 128:
			if ascii_code == 8201:
				write_c(" ")
			elif ascii_code == 8212:
				write_c("-")
			elif ascii_code == 8217:
				write_c("'")
			elif ascii_code == 8220 or ascii_code == 8221:
				write_c("\"")
			else:
				print(f"[warning] discarded unrecognized ascii character: {char} ({ascii_code})")
		else:
			if ascii_code == 0x0a:
				write_i(0x0d)
			else:
				write_c(char)
if args.verbose:
	print(f"[info] finished, wrote {total_bytes} bytes")
	
