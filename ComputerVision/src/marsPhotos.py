#Written by: Emma Davis
import json
import requests
import argparse

def getData(url, api_key, earth_date, camera, page):
  print('\nResponse:')

  apiRequest = url + '?earth_date=' + earth_date + '&api_key=' + api_key

  if camera is not None:
    apiRequest = apiRequest + '&camera=' + camera
  if page is not None:
    apiRequest = apiRequest + '&page=' + page

  print(apiRequest)
  print()
  response = requests.get(apiRequest)
  data = []
  data.append(response.json())
  print(data)

  return data

def readData(api_key, date, page, camera):
  url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos/'
  earth_date = date
  
  data = {}
  data = getData(url, api_key, earth_date, camera, page)

  felixFile = open('ImageSource.txt', 'w') 
  numPhotos = len(data[0]['photos'])
  parsedData = []
  for x in range(0, numPhotos, 1):
    dict1 = {}
    dict1['camera_name'] = data[0]['photos'][x]['camera']['name']
    dict1['id'] = data[0]['photos'][x]['id']
    dict1['earth_date'] = data[0]['photos'][x]['earth_date']
    dict1['img_src'] = data[0]['photos'][x]['img_src']
    dict1['rover_name'] = data[0]['photos'][x]['rover']['name']
   
    parsedData.append(dict1)
    felixFile.write(data[0]['photos'][x]['img_src'])
    felixFile.write('\n')

  dict2 = {}
  dict2['images'] = parsedData
  with open('data.txt', 'w') as outFile:
    json.dump(dict2, outFile)

  felixFile.close()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Mars Pictures")
  parser.add_argument('-k', '--api_key', help = 'api key needed for query')
  parser.add_argument('-d', '--date', help = 'Date for query.')
  parser.add_argument('-p', '--page', help = 'Page for query.')
  parser.add_argument('-c', '--camera', help = 'Camera for query')
  args = parser.parse_args()

  api_key = args.api_key
  date = args.date
  
  if args.page:
    page = args.page
  else:
    page = None
  if args.camera:
    camera = args.camera
  else:
    camera = None

  readData(api_key, date, page, camera)

