import grongier.pex
import iris

class EmailOperation(grongier.pex.BusinessOperation):

    def getAdapterType():
        """
        Name of the registred adaptor
        """
        return "EnsLib.EMail.OutboundAdapter"

    def OnMessage(self, pRequest):

        mailMessage = iris.cls("%Net.MailMessage")._New()
        mailMessage.Subject = pRequest.Found+" found"
        self.Adapter.AddRecipients(mailMessage,pRequest.ToEmailAddress)
        mailMessage.Charset="UTF-8"

        title = author = url = ""
        if (pRequest.Post is not None) :
            title = pRequest.Post.title
            author = pRequest.Post.author
            url = pRequest.Post.url
        
        mailMessage.TextData.WriteLine("More info:")
        mailMessage.TextData.WriteLine("Title: "+title)
        mailMessage.TextData.WriteLine("Author: "+author)
        mailMessage.TextData.WriteLine("URL: "+url)

        return self.Adapter.SendMail(mailMessage)
