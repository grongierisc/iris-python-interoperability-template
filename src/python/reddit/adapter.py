from grongier.pex import InboundAdapter
import requests
import iris
import json

class RedditInboundAdapter(InboundAdapter):
    
    def on_init(self):
        
        if not hasattr(self,'feed'):
            self.feed = "/new/"
        
        if self.limit is None:
            raise TypeError('no Limit field')
        
        self.last_post_name = ""
        
        return 1

    def on_task(self):
        self.LOGINFO(f"LIMIT:{self.limit}")
        if self.feed == "" :
            return 1
        
        tSC = 1
        # HTTP Request
        try:
            server = "https://www.reddit.com"
            request_string = self.feed+".json?before="+self.last_post_name+"&limit="+self.limit
            self.log_info(server+request_string)
            response = requests.get(server+request_string)
            response.raise_for_status()

            data = response.json()
            updateLast = 0

            for key, value in enumerate(data['data']['children']):
                if value['data']['selftext']=="":
                    continue
                post = iris.cls('dc.Reddit.post')._New()
                post._JSONImport(json.dumps(value['data']))
                post.original_json = json.dumps(value)
                if not updateLast:
                    self.LastpostName = value['data']['name']
                    updateLast = 1
                response = self.BusinessHost.ProcessInput(post)
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:
                self.log_warning(err.__str__())
            else:
                raise err
        except Exception as err: 
            self.log_error(err.__str__())
            raise err

        return tSC