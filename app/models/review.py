from .basemodel import BaseModel
from app.models.place import Place
from app.models.user import User


class Review(BaseModel):
    def __init__(self, text, rating, user_id, place_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self._user_id = user_id
        self._place_id = place_id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value and len(value) > 50:
            raise ValueError("Text must be less than 50 characters")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not value or not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

@property
def user_id(self):
    return self._user_id
    
@user_id.setter
def user_id(self, value):
    if not isinstance(value, User):
        raise ValueError("User not found, please enter a valid username")
    self._user_id = value

@property
def place_id(self):
    return self._place_id
    
@place_id.setter
def place_id(self, value):
    if not isinstance(value, Place):
        raise ValueError("Place not found, please enter a valid place")
    self._place_id = value