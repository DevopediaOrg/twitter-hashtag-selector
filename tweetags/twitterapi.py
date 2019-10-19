import tweepy
import re


API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_KEY = ""


def tweepy_auth(api_key, api_secret_key, access_token, access_token_key):
    """Authentication using twitter api_key, api_secret_key, access_token,
    and access_token_key

    api_key: get the key from twitter developer account.
    api_secret_key: get the secret key from twitter developer account.
    access_token: get the access token from twitter developer account.
    access_token_secret: get the access token key from twitter developer account.
    returns: it returns twitter authentication api.
    """
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_key)
    api = tweepy.API(auth)
    return api


def keyword_search(keyword):
    """Keyword search function to returns related hash tags.

    keyword: input text to search all the twitter hash tags.
    returns: list of unique hash tags realated to input keyword.
    """
    api_key, api_secret_key = API_KEY, API_SECRET_KEY
    access_token, access_token_key = ACCESS_TOKEN, ACCESS_TOKEN_KEY
    api = tweepy_auth(api_key, api_secret_key, access_token, access_token_key)
    hash_tag = []
    for text in api.search(q=keyword, lang="en", ):
        tags = re.findall(r"(#\w+)", str(text))
        hash_tag.extend(tags)
    return set(hash_tag)


if __name__ == '__main__':
    tags = keyword_search("Python")
    print(tags)
