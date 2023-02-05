# pip insatll openai

import openai

openai.api_key = "your api" # https://platform.openai.com/docs/guides/images/introduction

image = input("Enter the name to the image: ")

response = openai.Image.create(
    prompt = image, 
    n=1,
    size ='1024x1024'
)

image_url = response['data'][0]['url']
print(f'URl da imagem gerada: {image_url}')
