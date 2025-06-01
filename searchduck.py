from duckduckgo_search import DDGS
import asyncio 

def search(query, max_results=3):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        links = [{"title": r["title"], "url": r["href"]} for r in results]
        print(links) 
        return links


