import requests
import json
import pandas as  pd
import time


start_time=time.process_time()
API_KEY="c55cf1bd94dbcd5b04a1bfdfa6c9f461"
# urlcomp='https://api.themoviedb.org/3/movie/popular?api_key=c55cf1bd94dbcd5b04a1bfdfa6c9f461&language=en-US&page=1'
def getjson(pagenum):
    link=f'https://api.themoviedb.org/3/movie/top_rated?api_key=c55cf1bd94dbcd5b04a1bfdfa6c9f461&language=en-US&page={pagenum}'
    request_api=requests.get(link)
    moviesdatajson=request_api.json()
    return moviesdatajson

def getjson1(movieid):
    link=f'https://api.themoviedb.org/3/movie/{movieid}/external_ids?api_key={API_KEY}'
    request_api=requests.get(link)
    moviesdatajson1=request_api.json()
    return moviesdatajson1
# req=requests.get('https://api.themoviedb.org/3/movie/popular?api_key=c55cf1bd94dbcd5b04a1bfdfa6c9f461&language=en-US&page=1')
# weatherdatajson=req.json()

# rcomp = requests.get(urlcomp )
maindf=pd.DataFrame()
for i in range(1,50):
    pqr=getjson(i)['results']
    # print(pqr)

    df=pd.DataFrame(pqr)
    maindf=maindf.append(df)

print(maindf)

idlist=maindf['id']
movieslist=maindf['title']
imdb_id_list=[]
movies_list=[]

for i in range(len(idlist)):
    ids=idlist.iloc[i]
    # moviename=maindf['title'][i]
    movies=movieslist.iloc[i]
    # print(ids)
    externalid=getjson1(ids)
    # print(externalid['imdb_id'],movies)
    imdb_id=externalid['imdb_id']
    imdb_id_list.append(imdb_id)
    # print(imdb_id_list)
    movies_list.append(movies)
    # print(movies_list)

moviesdf=pd.DataFrame(imdb_id_list,movies_list)

moviesdf.to_csv('imdb_id_moviename__toprated.csv')
print("done")

end_time=time.process_time()

print("Total execution time ",start_time-end_time)
