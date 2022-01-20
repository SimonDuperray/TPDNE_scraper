import requests, shutil, time
from datetime import datetime

url_people = "https://thispersondoesnotexist.com/image"
url_miss = "https://www.thismissfrancedoesnotexist.com/assets/image"

def get_images(url, type, ntimes):
   print(f"=== {type} ===")
   for i in range(ntimes):
      req = requests.get(
         url,
         stream=True
      )
      print(f"{i+1}. Status Code:{req.status_code}")
      if type=="people":
         cat = "people"
      else:
         cat = "miss"
      buffer_name = "./images/"+str(cat)+"/"+str(cat)+str(int(datetime.timestamp(datetime.now())))+".png"
      with open(buffer_name, 'wb')  as outfile:
         shutil.copyfileobj(req.raw, outfile)
      if i==ntimes-1:
         print(f"=== end ===")
         break
      else:
         time.sleep(3)


def get_name(url):
   req = requests.get(url)
   print(req.status_code)
   print(req.headers)

get_name(
   url='https://gender-api.com/get?split=theresa%20miller&'
)

# get_images(
#    url=url_people,
#    type="people",
#    ntimes=20
# )

