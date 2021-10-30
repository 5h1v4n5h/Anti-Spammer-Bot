import requests
import subprocess
import os


def attachmentdownloader(url):
  url = url[0]
  #r = requests.get(url)
  filename = url[77:]

  
  directory_path = os.getcwd()
  path_file = directory_path+"//tempdownload//"+filename
  bashCommand = 'curl '+ url+" --output "+path_file 
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output, error = process.communicate()
  '''with open(path_file, 'wb') as f:
      f.write(r.content)
    '''
  return path_file


def deleteattachmentfile(path):
  os.remove(path)


