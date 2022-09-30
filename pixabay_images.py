import requests
import key

# Input from the user
name = input("Enter images you want to download: ")

# Accessing API from Pixabay for 200 images
url = f'https://pixabay.com/api/?key={key.api_key}&q={name}&image_type=photo&per_page=200'

# Requests URL
request = requests.get(url)

# Getting JSON Data
json_data = request.json()

# Looping the hits array in API
for image in json_data['hits']:
    name = image['id']
    img_url = image['largeImageURL']
    r = requests.get(img_url, stream=True)

    # Downloading multiple files in current folder
    with open(str(name) + '.jpg', 'wb') as f:
        f.write(r.content)
