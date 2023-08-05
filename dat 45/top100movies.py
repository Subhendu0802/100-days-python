from bs4 import BeautifulSoup
import requests
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
#url=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
#print(response.text)
data=response.text
#data2=url.text
soup=BeautifulSoup(data,"html.parser")
#soup2=BeautifulSoup(data2,"html.parser")
#print(soup.title)
#print(soup.h3)
#tag=soup.h3.getText()
#print(tag)
names=soup.findAll("h3")
years=soup.findAll("strong")
list_of_movies=[]
year_of_movies=[]
for x in names:
    list_of_movies.append(x.getText())
for y in years:
     year_of_movies.append((y).getText())
#print(list_of_movies)
#print(year_of_movies)

#lets reverse the listf movies
top_movies=list_of_movies[::-1]
#print(top_movies)
#lets reverse the years
years=year_of_movies[::-1]
#print(len(top_movies))
# with open('day 45/Top_Movies.txt',mode="w") as file:
#      for movies in top_movies:
#           file.write(f'{movies}\n')
with open('day 45/Top_Movies.txt', mode="w",encoding="utf-8") as file:
    for movie, year in zip(top_movies, years):
            file.write(f'{movie} ({year})\n')
