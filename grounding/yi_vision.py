

def yi_vision_api(PROMPT='帮我把红色方块放在钢笔上', img_path='temp/vl_now.jpg'):
    '''
    零一万物大模型开放平台，yi-vision视觉语言多模态大模型API
    '''

    client = OpenAI(
        api_key=YI_KEY,
        base_url="https://api.lingyiwanwu.com/v1"
    )

    # 编码为base64数据
    with open(img_path, 'rb') as image_file:
        image = 'data:image/jpeg;base64,' + base64.b64encode(image_file.read()).decode('utf-8')

    # 向大模型发起请求
    completion = client.chat.completions.create(
        model="yi-vision",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT + PROMPT
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image
                        }
                    }
                ]
            },
        ]
    )

    # 解析大模型返回结果
    result = eval(completion.choices[0].message.content.strip())
    print('    大模型调用成功！')

    return result