HBNB - Web Application Backend
In this project, we have implemented the phase of the application based on the design developed in the previous part. We have focused on the Persistence, Business Logic, and API Layers. This project is built using Python and Flask.
We created the structure of the project, developed the classes that define the business logic, and implemented the API endpoints.
We also manage users, places, reviews, and amenities.

Project Structure

hbnb/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   │   ├── basemodel.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
Explanation of Key Directories and Files
app/: Contains the main application components

api/: Handles API routing and versioning

models/: Defines business logic classes for User, Place, Review, and Amenity

services/: Implements the facade pattern to act as a bridge between layers

persistence/: Contains the in-memory repository that can later be swapped for a database

run.py: Entry point of the application

config.py: Configuration settings for different environments

requirements.txt: List of libraries needed to run the project

Business Logic Layer Explanation
User
The user entity has a unique ID and can create or interact with places, reviews, and amenities.

Create a User                                                                                                                                                                                               
POST /api/v1/users
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
Response:

{
  "id": "uuid",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com"
}
201 Created

400 Bad Request if the email already exists

Retrieve a User by ID

GET /api/v1/users/<id>
200 OK

404 Not Found if the user does not exist

List All Users

GET /api/v1/users
200 OK

Update a User

PUT /api/v1/users/<id>
Content-Type: application/json

{
  "first_name": "Jane",
  "email": "jane.doe@example.com"
}
200 OK

404 Not Found

400 Bad Request for invalid data

Place
A place is created by a user and can have reviews and amenities.

Create a Place

POST /api/v1/places
Content-Type: application/json

{
  "title": "Cozy Apartment",
  "description": "A nice place to stay",
  "price": 100.0,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "owner_id": "uuid"
}
201 Created

400 Bad Request

Review
Users write reviews to rate places.

Create a Review

POST /api/v1/reviews
Content-Type: application/json

{
  "text": "Great place!",
  "rating": 5,
  "user_id": "uuid",
  "place_id": "uuid"
}
201 Created

400 Bad Request

Amenity
Amenities are created by users and added to places.

Create an Amenity

POST /api/v1/amenities
Content-Type: application/json

{
  "name": "Wi-Fi"
}
201 Created

400 Bad Request

Setup and Installation
Clone the repository

git clone https://github.com/Kraoshin/holbertonschool-hbnb.git
Install requirements

pip install -r requirements.txt
Run the application

python run.py