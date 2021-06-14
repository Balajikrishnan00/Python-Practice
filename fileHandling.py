import os
class FileHandling:
    def __init__(self,fileName,fileMode):
        self.filename=fileName
        self.filemode=fileMode
        self.is_file=False
        self.line=self.word=self.char=0
    def LocateFile(self):
        if os.path.isfile(self.filename):
            self.is_file=True
    def FileLine(self):
        if self.is_file:
            with open(self.filename,self.filemode) as f:
                for l in f:

                    self.line+=1

                f.close()
                return self.line
        else:
            print('Pls Locate The File')
    def FileChar(self):
        if self.is_file:
            with open(self.filename, self.filemode) as f:
                list1=f.read()
                f.close()
                return len(list1)
        else:
            print('Plese Locate the File')
    def FileWord(self):
        if self.is_file:
            with open(self.filename, self.filemode) as f:
                data=f.readlines()
                for x in data:
                    self.word+=len(x.split())
                f.close()
                return self.word

file1=FileHandling('filedata','r')
#file1.FileLine()
file1.LocateFile()
line=file1.FileLine()
print(line)
char=file1.FileChar()
print(char)
word=file1.FileWord()
print(word)