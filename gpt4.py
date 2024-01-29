from openai import OpenAI
import requests

def generate_dalle_image(api_key, user_prompt):
    fixed_prompt = """
    I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:
    """
    full_prompt = fixed_prompt + "\n" + user_prompt
    client = OpenAI(api_key=api_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=full_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    if response and response.data:
        image_url = response.data[0].url
        return image_url
    else:
        return "Image generation failed."

api_key = ""
user_prompt = input("Enter your image prompt: ")

image_url = generate_dalle_image(api_key, user_prompt)
print("Image URL:", image_url)
