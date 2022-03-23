import grongier.pex
import iris

from PostMessage import PostMessage

class FilterPostRoutingRule(grongier.pex.BusinessProcess):
    
    def OnInit(self):
        
        if not hasattr(self,'Target'):
            self.Target = "Python.FileOperation"
        
        return 1

    def OnTearDown(self):
        return

    def OnRequest(self, request: PostMessage):
        if 'dog'.upper() in request.Post.Selftext.upper():
            request.ToEmailAddress = 'dog@company.com'
            request.Found = 'Dog'
            self.SendRequestAsync(self.Target,request)
        if 'cat'.upper() in request.Post.Selftext.upper():
            request.ToEmailAddress = 'cat@company.com'
            request.Found = 'Cat'
            self.SendRequestAsync(self.Target,request)
        return 

    def OnResponse(self, request, response, callRequest, callResponse, pCompletionKey):
        return response

    def OnComplete(self, request, response):
        return response