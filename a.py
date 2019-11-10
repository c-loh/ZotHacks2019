import json
import urllib.parse
import urllib.request


# You'll need to paste a valid Google API key here.  It needs to be one
# that has the YouTube Data API activated.  I've created such an API key
# for this course -- which I'll email out separately -- but you can also
# create your own, if you prefer.
GOOGLE_API_KEY = 'AIzaSyAo_ZSrnG3i80YVJw4Q2X7xygbxPzqyhAM'

# All of the services provided by the YouTube Data API have URLs that
# begin like this; it's simply a matter of adding the rest of the URL
# and its query parameters to the end of this.
BASE_YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3'
titlelist = []
idlist = []
thumbnaillist = []
likes_views = []

FOOD_URL = "https://www.themealdb.com/api/json/v1/1/filter.php?i="




def build_search_url(search_query: str, max_results: int) -> str:
    '''
    This function takes a search query and the maximum number of results
    to display, and builds and returns a URL that can be used to ask the
    YouTube Data API for information about videos matching the search
    request.
    '''

    # Here, we create a list of two-element tuples, which we'll convert to
    # URL query parameters using the urllib.parse.urlencode function.  The
    # reason we do this, rather than building the URL string ourselves, is
    # because there is a fair amount of complexity -- dealing with special
    # characters, etc. -- that will be difficult to get precisely correct,
    # but that urllib.parse.urlencode already knows how to do correctly.
    query_parameters = [
        ('key', GOOGLE_API_KEY), ('part', 'snippet'),
        ('type', 'video'), ('maxResults', str(max_results)),
        ('q', search_query)
    ]

    return BASE_YOUTUBE_URL + '/search?' + urllib.parse.urlencode(query_parameters)



def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None

    try:
        # Here, we open the URL and read the response, just as we did before.
        # After the second line, json_text will contain the text of the
        # response, which should be in JSON format.
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        # Given the JSON text, we can use the json.loads() function to convert
        # it to a Python object instead.
        return json.loads(json_text)

    finally:
        # We'd better not forget to close the response when we're done,
        # assuming that we successfully opened it.
        if response != None:
            response.close()



def addlist(search_result: dict) -> None:
    '''
    This function takes a parsed JSON response from the YouTube Data API's
    search request and prints the titles and descriptions of all of the
    videos in the response.
    '''
    
    for item in search_result['items']:
        idlist.append(item["id"]["videoId"])
        titlelist.append(item["snippet"]["title"])
        thumbnaillist.append(item["snippet"]["thumbnails"]["default"]["url"])
        print(item)

    for i in idlist:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={i}&key={GOOGLE_API_KEY}"

        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        print(json_text)

        likes_views.append((json_text["items"][0]["statistics"]["likeCount"],json_text["items"][0]["statistics"]["viewCount"]))

    print(likes_views)



"""def calculateformula():
    ratios = []
    for i in range(len(idlist)):
        likes = idlis"""


def get_recipes():
    x = True
    foodlist = []
    while x:
        main_food = input("What main food?")
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
    print("Which meal? Select number")
    for i in foodlist:
        print(i[0],i[1])
    foodnumber = int(input())
    currentfood = foodlist[foodnumber-1][1].lower().replace(" ","_")
    return currentfood
    
def print_food(food):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}"
    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    table = json.loads(json_text)
    #print(table)
    for i in table["meals"]:
        print(i["strMeal"]+":")
        print (i['strInstructions'])
        print()



def run() -> None:
    #search_query = input('Query: ')
    current_food = get_recipes()
    print_food(current_food)
   # x = build_search_url(search_query,1)
    #print(x)
    #result = get_result(x)
    #addlist(result)



if __name__ == '__main__':
    run()
