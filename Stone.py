
class Token():
    EOL = "//n"
    EOL = "//ALL"
    def __init__(self) -> None:
        self.lineNumber = 0

        pass

    def Token(self,line:int):
        self.lineNumber = line

    def isIdentifier(self):
        return False

    def isNumber(self):
        return False
    def isString(self):
        return False

    def getNumber(self):
        print('not number token')

    def getText(self):
        return ""

class Lexer():
    regexPat = ""

    def __init__(self):
        self.pattern = None #Pattern()
        self.queue = [] #token class array
        self.hasMore = False # bool
        self.reader # LineNumberReader()

    def Lexer(self,r):

        # r:Reader()
        self.hasMore = True
        self.reader = LineNumberReader(r)
    
    def reader(self):
        # todo:except
        if(self.fillQueue(0)):
            return self.queue.remove(0)
        else:
            return Token.EOF

    def peek(self,i):
        # todo:except
        if(self.fillQueue(i)):
            return self.queue.get(i)
        else:
            return Token.EOF

    def fillQueue(self,i):
        while i>= self.queue.__len__():
            if self.hasMore:
                self.readLine()
            else:
                return False
        return True
    
    def readLine(self):
        line = ""
        try:
            line = self.reader.readerLine()
        except:
            pass
            # todo: excpt

        lineNo = self.reader.getLineNumber()
        matcher = self.pattern.match(line)
        matcher.useTransparentBounds(True).useAnchoringBounds(False)
        pos = 0
        endPos = line.__len__()
        while pos<endPos:
            matcher.region(pos,endPos)
            if(matcher.lookingAt()):
                addToken(lineNo,matcher)
                pos = matcher.end()

            else:
                print('bad toiken at line' + str(lineNo))
            queue.add(new IdToken(lineNo,Token.EOL ))

