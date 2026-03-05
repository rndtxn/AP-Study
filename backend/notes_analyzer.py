from openai import OpenAI

client = OpenAI()

def analyze_notes(notes):

    prompt = f"""
    Analyze these study notes.

    1. Highlight key concepts
    2. Summarize them
    3. Suggest 3 quiz questions

    Notes:
    {notes}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return {"analysis": response.choices[0].message.content}
