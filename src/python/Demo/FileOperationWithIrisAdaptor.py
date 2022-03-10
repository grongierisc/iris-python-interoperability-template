import iris
import grongier.pex

class FileOperation(grongier.pex.BusinessOperation):

    def getAdapterType():
        """
        Name of the registred adaptor
        """
        return "EnsLib.File.OutboundAdapter"

    def OnMessage(self, pRequest):

        ts = title = author = url = text = ""

        if (pRequest.Post != ""):
            title = pRequest.Post.Title
            author = pRequest.Post.Author
            url = pRequest.Post.Url
            text = pRequest.Post.Selftext
            ts = iris.cls("%Library.PosixTime").LogicalToOdbc(iris.cls("%Library.PosixTime").UnixTimeToLogical(pRequest.Post.CreatedUTC))
        line = ts+" : "+title+" : "+author+" : "+url
        filename = pRequest.Found+".txt" 
        self.Adapter.PutLine(filename, line)
        self.Adapter.PutLine(filename, "")
        self.Adapter.PutLine(filename, text)
        self.Adapter.PutLine(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return 1
