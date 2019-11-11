
import json
import urllib.parse
import urllib.request


GOOGLE_API_KEY = 'AIzaSyAo_ZSrnG3i80YVJw4Q2X7xygbxPzqyhAM'
BASE_YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3'
youtube_link = "https://www.youtube.com/watch?v="
titlelist = []
idlist = []
thumbnaillist = []
likes = []
videos_to_display = []
FOOD_URL = "https://www.themealdb.com/api/json/v1/1/filter.php?i="


def build_search_url(search_query, max_results):
    query_parameters = [
        ('key', GOOGLE_API_KEY), ('part', 'snippet'),
        ('type', 'video'), ('maxResults', str(max_results)),
        ('q', search_query)
    ]

    return BASE_YOUTUBE_URL + '/search?' + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> dict:
    response = None

    try:

        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()



def addlist(search_result: dict) -> None:
    for item in search_result['items']:
        idlist.append(item["id"]["videoId"])
        titlelist.append(item["snippet"]["title"])
        thumbnaillist.append(item["snippet"]["thumbnails"]["default"]["url"])
        #print(item)

    for i in idlist:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={i}&key={GOOGLE_API_KEY}"

        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        json_text = json.loads(json_text)
        likes.append(int(json_text["items"][0]["statistics"]["likeCount"]))

    index_one = likes.index(max(likes))
    likes[index_one] = 0
    index_two = likes.index(max(likes))
    likes[index_two] = 0
    index_three = likes.index(max(likes))
    videos_to_display.append((titlelist[index_one],youtube_link+idlist[index_one],thumbnaillist[index_one]))
    videos_to_display.append((titlelist[index_two],youtube_link+idlist[index_two],thumbnaillist[index_two]))
    videos_to_display.append((titlelist[index_three],youtube_link+idlist[index_three],thumbnaillist[index_three]))
    return videos_to_display


    




def get_recipes(main_food):
    x = True
    foodlist = []
    while x:
        #main_food = input("What main food?")  use paramater instead
        link = FOOD_URL+str(main_food)
        response = urllib.request.urlopen(link)
        json_text = response.read().decode(encoding = 'utf-8')
        table = json.loads(json_text)
        if table["meals"] !=None:
            x = False
        if x:
            print("invalid food option, try again")
    for i in range(len(table["meals"])):
        foodlist.append((i+1,table["meals"][i]["strMeal"]))
    #for i in foodlist:
      #  print(i[0],i[1])
    return foodlist

def food_search(foodnumber):
    return foodlist[foodnumber-1][1]
def get_food_string(foodnumber):
    #foodnumber = int(input())
    return foodlist[foodnumber-1][1].lower().replace(" ","_")
    
    
def print_food(food):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}"
    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    table = json.loads(json_text)
    return table
    #print(table)
    '''for i in table["meals"]:
        #print("Ingredients:")
        for a in range(1,21):
            if i[f"strIngredient{a}"] != "":
            #    print(i[f"strIngredient{a}"],i[f"strMeasure{a}"])
        print(i["strMeal"]+":")
        print (i['strInstructions'])
        print()'''
    


#def run() -> None:
'''
   current_food = get_recipes()
   x = build_search_url(current_food,3)
    result = get_result(x)
    addlist(result)

    get user input and put into get_recipes// returns list of foods with choice number
    get user input of choice number and put into get_food_string
    put answer of get_food_string into print_food, returns table where you print ingrediants meals and instructions
    use food_search and put answer into  build_search_url, put url into get_result
    put answer from get_result into addlist, returns  table with 1.title 2.video link 3.Thumbnail link
'''


from flask import Flask, request#, response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/food', methods = ["POST"])
def hello_world():
    food = request.get_json()
    #response.header["Access-Control-Allow-Origin"] = "*"


    food_choices = get_recipes(food["food"]) #food choices
    print(food_choices)


    food_string = get_food_string(number) #food string to put in as link
    table = print_food(food_string)
    
    #for youtube link
    url = build_search_url(foodsearch(number))
    answer = get_result(url) #returns json of all food info
    table_two = addlist(answer)
    print(table_two)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return {}

if __name__ == '__main__':
    app.run(port=5000, debug=True, use_reloader=True)


