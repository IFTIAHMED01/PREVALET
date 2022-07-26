# Project Name - PREVALET
# Documentation of Python Script to extract Twitter data from Twitter API Version 2.0
So, before creating this Python script to extract Twitter data, we need to follow some steps to get the Twitter API ready for data extraction. Those steps are:</br></br>
1.) <b> So. the first step is to apply for a Twitter Developer Account </b>. Inorder to do that, navigate to Twitter’s apply for access page and apply for a developer account.Then, after navigation, login to your Twitter if you have already created a account. Otherwise, sign up for a Twitter account. Then, after successfully logging in, you’ll be navigated to a questionnaire on why and how you intend to use the Twitter API. Fill it according to your use-case. In this case, it will be the <b> Academic Research </b> option. After that, answer all the follow-up questions. Then, <b> Review </b> the Developer Agreement and Policy and <b> Submit your Application </b>. Then, check your email and click the confirmation link to complete the application process.</br></br>
2.) <b> Then, the next step is to get the Twitter Access/Bearer Token from our Twitter Developer Account </b>. So, on clicking the confirmation email from the above application step, you’ll be navigated to the Twitter Developer Platform. Give your App a name and click Get keys. You’ll be shown your <b> API key </b> and <b> API Access Token </b>. Copy and save them securely. You’ll be using them to access the Twitter API. For our purpose for this script, we only need the <b> API Access Token </b> for successful connection to our Twitter API Version 2.0.
3.) Now, since we have the <b> API Bearer/Access Token </b>, we can use that token and the python script I provided here to successfully extract the Twitter Data using Twitter API 2.0. <b> Note that, python script I provided here only works for Twitter API Version 2.0, not for any other versions </b>. </br></br>
# Explanation of my Python Script</br>
•  Firstly, you need to import requests (import os and import json). </br>
•  Secondly, To set your environment variables in your terminal run the following line: </br>
   <b> export 'BEARER_TOKEN'='<your_bearer_token>' </b> </br>
•  Then you have to a search_url which will be constant all the time. </br>
   <b> search_url = "https://api.twitter.com/2/tweets/search/recent" </b> </br>
•  Then, you will have to setup your search query parameter inorder to specify what exactly are you looking for. In this scenario, it will be mostly related to <b>    illicit drugs </b>. We can also use optional parameters inorder to manipulate the search to our likings. </br>
   <b> Optional params: start_time,end_time,since_id,until_id,max_results,next_token, </br>
   expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields </br> </b>
•  <b> bearer_oauth(r): </b> </br>
    Method required by bearer token authentication. </br>
    So here, in this method we have to pass the value of our Bearer Tokens that we got from our Twitter developer account </br>
    inorder for the Twitter to successfully authenticate our request to get Twiiter Data. </br>
•  <b> connect_to_endpoint(url, params): </b> </br>
    This is the method used to request connection to the Twitter Version 2.0 Endpoint. </br>
    By using the search_url and query_params. </br>
    If there is any error, this method raises Exceptions </br>
