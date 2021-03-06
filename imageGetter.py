import requests
from bs4 import BeautifulSoup
import urlparse



url = "https://www.walmart.com/ip/54649026"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
images = []

    # This will look for a meta tag with the og:image property
og_image = (soup.find('meta', property='og:image') or
soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
        #print og_image['content']
        #print ''
    images.append(og_image['content'])

    # This will look for a link tag with a rel attribute set to 'image_src'
thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
        # print thumbnail_spec['href']
        # print ''
    images.append(thumbnail_spec['href'])


    #image = """<img src="%s"><br />"""
for img in soup.findAll("img", src=True):
    if img["src"] not in images:
        images.append(img["src"] + "\n")
        
imgs= '\n'.join(images)
print imgs
