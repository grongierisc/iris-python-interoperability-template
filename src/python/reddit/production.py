from iop import Production

from bo import FileWriterOperation
from bp import KeywordRouterProcess
from bs import RedditFetchService

prod = Production("dc.Python.Production")

reddit_service = prod.service("RedditFetchService", RedditFetchService)
keyword_router = prod.process("KeywordRouterProcess", KeywordRouterProcess)
cat_writer = prod.operation("CatFileWriterOperation", FileWriterOperation)
dog_writer = prod.operation("DogFileWriterOperation", FileWriterOperation)

prod.connect(reddit_service.Router, keyword_router)
prod.connect(keyword_router.CatTarget, cat_writer)
prod.connect(keyword_router.DogTarget, dog_writer)
