import regex as re
import validators

def urldetector(message):
  regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  url = re.findall(regex,message.content.lower())
  url_list = [x[0] for x in url]
  valid_url = url_validator(url_list)
  return valid_url

def url_validator(url_list):
  for i in url_list:
    valid=validators.url(i)
    if valid != False:
      url_list.remove(i)
  return url_list