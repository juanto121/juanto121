import json


def score(event, context):
    try:
        body = json.loads(event['body'])
        questions = body['questions']
        name = body['name']
        # other parameters
        
        # scoring_result = scorer.score(questions)
        scoring_result = "dummy_data"

        response = {
            "statusCode": 200,
            "body": json.dumps(scoring_result),
            "headers": {"Access-Control-Allow-Origin": '*'}
        }

    except Exception as e:
        response = {
            "statusCode": 500,
            "body": "Failed to score",
            "headers": {"Access-Control-Allow-Origin": '*'}
        }

    return response

