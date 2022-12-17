# install and set up our modules (requests,beautifulsoup4)
from typing import List
import requests
from bs4 import BeautifulSoup
job_tile=[]
job_skill=[]
company_name=[]
company_location=[]
page=0
while page!=13:
   url=f"https://wuzzuf.net/search/jobs/?a=hpb&q=UI%20Designer&start={page}"
# use requests to fetch url
   result=requests.get(url)
# save the page content
   src=result.content
# print(src)
# create soup object to parse content
   soup=BeautifulSoup(src,"html.parser")
# print(soup)
   page=page+1
# find elements containing information we need
# job title, #job skills ,#company name ,#location name
   job_titles=soup.find_all("h2",{"class":"css-m604qf"})
# print(job_titles)
   company_names=soup.find_all("a",{"class":"css-17s97q8"})
# print(company_names)
   company_locations=soup.find_all("span",{"class":"css-5wys0k"})
# print(company_locations)
   job_skills=soup.find_all("div",{"class":"css-y4udm8"})
# print(job_skills)
# loop over returned lists to extract needed information
   for i in range(len(job_titles)):
      job_tile.append(job_titles[i].text)
      company_name.append(company_names[i].text)
      company_location.append(company_locations[i].text)
      job_skill.append(job_skills[i].text)
      print(company_location)
      print(company_name)
      print(job_skill)
      print(job_tile)
