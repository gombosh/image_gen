import openai
import os
openai.api_key = os.getenv("MY_OPENAI_API")
response = openai.Image.create(
  prompt="photorealistic onion that looks like a barbie doll",
  n=4,
  size="256x256"
)
for image in response['data']:
    image_url = image['url']
    print(image_url)