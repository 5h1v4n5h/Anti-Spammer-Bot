from virustotal_python import Virustotal
from base64 import urlsafe_b64encode
#import VT
import os
from replit import db


db["Error_404_count"] = 0


my_secret_VT = os.environ['APIKEY']
vtotal = Virustotal(API_KEY=my_secret_VT, API_VERSION="v3")
bool_repo_output = True #boolean variable to check if report is there

def urlchecker(url):
  try:
    url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
    analysis_resp = vtotal.request(f"urls/{url_id}").json()
    if "error" in analysis_resp:
      bool_repo_output = False
      error_code = analysis_resp["error"]["code"]
      error_message = analysis_resp["error"]["error_message"]
      if error_code == "NotFoundError":
        db["Error_404_count"] +=1
        return (error_message)
      else:
        return("Unable to check url kindly open at your own risk.")
      print(error_code,error_message)
    dict_web = analysis_resp["data"]["attributes"]["last_analysis_results"]
    tot_engine_c = 0
    tot_detect_c = 0
    result_eng = []
    eng_name = []
    #count_harmless = 0
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
    if bool_repo_output == True:
      if tot_detect_c > 0:
        return("The above mentioned url was rated for "+ str(result_eng)[1:-1] + " on "+str(tot_detect_c) + "engines out of "+ str(tot_engine_c) + "engines .\n The Engines which reported this are: " + str(eng_name)[1:-1]+".")
      else:
        return("This url " + "has been marked as harmless and clean")
      
  except:
    print("Its Running in good condition.")

