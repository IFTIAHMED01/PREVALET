import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAE82cgEAAAAAnARj96URqDRE2QEGw1W9EmwymKI%3DBQAAnXnBggf9Kels8Z9JMVA61gQZmcde4taaakewtpzmM23l2j"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '#marijuana OR #opioids OR #weed OR #illicitdrugs','max_results':100,'start_time':'2022-07-19T21:32:00Z','tweet.fields': 'created_at,author_id'}


def bearer_oauth(r):
    """
    bearer_oauth(r):
    Method required by bearer token authentication.
    So here, in this method we have to pass the value of our Bearer Tokens that we got from our Twitter developer account 
    inorder for the Twitter to successfully authenticate our request to get Twiiter Data.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    """
    connect_to_endpoint(url, params):
    This is the method used to request connection to the Twitter Version 2.0 Endpoint.
    By using the search_url and query_params.
    If there is any error, this method raises Exceptions
    """
    
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(bearer_oauth.__doc__)
    print(connect_to_endpoint.__doc__)
    print("*Documentation Ends Here*")
    print("--------------------------------------------------------------------------------------------------------")
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
