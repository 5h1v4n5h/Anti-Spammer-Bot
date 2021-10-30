import hashlib

def md5_file_hash(path):
  h = hashlib.sha1()
  with open(path,'rb') as file:
    chunk = 0
    while chunk != b'':
      chunk = file.read(1024)
      h.update(chunk)
  return h.hexdigest()