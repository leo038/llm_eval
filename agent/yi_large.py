import json

from openai import OpenAI

from api_key import YI_API_KEY

API_BASE = "https://api.lingyiwanwu.com/v1"
API_KEY = YI_API_KEY


def yi_large_react(text_prompt="hi"):
    client = OpenAI(
        api_key=API_KEY,
        base_url=API_BASE
    )

    model = "yi-large"

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": text_prompt,
            }
        ],
        max_tokens=3000,
    )

    res = response.choices[0].message.content

    print(f"model: {model}, text_prompt:{text_prompt},output: {res}")

    return res


if __name__ == "__main__":
    with open("./prompt/fever.json", 'r') as f:
        prompt = json.load(f)
    webthink_simple3_prompt = prompt.get("webthink_simple3")
    question = "Claim: Paramore is not from Tennessee."
    yi_large_react(text_prompt=webthink_simple3_prompt + question + "\n")

"""
Claim: Paramore is not from Tennessee.
output: Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Thought 1: I need to search Nikolaj Coster-Waldau and find if he has worked with the Fox Broadcasting Company.
Action 1: Search[Nikolaj Coster-Waldau]
Observation 1: Nikolaj William Coster-Waldau (born 27 July 1970) is a Danish actor and producer. He graduated from the Danish National School of Performing Arts in Copenhagen in 1993,[1] and had his breakthrough role in Denmark with the film Nightwatch (1994). He played Jaime Lannister in the HBO fantasy drama series Game of Thrones, for which he received two Primetime Emmy Award nominations for Outstanding Supporting Actor in a Drama Series.. Coster-Waldau has appeared in numerous films in his native Denmark and Scandinavia, including Headhunters (2011) and A Thousand Times Good Night (2013). In the U.S, his debut film role was in the war film Black Hawk Down (2001), playing Medal of Honor recipient Gary Gordon.[2] He then played a detective in the short-lived Fox television series New Amsterdam (2008), and appeared in the 2009 Fox television film Virtuality

"""
