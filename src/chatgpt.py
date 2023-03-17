import openai
import os
import sys


openai.key = os.environ['OPENAI_API_KEY']


def get_completion(prompt: str) -> str:
    prompt_message = {'role': 'user', 'content': prompt}
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[prompt_message],
        temperature=0.0,
        max_tokens=1000,
    )

    return completion.choices[0].message.content


if __name__ == '__main__':
    print(get_completion(sys.argv[1]))
