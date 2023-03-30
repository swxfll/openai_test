import os

from flask import Flask, request
import openai
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
@cross_origin()
def hello_world():
    request_context = request.json

    problem = None

    try:
        problem = request_context["problem"]
    except KeyError:
        print("发生 KeyError 错误...")

    print(problem)

    # Set up the OpenAI API client
    openai.api_key = "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"

    # # Set up the model and prompt
    # model_engine = "text-davinci-003"
    # prompt = problem
    #
    # # Generate a response
    # completion = openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    #
    # response = completion.choices[0].text
    # # print(completion.choices[1].text)
    #
    # return response

    response = openai.Image.create(
        prompt=problem,
        n=2,
        size="1024x1024"
    )
    # image_url = response['data'][0]['url']

    list = []

    for item in response['data']:
        print("查询到以下图片", item['url'])
        list.append(item['url'])

    return list


if __name__ == '__main__':
    app.run()
