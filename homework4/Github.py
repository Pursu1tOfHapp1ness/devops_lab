import requests
import time
import getpass
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
NameOfUser = config["GitStatsUsername"]["GitStatsUsername"]
NameOfRepo = config["GitStatsRepo"]["GitStatsRepo"]
ID = config["GitStatsId"]["GitStatsId"]
GitName = config["YourGitUsername"]["GitUsername"]
GitCredentials = getpass.getpass("Enter your github profile credentials: ")

URL1 = "https://api.github.com/" + "repos/" \
      + NameOfUser + "/" \
      + NameOfRepo + "/" \
      + "pulls/" + str(ID)
data = requests.get(URL1, auth=(GitName, GitCredentials)).json()
print("URL of chosen repo: %s" % str(data['url']))
print("User login of chosen ID: %s" % str(data['user']['login']))
print("Title of chosen Id: %s" % str(data['title']))
print("Create at: %s" % str(data['created_at']))
print("Update at: %s" % str(data['updated_at']))
print("Closed at: %s" % str(data['closed_at']))
print("Count of commits: %s" % str(data['commits']))
print("\n")
time.sleep(2)
URL2 = URL1 + "/files"
data_inf = requests.get(URL2, auth=(GitName, GitCredentials)).json()
for i in data_inf:
    print("Filename : %s" % str(i['filename']))
    print("Count of additions : %s" % str(i['additions']))
    print("Count of deletions : %s" % str(i['deletions']))
    print("Count of changes : %s" % str(i['changes']))
    print("\n")
