from virustotal_python import Virustotal
from base64 import urlsafe_b64encode
import os

my_secret_VT = os.environ['APIKEY']
vtotal = Virustotal(API_KEY=my_secret_VT, API_VERSION="v3")

def urlchecker(url):
  try:
    #resp = vtotal.request("urls", data={"url": url}, method="POST")
    url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
    analysis_resp = vtotal.request(f"urls/{url_id}").json()
    dict_web = analysis_resp["data"]["attributes"]["last_analysis_results"]
    tot_engine_c = 0
    tot_detect_c = 0
    result_eng = []
    eng_name = []
    count_harmless = 0
    for i in dict_web:
        tot_engine_c = 1 + tot_engine_c
        if dict_web[i]["category"] == "malicious" or dict_web[i]["category"]  == "suspicious":
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
      
  except:
    print("ok")
#except: VirustotalError as err:
    #print(f"An error occurred: {err}\nCatching and continuing with program.")

#urlchecker(url)