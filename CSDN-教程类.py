#!/usr/bin/python3
# -- coding: utf-8 --
# @Date  : 2024/11/23
# @Name  : ZhouZongXin

"""

"""
import os
import requests
from openai import OpenAI
import time
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

api_key = os.getenv('api_key')
cadn_data = {
    "综合": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&type=",
    ],
    "人工智能": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&type=",
    ],
    "前沿技术": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF&type=",
    ],
    "Python": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=python&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=python&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=python&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=python&type=",
    ],
    "大数据": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=%E5%A4%A7%E6%95%B0%E6%8D%AE&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=%E5%A4%A7%E6%95%B0%E6%8D%AE&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=%E5%A4%A7%E6%95%B0%E6%8D%AE&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=%E5%A4%A7%E6%95%B0%E6%8D%AE&type=",
    ],
    "开发工具": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7&type=",
    ],
    "JS": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=javascript&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=javascript&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=javascript&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=javascript&type=",
    ],
    "C++": [
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=0&pageSize=25&child_channel=c%2Fc%2B%2B&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=1&pageSize=25&child_channel=c%2Fc%2B%2B&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=2&pageSize=25&child_channel=c%2Fc%2B%2B&type=",
        "https://blog.csdn.net/phoenix/web/blog/hot-rank?page=3&pageSize=25&child_channel=c%2Fc%2B%2B&type="
    ]
}

dict_data = []


# 抓取数据函数
def fetch_hot_rank(URL):
    csdn_hot_rank_url = URL

    for csdn_url in csdn_hot_rank_url:
        print("正在获取当前榜单数据...", csdn_url)
        time.sleep(1)
        try:
            headers = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Charset": "utf-8"
            }
            # 发送请求
            response = requests.get(csdn_url, headers=headers, timeout=10)
            response.raise_for_status()

            # 解析响应
            data = response.json()

            # 筛选并打印所需数据
            if data["code"] == 200:
                for entry in data["data"]:
                    nick_name = entry.get("nickName", "N/A")
                    article_title = entry.get("articleTitle", "N/A")
                    pc_hot_rank_score = entry.get("pcHotRankScore", "N/A")
                    data_csdn = f"作者: {nick_name}, 文章名: {article_title}, 当前热度值: {pc_hot_rank_score}"
                    dict_data.append(data_csdn)

            else:
                print("Failed to fetch data. Server responded with error.")

        except requests.RequestException as e:
            print(f"Request failed: {e}")


def GPT_data():
    user_content = f"""
你是一位资深的热点分析专家。请根据我提供的以下数据，完成以下任务：

1、帮我分析出内容中的热点热词,并且根据热词生成新的文章标题,标题最好包含入门,教程,详细,详解,超详细等类型关键词.注意文章的标题要结合SEO,能够登上热点的标题
2、并且每个标题下面给出文章的内容方向.
3、生成15条

请确保分析结果详尽且具有可操作性。以下是需要分析的数据：


{dict_data}
        """

    print("获取数据的总数: ", len(dict_data))
    print()
    client = OpenAI(
        api_key=api_key,
        base_url="https://testchatmoss.aihao123.cn/luomacode-api/open-api/v1"
    )
    response = client.chat.completions.create(
        messages=[
            {'role': 'user', 'content': user_content}, ],
        model='gpt-4o-mini',
        stream=False
    )

    # print(response.choices[0].message.content)
    with open('output.md', 'a', encoding='utf-8') as file:
        file.write(response.choices[0].message.content)
   

    print("字符串已成功写入文件。")
    # for chunk in response:
    #     print(chunk.choices[0].delta.content, end="", flush=True)


# 主函数
if __name__ == "__main__":
    # CSDN人工智能热榜

    # 综合、人工智能、前沿技术、Python、大数据、开发工具、JS、C++
    URL = cadn_data['前沿技术']

    fetch_hot_rank(URL)
    time.sleep(1)
    GPT_data()

