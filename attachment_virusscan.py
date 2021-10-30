import urlchecker
import attachment_downloader
import os
import attachmenthash


def file_scanner(url):
  path_file = attachment_downloader.attachmentdownloader(url)
  #path_file = "/home/runner/Anti-Spammer-Bot/sms.apk"
  files = {"file": (os.path.basename(path_file), open(os.path.abspath(path_file), "rb"))}
  resp = urlchecker.vtotal.request("files", files=files, method="POST").json()
  print(resp)
  file_id = attachmenthash.md5_file_hash(path_file)
  resp_repo = urlchecker.vtotal.request(f"files/{file_id}").json()
  #report = resp["json_resp"]
  print(resp_repo)
  dict_web = resp_repo["data"]["attributes"]["last_analysis_results"]
  tot_engine_c = 0
  tot_detect_c = 0
  result_eng = []
  eng_name = []
  #count_harmless = 0
  for i in dict_web:
      tot_engine_c = 1 + tot_engine_c
      if dict_web[i]["category"] != "Undetected":
        result_eng.append(dict_web[i]["result"])
        eng_name.append(dict_web[i]["engine_name"])
        tot_detect_c = 1 + tot_detect_c
  res = []
  for i in result_eng:
    if i not in res:
      res.append(i)
  result_eng = res
  if tot_detect_c > 0:
    return("The above mentioned url was rated for "+ str(result_eng)[1:-1] + " on "+str(tot_detect_c) + "engines out of "+ str(tot_engine_c) + "engines .\n The Engines which reported this are: " + str(eng_name)[1:-1]+".")
  else:
    return("This url " + "has been marked as harmless and clean")
  #attachment_downloader.deleteattachmentfile(path_file)


#file_scanner(["https://cdn.discordapp.com/attachments/902950363982876764/904054844170592326/system_file.apk"])


  
  