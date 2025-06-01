import asyncio
from webscrape import transform
from searchduck import search
from Rag import add_docs, retrieve
from langchain.schema import Document

async def test_all():
    
    query = "who is prime minister of india"
    print(f"Searching for: {query}")
    search_results = search(query)
    print(f"Search returned {len(search_results)} results:")
    for res in search_results:
        print(res)

    if search_results:
        url = search_results[0]["url"]
        print(f"\nTransforming URL: {url}")
        docs = await transform(url)  
         
        print(f"Transformed into {len(docs)} documents.")

        
        add_docs(docs)

        
        retrieval_query = "Who is primeminister of india"
        print(f"\nRetrieving docs for query: '{retrieval_query}'")
        retrieved_text = retrieve(retrieval_query)
        print("Retrieved text:\n", retrieved_text)
    else:
        print("No search results to test transform.")


asyncio.run(test_all())
