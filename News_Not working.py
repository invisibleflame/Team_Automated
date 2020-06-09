from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='003b0b68b79b4fa79ca02a7063c9b46f')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin')
# /v2/sources
sources = newsapi.get_sources()
