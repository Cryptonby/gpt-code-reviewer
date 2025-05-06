import os
import openai

def get_diff():
    # Placeholder for actual git diff fetch logic
    return "diff --git a/example.py b/example.py..."

def format_prompt(diff):
    with open('config/prompt_template.txt', 'r') as f:
        template = f.read()
    return template.replace("{{diff}}", diff)

def review_pull_request():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    diff = get_diff()
    prompt = format_prompt(diff)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    print("Review Comments:\n", response.choices[0].message.content)
