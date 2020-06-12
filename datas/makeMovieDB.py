import json

genre_set = {}
genre_dic = []
num = 1

with open('movieRawData.json', 'r', encoding='UTF-8-sig') as fr:
    movie_dic = json.load(fr)

for movie in movie_dic:
    field = movie["fields"]
    genres = field["genre"]
    genre_list = genres.split(',')
    for genre in genre_list:
        if genre not in genre_set:
            new_dic = {
                "pk": num,
                "model": "movies.genre",
                "fields": {
                    "name": genre
                }
            }
            genre_set[genre] = num
            genre_dic.append(new_dic)
            num += 1


with open('genre.json', 'w', encoding='UTF-8') as fp:
    json.dump(genre_dic, fp, ensure_ascii=False, indent=4)
    
for j in range(len(movie_dic)):
    field = movie_dic[j]["fields"]
    genres = field["genre"]
    genre_list = genres.split(',')
    code_list = []
    for i in range(len(genre_list)):
        genre_list[i] = genre_set[genre_list[i]]
    print(genre_list)
    movie_dic[j]["fields"]["genre"] = genre_list
print(movie_dic)

with open('movieDB2.json', 'w', encoding='UTF-8') as fp:
    json.dump(movie_dic, fp, ensure_ascii=False, indent=4)

######################## Genre 끝 ########################
actor_set = {}
actor_dic = []
num = 1

with open('movieDB2.json', 'r', encoding='UTF-8-sig') as fr:
    movie_dic = json.load(fr)

for movie in movie_dic:
    field = movie["fields"]
    actor = field["actors"]
    actor_list = actor.split('|')
    for actor in actor_list:
        new_name = ''
        for c in actor:
            if c == '(': break
            else: new_name += c
        new_name = new_name.strip()
        if new_name not in actor_set:
            new_dic = {
                "pk": num,
                "model": "movies.actor",
                "fields": {
                    "name": new_name
                }
            }
            actor_set[new_name] = num
            actor_dic.append(new_dic)
            num += 1
print(actor_set)


with open('actor.json', 'w', encoding='UTF-8') as fp:
    json.dump(actor_dic, fp, ensure_ascii=False, indent=4)

for j in range(len(movie_dic)):
    field = movie_dic[j]["fields"]
    actor = field["actors"]
    actor_list = actor.split('|')
    code_list = []
    for i in range(len(actor_list)):

        new_name = ''
        for c in actor_list[i]:
            if c == '(': break
            else: new_name += c
        new_name = new_name.strip()

        actor_list[i] = actor_set[new_name]
    movie_dic[j]["fields"]["actors"] = actor_list
print(movie_dic)

with open('movie.json', 'w', encoding='UTF-8') as fp:
    json.dump(movie_dic, fp, ensure_ascii=False, indent=4)