## Lambda template for python functions

### Usage:

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

