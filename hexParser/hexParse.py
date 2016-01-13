import pdb
class LineParse:
    location_dataLen_start = 1
    location_dataLen_end = 3
    location_dataAddr_start = 3
    location_dataAddr_end = 7
    location_dataType_start = 7
    location_dataType_end = 9
    location_data_start = 9
    def __init__(self):
        pass
    def getDataType(self):
        return self.dataType

    def getDataLength(self):
        return self.dataLen

    def getDataContent(self):
        return self.dataContent

    def getDataAddr(self):
        return self.dataAddr

    def parse(self, value):
        self.dataType = value[LineParse.location_dataType_start:LineParse.location_dataType_end]
        self.dataLen = int(value[LineParse.location_dataLen_start:LineParse.location_dataLen_end], 16)
        self.dataAddr = int(value[LineParse.location_dataAddr_start:LineParse.location_dataAddr_end], 16)
        self.dataContent = value[LineParse.location_data_start:LineParse.location_data_start + self.dataLen * 2]

    def __del__(self):
        pass

class Segment:
    def __init__(self, startAddr):
        self.startAddr = startAddr
        self.content = ''
    def addToContent(self, value):
        self.content = self.content + value

    def getContent(self):
        return self.content

    def __del__(self):
        pass

class HexParse:
    CONSTANT_DATA = '00'
    CONSTANT_START_ADDR = '04'
    CONSTANT_ENTRY_ADDR = '05'
    CONSTANT_END = '01'

    def __init__(self, fileName):
        self.fileName = fileName
        self.f = open(self.fileName, 'r')
        self.result = []

    def parse(self):
        parse = LineParse()
        segLineCnt = 0
        segAddr = 0
        for line in self.f.readlines():
            parse.parse(line)
            if parse.getDataType() == HexParse.CONSTANT_START_ADDR:
                segment = Segment(int(parse.getDataContent(), 16))
                self.result.append(segment)

                segLineCnt = 0
                segAddr = 0
            if parse.getDataType() == HexParse.CONSTANT_DATA:
                segLineCnt = segLineCnt + 1
                if segLineCnt == 1:
                    segAddr = parse.getDataAddr()
                    self.result[-1].addToContent(parse.getDataContent())
                    segAddr = segAddr + parse.getDataLength()
                else :
                    if segAddr < parse.getDataAddr():
                        segment.addToContent('00' * (parse.getDataAddr() - segAddr))
                        segAddr = parse.getDataAddr()
                    self.result[-1].addToContent(parse.getDataContent())
                    segAddr = segAddr + parse.getDataLength()

            if parse.getDataType() == HexParse.CONSTANT_ENTRY_ADDR:
                entryAddr = parse.getDataContent()

            if parse.getDataType() == HexParse.CONSTANT_END:
                pass

    def getResult(self):
        return self.result

    def __del__(self):
        pass


if __name__ == '__main__':
    parse = HexParse('socTest.hex')
    parse.parse()

    for s in parse.getResult():
        for x in range(0, len(s.getContent()), 32):
            print s.getContent()[x:x+32]
        print
        print
