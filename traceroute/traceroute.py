#! /bin/python

#http = "http://www.ip5.me/index.php"

import sys
import pdb


class HttpAddr:
    def __init__(self, http):
        self.http = http
        pass
    def getUrlData(self, ip):
        import urllib
        return urllib.urlencode({'s':ip, 'doit':'1'})

    def getHttp(self):
        return self.http

    def getResult(self, content):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content)
        addr = soup.find(id = 'ip_pos').contents[0]
        return addr

    def __del__(self):
        pass

class Traceroute:
    def __init__(self, url, http):
        import platform
        self.platform = platform.system()
        self.http = http
        self.result = []
        if self.platform == 'Darwin':
            self.cmd = 'traceroute -I ' + url
        elif self.platform == 'Linux':
            self.cmd = 'traceroute -I ' + url
        elif self.platform == 'Windows':
            self.cmd = 'traceroute -I ' + url

    def getIpLocation(self, ip):
        import urllib2
        httpObj = HttpAddr(self.http)
        content = urllib2.urlopen(httpObj.getHttp(), httpObj.getUrlData(ip)).read()
        addr = httpObj.getResult(content)
        return addr

    def getCmdResult(self):
        import os
        output = os.popen(self.cmd).read()
        if self.platform == 'Windows':
            output = output.split('\r\n')
        else :
            output = output.split('\n')
        return output
    def getResult(self):
        return self.result

    def traceroute(self):
        import re
        output = self.getCmdResult()
        i = 0
        for line in output:
            m = re.search(r'\((?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)', line)
            t = re.search(r'\((?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\)  *(?P<time>.*)', line)

            i += 1
            if m:
                ip = m.group('ip')
                addr = self.getIpLocation(ip)
                self.result.append('%-4s%-20s%-30s%s' % (i, ip, addr, t.group('time')))

    def __del__(self):
        pass

if __name__ == '__main__':
    http = "http://www.ip5.me/index.php"
    traceroute = Traceroute(sys.argv[1], http)
    traceroute.traceroute()
    for line in traceroute.getResult():
        print line
