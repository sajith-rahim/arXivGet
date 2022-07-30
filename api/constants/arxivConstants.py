ARXIV_HEADER = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept-Language": "en-US,en;q=0.9",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Windows",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "http://www.google.com",
    "Upgrade-Insecure-Requests": "1",
    "sec-ch-ua": '"Google Chrome";v="103", "Chromium";v="103"',
}

ARXIV_SEARCH_URI = "https://arxiv.org/search/"

ARXIV_DEFAULT_PARAMS = (
    ("searchtype", "all"),
    ("query", "Machine Learning"),
    ("abstracts", "show"),
    ("size", str(100)),
    ("order", ""),  # ("order","-announced_date_first")
    ("start", str(0)),
)
