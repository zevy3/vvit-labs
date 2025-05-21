from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel
import wikipedia

app = FastAPI()

# @app.get("/")
# def joke():
#     return pyjokes.get_joke() 

# @app.get("/{friend}")
# def friends_joke(friend: str):
#     return friend + " tells his joke:" + pyjokes.get_joke() 


# @app.get("/multi/{friend}")
# def multi_friends_joke(friend: str, jokes_number: int):
#     result = ""
#     for i in range(jokes_number):
#         result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " " 
#     return result

# class Joke(BaseModel):
#     friend: str
#     joke: str

# class JokeInput(BaseModel):
#     friend: str
 
# @app.post("/", response_model=Joke)
# def create_joke(joke_input: JokeInput):
#     """Создание шутки"""
#     return Joke(friend=joke_input.friend, joke=pyjokes.get_joke()) 


wikipedia.set_lang("ru")


class WikiSummary(BaseModel):
    title: str
    summary: str


class WikiRequest(BaseModel):
    topic: str

@app.get("/summary/{request}")
def get_summary(request: str):
    return wikipedia.summary(f"{request}")

@app.get("/multi/{name}")
def multi_articles(name: str, articles_number: int):
    result = ""
    search_term = "наука"
    articles = wikipedia.search(search_term)
    for i in range(articles_number):
        result += f"{name} рекомендует статью #{i + 1}: {articles[i]}. "

    return result

@app.post("/article", response_model=WikiSummary)
def get_article_by_body(request: WikiRequest):
    summary = wikipedia.summary(request.topic)
    return WikiSummary(title=request.topic, summary=summary)