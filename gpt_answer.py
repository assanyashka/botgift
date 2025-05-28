from g4f.client import Client
import config

def generate(query):
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": f"{config.GPT_PROMPT + query}"}],
            web_search=False
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Ошибка при обработке текста через g4f: {e}")
        return None
