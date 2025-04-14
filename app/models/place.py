from .basemodel import BaseModel
from .user import User
from .amenity import Amenity


class Place(BaseModel):
    def __init__(self, title, description, price, latitude,
                 longitude, owner_id, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = amenities or []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be an Amenity instance")
        self.amenities.append(amenity)

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("title is required")
        if len(value) > 100:
            raise ValueError("title must be less than 100 characters")
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("price must be greater than 0")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if not (90 >= value >= -90):
            raise ValueError("Latitude must be beewteen 90 and -90")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if not (180 >= value >= -180):
            raise ValueError("longitude must be beewteen 180 and -180")
        self.__longitude = value

    @property
    def owner(self):
        return self.__owner_id

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("owner must be a User instance")
        self.__owner_id = value
