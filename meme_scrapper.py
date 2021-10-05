
import requests
from bs4 import BeautifulSoup


def extract_memes(topic):
    url = "https://www.memedroid.com/memes/tag/"+topic
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')
        memes = soup.find_all('div',{'class':'item-aux-container'})
        imgs = []
        for meme in memes:
            img = meme.find('img')['src']
            alt = meme.find('img')['alt'].replace(" ","")
            
            if img.startswith('http') and img.endswith('jpeg'):
                imgs.append({"image":img,"text":alt})
        if len(imgs)>0:
            for i in range(len(imgs)):
                r = requests.get(imgs[i]["image"])
                
                with open(f'downloads/{topic}--{imgs[i]["text"]}.jpeg','wb') as image:
                    image.write(r.content)
                print('Meme successfully downloaded!')
        else:
            print("No meme found for the topic you enter!")

        
    except:
        print("Error while downloading meme!")
        

topic = input("Enter which topic you want memes? ")

if topic:
    extract_memes(topic)
else:
    print("Make sure you add a topic for the meme")

