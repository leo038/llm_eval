from api_key import OPENAI_API_KEY
import os
from openai import OpenAI
from utils import encode_image

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


def gpt4_grounding(text_prompt="What’s in this image?", input_image=None):
    client = OpenAI()

    base64_image = encode_image(image_path=input_image)
    model = "gpt-4o-mini"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": text_prompt
                     },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    res = response.choices[0].message.content
    print(f"model: {model}, text_prompt:{text_prompt}, input_image: {input_image},output: {res}")
    return res


if __name__ == "__main__":
    gpt4_grounding(text_prompt="从这张图中找到小狗的左上角和右下角的像素坐标，输出如下格式的结果：[[102,505],[324,860]]",
                   input_image="image/dog_and_girl.jpeg")

"""
模型输出： 


gpt4o-mini:  抱歉，我无法处理该请求。
gpt4o-mini:  第二次运行输出：抱歉，我无法处理图片内容以提取特定像素坐标。
gpt4o:  [[262, 222], [657, 683]]
gpt4o: 第二次运行输出：  对于这张图片，假设其大小是标准的1920x1080像素，则可以估算小狗的左上角和右下角的坐标大致如下：

- 左上角：[350, 400]
- 右下角：[750, 820]

输出格式如下：
[[350, 400], [750, 820]]

可视化之后发现2次输出结果都偏离比较大


"""
