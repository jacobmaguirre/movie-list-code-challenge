## Installation

## API usage examples using curl

### Get a list of movies
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
curl http://localhost:8000/api/movie/add -X POST -H "Content-Type: application/json" -d '{"Title": "Movie Title", "Release Date": "Year", "Production Company": "Production Company"}'
```
Return:
```
{
    "Status": "Success"
}
```
### Modify an existing movie by title
Request:
```
curl http://localhost:8000/api/movie/Movie+Title -X POST -H "Content-Type: application/json" -d '{"Title": "Movie Title", "Release Date": "Year", "Production Company": "Production Company A"}'
```
Return:
```
{
    "Status": "Success"
}
```
### Delete a movie by title
Request:
```
 curl http://localhost:8000/api/movie/Movie+Title -X DELETE
```
Return:
```
{
    "Status": "Success"
}
```

Notes:
When using <title> to modify or delete movies, use '+' instead of whitespace " " for movies with titles longer
than 1 word. E.g. The Matrix would be written as http://localhost:8000/api/movie/The+Matrix

Errors return in the following format:
```
{
  "error": {
    "message": "Error Message"
  }
}
```

