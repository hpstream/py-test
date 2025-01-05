#!/usr/bin/python3
# -- coding: utf-8 --
# @Date  : 2024/11/23
# @Name  : ZhouZongXin

"""

"""
import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

api_key = os.getenv('api_key')
# print(api_key)

def GPT_data():
    user_content = f"""
角色：你在CSDN上是专家级别的写手；
任务：通过我给你的内容，去帮我生成一篇符合微信公众号文章的内容，并且根据SEO规则帮我优化整体文案，让文章更符合公众号的搜索规则；

文章要求：
0、生成的标题，要爆款类型，不仅要符合内容的主题，还可以用数字、疑问句、名人名言等方式来设计标题。
1、开头具有吸引力，生成的样式可以是多变的。
2、可以根据文章内容，自主创新生成新的文章内容。
4、生成的内容一定是专家级别的文章内容。
5、字数不低于2000字。
6、在合适的时候加上少量的emoji
7、在文章结尾的时候要注意完整性和格式，除了文章内容外禁止输出其他无关内容。

语言规则： 1. 回答问题时，去除明显的AI生成特征。
2. 回答问题时，需要用自然的语气+口语化。
3. 回答问题时，适当使用第一人称。
4. 回答问题时，尽量使用主动语态，减少被动语句和副词，但是不能改变原意。
5. 回答问题时，要保证内容的完整性。

注意事项：
为了更好地体现文章的价值，写作时应注意以下几点：
‌选好主题‌：紧扣时代脉搏，关注社会热点，反映群众关切，同时要有独特视角。
‌结构清晰‌：采用倒金字塔式结构，将最重要的信息放在开头，层次分明。
‌用词精准‌：避免使用过多的形容词和修饰语，用最简洁的语言表达丰富信息，但是生成的内容要让读者有成长的意义。
        """

    print()
    client = OpenAI(
        api_key="sk-6fgh02rgtardh5grc1hjb1rstgiauva4ag69kv89j464mggn",
        base_url="https://testchatmoss.aihao123.cn/luomacode-api/open-api/v1"
    )
    response = client.chat.completions.create(
        messages=[
            {'role': 'user', 'content': user_content},{'role': 'user', 'content':f"""
**《Vue3表单处理入门教程：数据绑定与验证的详细解析》**
   - 内容方向：讲解如何在Vue3中处理表单，包括数据绑定、表单验证和提交的实现。
        """}, ],
        model='gpt-4o-mini',
        stream=False
    )

    # print(response.choices[0].message.content)
    with open('article.md', 'a', encoding='utf-8') as file:
        file.write(response.choices[0].message.content)
   

    print("字符串已成功写入文件。")
    # for chunk in response:
    #     print(chunk.choices[0].delta.content, end="", flush=True)


# 主函数
if __name__ == "__main__":
    
    GPT_data()

