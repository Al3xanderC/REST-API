# REST-API
 REST-api in Python using Flask

My first project in python. I created a Flask application with three routes: /operations, /words, and /average. These routes handle various calculations like arithmetic operations, word count from a text file and average calculation from a CSV file.

Here's a brief explanation of each route:

/operations:

Accepts query parameters x and y from a GET request.
Calls functions to perform arithmetic operations (sum, subtraction, multiplication, division) using the provided x and y.
Returns the results of the operations as a JSON response.

/words:

Accepts a file uploaded via a GET request.
Calls a function to calculate the word count from the content of the uploaded file.
Returns the word count as a JSON response.

/average:

Accepts a file and a column name as query parameters from a GET request.
Calls a function to calculate the average from the specified column in the uploaded CSV file.
Returns the average as a JSON response.

The exception handling in each route ensures that appropriate error messages are returned in case of exceptions.

I've encapsulated my Flask application within a Docker container using a Dockerfile.

In my Dockerfile, I've defined the necessary steps to build the Docker image. This image contains all the dependencies, configurations, and my Flask application code. You can then use the Docker image I've created to start a container that runs my application, independent of your local environment.
