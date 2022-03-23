import grongier.pex
import datetime
import os
import iris

class FileOperation(grongier.pex.BusinessOperation):

    def OnInit(self):
        if hasattr(self,'Path'):
            os.chdir(self.Path)

    def OnMessage(self, pRequest):
        
        ts = title = author = url = text = ""

        if (pRequest.Post is not None):
            title = pRequest.Post.Title
            author = pRequest.Post.Author
            url = pRequest.Post.Url
            text = pRequest.Post.Selftext
            ts = datetime.datetime.fromtimestamp(pRequest.Post.CreatedUTC).__str__()

        line = ts+" : "+title+" : "+author+" : "+url
        filename = pRequest.Found+".txt" 

        self.PutLine(filename, line)
        self.PutLine(filename, "")
        self.PutLine(filename, text)
        self.PutLine(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return iris.cls('Ens.StringResponse')._New("hello")


    @staticmethod
    def PutLine(filename,string):
        try:
            with open(filename, "a",encoding="utf-8") as outfile:
                outfile.write(string)
        except Exception as e:
            raise e