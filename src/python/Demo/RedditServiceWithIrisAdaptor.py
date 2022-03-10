import iris
import grongier.pex

class RedditService(grongier.pex.BusinessService):

    def getAdapterType():
        """
        Name of the registred adaptor
        """
        return "dc.Reddit.InboundAdapter"

    def OnProcessInput(self, messageInput):
        msg = iris.cls("dc.Demo.PostMessage")._New()
        msg.Post = messageInput
        return self.SendRequestSync("FilterPosts",msg)
