dished_server
=============

Dished is a dish review app for Android currently in progress.

This is the server with a rest api to store persistent data.

Django, Tastypie  
Heroku, PostgreSQL

## REST API
| endpoint                              | description                        |
| --------------------------------------|------------------------------------|
| /api/dish/ POST                       | create new                         |
| /api/dish/123 GET                     | get single dish                    |
| /api/dish/?restaurant='McD' GET       | get dishes of restaurant           |
| /api/review/?dish=123 GET             | get all single dish's reviews      |
| /api/review/ POST                     | new review                         |
| /api/review/456 GET, PUT, DELETE      | get/modify single review           |
| /api/restaurant/ GET, POST            | get all restaurants, create new    |


### restaurant post payload

{  
"name": "McDonald's 3",  
"address": "100 Rainbow Road",  
"state": "NY",  
"country": "US",  
"postal_code": "12345",  
"restaurant_type": "fast_food"  
}  

not completed
/api/dish/?category=5 GET


### questions:
number of requests vs size of request
should server be filtering more or android? (fetch more info and calculate on android, or fetch relevant info filtered by server?

mobile apps should have infrequent, larger requests due to lower bandwidth
