## Lambda template for python functions

### Usage:

to test offline:
 - needs npm
 - recommended use of virtualenv
 - needs to install serverless 

``
  npm i
  pip install -r requirements.txt
  sls offline
``

POST /score
{
	"questions":[],
	"name": "something"
}


curl --location --request POST 'localhost:3000/score' \
--header 'Content-Type: application/json' \
--data-raw '{
	"questions":[],
	"name": "something"
}'

