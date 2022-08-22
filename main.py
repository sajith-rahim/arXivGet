from api import arxiv
from api.arxiv import ArxivAPI

if __name__ == '__main__':
    api = ArxivAPI()
    res = api.fetch(query="Diffusion", page_size=200, page=0)
    print(res)
