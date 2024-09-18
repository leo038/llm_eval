from openai import OpenAI

from api_key import YI_API_KEY
from utils import encode_image

API_BASE = "https://api.lingyiwanwu.com/v1"
API_KEY = YI_API_KEY


def yi_vision_grounding(text_prompt="What’s in this image?", input_image=None):
    client = OpenAI(
        api_key=API_KEY,
        base_url=API_BASE
    )

    model = "yi-vision"

    base64_image = encode_image(image_path=input_image)

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
    yi_vision_grounding(text_prompt="从这张图中找到小狗的左上角和右下角的像素坐标，输出如下格式的结果：[[102,505],[324,860]]",
                   input_image="image/dog_and_girl.jpeg")


"""
输出：
[[102, 505], [324, 860]]
[[236, 405], [506, 853]]
[[224, 427], [534, 842]]
[[243, 416], [509, 860]]
"""