import grongier.pex
import iris

from PostMessage import PostMessage

class FilterPostRoutingRule(grongier.pex.BusinessProcess):
    
    def OnInit(self):
        return

    def OnTearDown(self):
        return

    def OnRequest(self, request: PostMessage):
        if 'dog'.upper() in request.Post.Selftext.upper():
            request.ToEmailAddress = 'dog@company.com'
            request.Found = 'Dog'
            self.SendRequestAsync("dc.Demo.FileOperation",request)
        if 'cat'.upper() in request.Post.Selftext.upper():
            request.ToEmailAddress = 'cat@company.com'
            request.Found = 'Cat'
            self.SendRequestAsync("dc.Demo.FileOperation",request)
        return 

    def OnResponse(self, request, response, callRequest, callResponse, pCompletionKey):
        return response

    def OnComplete(self, request, response):
        return response