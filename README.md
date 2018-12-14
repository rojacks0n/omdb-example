# omdb-example
Simple example program to query OMDB API and print the Rotten Tomatoes rating for a given movie.
To build and execute:
  ```
  docker build . -t omdb-example
  docker run omdb-example <Movie Title>
  ```