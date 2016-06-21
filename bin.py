#! /usr/bin/python

import sys

def btransfor(byte):
    if ord(byte) < 16:
        return '0'+ hex(ord(byte))[2:]
    return hex(ord(byte))[2:]

def wtransfor(word):
    return btransfor(word[3]) + btransfor(word[2]) + btransfor(word[1]) + btransfor(word[0])

def usage():
    print 'python bin.py <inputFile>  <startAddress>   <byteCount>   <outputFile>(optional)'

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "invalid args"
        usage()
        exit(1)
    outputFile = ''
    if len(sys.argv) > 4:
        outputFile = sys.argv[4]
    fileName = sys.argv[1] 
    start = int(sys.argv[2], 16)
    count = int(sys.argv[3], 16)
    content = open(fileName).read()[start:(start + count)]
    tmp = [content[i * 4:i * 4 + 4] for i in range(len(content) / 4)]
    result = ',\r\n'.join(['0x' + wtransfor(x) for x in tmp]) + ','

    if outputFile:
        open(outputFile, 'w').write(result)
        exit(0)
    print result
