from bottle import route, run, request, response, delete, get, post
from pymongo import MongoClient
import json
from bson import json_util

# Create mongodb client
client = MongoClient('104.239.143.109', 27017)

# Connect to collection
db = client.test_1
collection = db.test_collection

## API methods

# Default /api/
@route('/api', method="GET")
def api():
    return 'Main api page'

# Returns all movies
@get('/api/movie/all')
def get_movies():
    # Set response header
    response.headers['Content-Type'] = 'application/json'

    # Query database for full list of movies without mongodb ids
    movie_list = []
    db_query = collection.find({}, {'_id': False})
    for movie in db_query:
        movie_list.append(movie)

    # Return list in JSON format
    return json.dumps({'movies': movie_list}, indent=4, sort_keys=True, default=json_util.default)

# Add a movie
@post('/api/movie/add')
def add_movie():
    # Set response header
    response.headers['Content-Type'] = 'application/json'

    # Request json and check if JSON is invalid
    try:
        json_request = request.json
    except ValueError:
        return error_message("Invalid JSON provided or 'Content-Type' header not set to 'application/json'")

    # Check for empty or invalid JSON
    if json_request is None:
        return error_message("Invalid JSON provided or 'Content-Type' header not set to 'application/json'")

    # Add movie to collection and return success
    collection.insert(json_request)
    return json.dumps({"Status": "Success"}, indent=4)

@delete('/api/movie/<title>')
# Deletes a movie
def delete_movie(title):
    # Set response header
    response.headers['Content-Type'] = 'application/json'

    # Convert + into whitespace for search
    title_string = str(title).replace("+", " ")

    # Check if title exists, if so delete
    if collection.count({'Title': title_string}) == 0:
        return error_message("Title not found")
    else:
        db.test_collection.delete_one({'Title': title_string})
        return json.dumps({"Status": "Success"}, indent=4)

# Updates a movies details
@post('/api/movie/<title>')
def update_movie(title):
    #Set response header
    response.headers['Content-Type'] = 'application/json'

    # Convert + into whitespace for search
    title_string = str(title).replace("+", " ")

    # Request json and check if JSON is invalid
    try:
        json_request = request.json
    except ValueError:
        return error_message("Invalid JSON provided or 'Content-Type' header not set to 'application/json'")

    # Check for empty or invalid JSON
    if json_request is None:
        return error_message("Invalid JSON provided or 'Content-Type' header not set to 'application/json'")

    # Check if title exists, if so delete and add new data
    if collection.count({'Title': title_string}) == 0:
        return error_message("Title not found in database")
    else:
        db.test_collection.delete_one({'Title': title_string})
        collection.insert(json_request)

    # Return success
    return json.dumps({"Status": "Success"}, indent=4)

# Error message response
def error_message( message):
    # Set response header and error message
    response.headers['Content-Type'] = 'application/json'
    body = {'message': message}
    return json.dumps({'error': body}, indent=4, sort_keys=True)


# Run host
run(host='localhost', port=8000)
