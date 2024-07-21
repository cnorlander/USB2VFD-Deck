import feedparser

def get_top_posts(rss_url: str, number_of_posts: int = 10) -> str:
    feed = feedparser.parse(rss_url)
    top_posts = feed.entries[:number_of_posts]
    news_ticker = " --- ".join([f"{post.title}" for idx, post in enumerate(top_posts)])
    return news_ticker