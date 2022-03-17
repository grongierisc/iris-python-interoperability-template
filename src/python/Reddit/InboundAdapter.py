import grongier.pex
import requests
import iris
import json

class RedditInboundAdapter(grongier.pex.InboundAdapter):
    
    def OnInit(self):
        
        self.Feed = "/new/"
        self.Limit = str(10)
        
        self.LastPostName = ""
        
        return 1

    def OnTask(self):
        self.LOGINFO(f"LIMIT:{self.Limit}")
        if self.Feed == "" :
            return 1
        
        tSC = 1
        # HTTP Request
        try:
            server = "https://www.reddit.com"
            requestString = self.Feed+".json?before="+self.LastPostName+"&limit="+self.Limit
            self.LOGINFO(server+requestString)
            response = requests.get(server+requestString)
            response.raise_for_status()

            data = response.json()
            updateLast = 0

            for key, value in enumerate(data['data']['children']):
                if value['data']['selftext']=="":
                    continue
                post = iris.cls('dc.Reddit.Post')._New()
                post._JSONImport(json.dumps(value['data']))
                post.OriginalJSON = json.dumps(value)
                if not updateLast:
                    self.LastPostName = value['data']['name']
                    updateLast = 1
                response = self.BusinessHost.OnProcessInput(post)
                
        except Exception as e: 
            self.LOGINFO(e.__str__())
            raise e

        return tSC