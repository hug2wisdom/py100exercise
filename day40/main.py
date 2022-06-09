import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pypushdeer import PushDeer
import time

MY_PUSH_KEY = "PDU11936TjsyL4roS5UjoTHZPecvFZcmgr9fmtgAE"
hack_news_endpoint = "https://hn.buzzing.cc/"
response = requests.get(url=hack_news_endpoint)
response.raise_for_status()
data_html = response.text
contents = BeautifulSoup(data_html, "html.parser")
# spans = contents.find_all(name="span", class_="css-iw9df2")
# 使用 css 选择器方法
spans = contents.select("div.css-1brhwtr span.css-iw9df2")
nums = [int(span.getText()) for span in spans]
max_index = nums.index(max(nums))

links = contents.find_all(name="a", attrs={"data-test": "item-title"})
info_list = [{"article_title": link.find(name="h3").getText(), "article_link": link.get("href")} for link in links]
sent_news_info = f"{time.strftime('%Y-%m-%d', time.localtime())}要闻:\n" \
                 f"标题是:{info_list[max_index]['article_title']}\n" \
                 f"点赞数是:{max(nums)}\n" \
                 f"链接是:{info_list[max_index]['article_link']}\n"
# print(sent_news_info)
pushdeer = PushDeer(pushkey=MY_PUSH_KEY)
pushdeer.send_text(sent_news_info, desp="my news")
pushdeer.send_text(f"{info_list[max_index]['article_link']}", desp="the news link")
