from openai import OpenAI
import os

client = OpenAI()

def generate_quiz(text):

    prompt = f"""
    Create 5 AP style multiple choice questions from these notes:

    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
