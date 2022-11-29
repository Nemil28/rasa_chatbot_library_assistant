import urllib.request as libreq
import feedparser

def paper(subject):

    link = ("http://export.arxiv.org/api/query?search_query=all:" + subject + "&start=0&max_results=2")
    
    with libreq.urlopen(link) as url:
        r = url.read()

    feed = feedparser.parse(r)

    a = []

    for entry in feed.entries:
        a.append(entry.title.replace('\n', '').replace('  ', ''))

#    print(a)
    return a