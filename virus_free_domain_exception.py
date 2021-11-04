
virus_free_domain = ["https://www.google.com","https://www.youtube.com","https://www.instagram.com","https://dev.to",]

def virusfreedomaincheck(url):
  for i in virus_free_domain:
    if i in url:
      #return ("This url has been marked as harmless and clean")
      return