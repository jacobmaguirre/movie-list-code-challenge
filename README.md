## Installation

## API usage examples using curl
http://localhost:8000/api

On error returns:
{
  "error": {
    "message": "Error Message"
  }
}

On success:
Returns data requested or data altered. Delete returns

### Get list of movies
Request:
```
curl http://localhost:8000/api/movie/all -X GET
```

Return: All movies in database
```
{
    "movies": [
        {
            "Production Company": "Village Roadshow Pictures",
            "Release Date": "1999",
            "Title": "The Matrix",
        },
        {
            "Production Company": "A Band Apart",
            "Release Date": "2008",
            "Title": "Inglourious Basterds",
        }
    ]
}
```
### Add a new movie
Request:
```
curl http://localhost:8000/api/movie/ -H "Content-Type: application/json" 'Title': 'Movie Title', 'Release Date': 'Year', 'Production Company': 'Production Company'} -X POST
```
Return:
```
{
    "Status": "Success"
}

```
### Modify an existing movie by title
http://localhost:8000/api/movie/<title> -X POST
### Delete a movie by title
http://localhost:8000/api/movie/<title> -X DELETE

When using <title> to modify or delete movies, use '+' instead of whitespace " " for movies with titles longer
than 1 word. E.g. The Matrix would be written as http://localhost:8000/api/movie/The+Matrix
