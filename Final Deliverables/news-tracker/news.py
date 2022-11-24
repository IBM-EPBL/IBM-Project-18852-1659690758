import requests
from pprint import pprint
from .config import RAPID_API_KEY, API_URI
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import functools



class FreeNews:
    """
    FreeNews RapidAPI Wrapper Class

    """
    def __init__(self):
        self.__header = {
            "X-RapidAPI-Key": RAPID_API_KEY,
            "X-RapidAPI-Host": "newscatcher.p.rapidapi.com"
        }
        self.__uri = API_URI


    def __request(self, path: str, querystring: dict):
        try:
            req = requests.request("GET", f'{self.__uri}/{path}', headers=self.__header, params=querystring)
            return req
        except requests.exceptions.RequestException as e:
            return e
    
    def Top(self, lang="en"):
        """
        Get top news

        Returns:
            A JSON object
        """
        query = {
            "lang": lang,
            "media": True
        }

        res = self.__request('latest_headlines', query)
        return res.json()


    def Search(self, query: str, lang="en"):
        """
        Search for a query which will return a JSON Object

        Arguments:
            query: A string that you want to search

        Returns:
            A JSON object
        """
        query = {
            "q": query,
            "lang": lang,
            "media": True
        }
        res = self.__request('search_free', query)
        return res.json()


news = FreeNews()
bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/top', methods=['GET'])
def top_news_fetch():

    print(g.user)

    json_obj = news.Top()

    if len(json_obj) < 3:
        return render_template('news.html', raw_obj_len=len(json_obj), query=query)
    else:
        return render_template('news.html', query="Top news", obj=json_obj["articles"], res = len(json_obj["articles"]), raw_obj_len=len(json_obj))



@bp.route('/query/<query>', methods=['GET', 'POST'])
def news_fetch(query):

    if request.method == 'POST':
        q = request.form['search']
        return redirect(url_for('news.news_fetch', query=q))
    else:
        json_obj = news.Search(str(query))
        if len(json_obj) < 3:
            return render_template('news.html', raw_obj_len=len(json_obj), query=query)
        else:
            return render_template('news.html', query=query, obj=json_obj["articles"], res = len(json_obj["articles"]), raw_obj_len=len(json_obj))

@bp.route('/query/<query>/JSON')
def news_fetch_json(query):
    json_obj = news.Search(query)
    return json_obj