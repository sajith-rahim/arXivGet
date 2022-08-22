from bs4 import BeautifulSoup

from api.constants import arxivConstants as ARXIV

import requests
import pandas as pd


# https://arxiv.org/search/?query=spiking&searchtype=all&abstracts=show&order=-announced_date_first&size=50


class ArxivAPI:
    def __init__(self):
        self.headers = ARXIV.ARXIV_HEADER
        self.params = ARXIV.ARXIV_DEFAULT_PARAMS

    def getBS(self, params=ARXIV.ARXIV_DEFAULT_PARAMS):
        response = requests.get(
            "https://arxiv.org/search/", headers=self.headers, params=params
        )
        return BeautifulSoup(response.text, "html.parser")

    def crawl(self, bs):
        papers = []
        # < li class ="arxiv-result" >
        final_out = bs.find_all("li", {"class": "arxiv-result"})

        for paper in final_out:
            paper_meta = dict()
            title = paper.find("p", {"class": "title is-5 mathjax"}).text.strip()
            paper_link = paper.find("p", {"class": "list-title is-inline-block"}).find(
                "a", href=True
            )["href"]
            pdf_link = paper.find("p", {"class": "list-title is-inline-block"}).findAll(
                "a", href=True
            )[1]["href"]

            abstract = paper.find("p", {"class": "abstract mathjax"}).find("span",
                                                                           {"class": "abstract-full"}).text.strip()

            paper_meta["title"] = title
            paper_meta["link"] = paper_link
            paper_meta["pdf"] = pdf_link
            paper_meta["abstract"] = abstract

            papers.append(paper_meta)
            # final_result.append(temp_result)

        df = pd.DataFrame(papers)
        return df

    def fetch(self, query, page_size, page):
        params = (
            ("searchtype", "all"),
            ("query", query),
            ("abstracts", "show"),
            ("size", str(page_size)),
            ("order", ""),  # ("order","-announced_date_first")
            ("start", str(page)),
        )
        bs = self.getBS(params)
        return self.crawl(bs)


"""
<li class="arxiv-result">
<div class="is-marginless">
<p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2207.05006">arXiv:2207.05006</a>
<span> [<a href="https://arxiv.org/pdf/2207.05006">pdf</a>, <a href="https://arxiv.org/format/2207.05006">other</a>] </span>
</p>
<div class="tags is-inline-block">
<span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Robotics">cs.RO</span>
<span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Artificial Intelligence">cs.AI</span>
<span class="tag is-small search-hit tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
</div>
</div>
<p class="title is-5 mathjax">
      
        TASKOGRAPHY: Evaluating robot task planning over large 3D scene graphs
      
    </p>
<p class="authors">
<span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
<a href="/search/?searchtype=author&amp;query=Agia%2C+C">Christopher Agia</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Jatavallabhula%2C+K+M">Krishna Murthy Jatavallabhula</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Khodeir%2C+M">Mohamed Khodeir</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Miksik%2C+O">Ondrej Miksik</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Vineet%2C+V">Vibhav Vineet</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Mukadam%2C+M">Mustafa Mukadam</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Paull%2C+L">Liam Paull</a>, 
      
      <a href="/search/?searchtype=author&amp;query=Shkurti%2C+F">Florian Shkurti</a>
</p>
<p class="abstract mathjax">
<span class="has-text-black-bis has-text-weight-semibold">Abstract</span>:
      <span class="abstract-short has-text-grey-dark mathjax" id="2207.05006v1-abstract-short" style="display: inline;">
        …most benchmarking efforts in this area focus on vision-based planning, we systematically study symbolic planning, to decouple planning performance from visual representation <span class="search-hit mathjax">learning</span>. We observe that, among existing methods, neither classical nor…
        <a class="is-size-7" onclick="document.getElementById('2207.05006v1-abstract-full').style.display = 'inline'; document.getElementById('2207.05006v1-abstract-short').style.display = 'none';" style="white-space: nowrap;">▽ More</a>
</span>
<span class="abstract-full has-text-grey-dark mathjax" id="2207.05006v1-abstract-full" style="display: none;">
        3D scene graphs (3DSGs) are an emerging description; unifying symbolic, topological, and metric scene representations. However, typical 3DSGs contain hundreds of objects and symbols even for small environments; rendering task planning on the full graph impractical. We construct TASKOGRAPHY, the first large-scale robotic task planning benchmark over 3DSGs. While most benchmarking efforts in this area focus on vision-based planning, we systematically study symbolic planning, to decouple planning performance from visual representation <span class="search-hit mathjax">learning</span>. We observe that, among existing methods, neither classical nor <span class="search-hit mathjax">learning</span>-based planners are capable of real-time planning over full 3DSGs. Enabling real-time planning demands progress on both (a) sparsifying 3DSGs for tractable planning and (b) designing planners that better exploit 3DSG hierarchies. Towards the former goal, we propose SCRUB, a task-conditioned 3DSG sparsification method; enabling classical planners to match and in some cases surpass state-of-the-art <span class="search-hit mathjax">learning</span>-based planners. Towards the latter goal, we propose SEEK, a procedure enabling <span class="search-hit mathjax">learning</span>-based planners to exploit 3DSG structure, reducing the number of replanning queries required by current best approaches by an order of magnitude. We will open-source all code and baselines to spur further research along the intersections of robot task planning, <span class="search-hit mathjax">learning</span> and 3DSGs.
        <a class="is-size-7" onclick="document.getElementById('2207.05006v1-abstract-full').style.display = 'none'; document.getElementById('2207.05006v1-abstract-short').style.display = 'inline';" style="white-space: nowrap;">△ Less</a>
</span>
</p>
<p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 11 July, 2022; 
      <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> July 2022.
      
    </p>
<p class="comments is-size-7">
<span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
<span class="has-text-grey-dark mathjax">Video: https://www.youtube.com/watch?v=mM4v5hP4LdA&amp;ab_channel=KrishnaMurthy . Project page: https://taskography.github.io/ . 18 pages, 7 figures. In proceedings of Conference on Robot <span class="search-hit mathjax">Learning</span> (CoRL) 2021. The first two authors contributed equally</span>
</p>
<p class="comments is-size-7">
<span class="has-text-black-bis has-text-weight-semibold">ACM Class:</span>
          I.2.8; I.2.9; I.2.10; I.2.6
        
      </p>
<p class="comments is-size-7">
<span class="has-text-black-bis has-text-weight-semibold">Journal ref:</span>
        PMLR 164 (2022) 46-58
      </p>
</li>
"""
