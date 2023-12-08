import asyncio

from spider_rs import crawl

async def main():
    website = await crawl("https://jeffmendez.com")
    print(website.links)

asyncio.run(main())