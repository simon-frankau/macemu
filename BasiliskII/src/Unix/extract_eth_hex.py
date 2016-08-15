from __future__ import absolute_import, division, print_function, unicode_literals
import sys
from optparse import OptionParser

if 2 == sys.version_info[0]:
    text = unicode
else:
    text = str

parser = OptionParser()
parser.add_option("-i", action="store", dest="input")
parser.add_option("-o", action="store", dest="output")

(options, args) = parser.parse_args()

with open(options.input, 'r') as log_file:
    line_list = log_file.read().splitlines()
    dump_list = list()
    should_store_next = False
    for line in line_list:
        if should_store_next:
            dump_list.append(line)
            should_store_next = False
        if line == 'Receiving Ethernet packet:' or line == 'Sending Ethernet packet:':
            should_store_next = True

dump_space_sep_string = ' '.join(dump_list)
dump_space_sep_list = dump_space_sep_string.split(' ')

print('totoal packets: ' + text(len(dump_list)))

with open(options.output, 'w') as hex_dump:
    for packet_string in dump_list:
        dump_space_sep_list = packet_string.split(' ')
        offset = 0
        end_offset = 0
        split_by = 8
        for hex_string in dump_space_sep_list:
            if offset % split_by == 0:
                hex_dump.write(format(offset, '08x') + ' ')
                end_offset = offset + split_by
            offset += 1
            if offset == end_offset:
                hex_dump.write(hex_string)
                hex_dump.write('\n')
            else:
                hex_dump.write(hex_string + ' ')
        hex_dump.write('\n')

print('hex dump conversion done!')
