from .basemodel import BaseModel


class Amenity(BaseModel):
    """Represents an amenity in the hbnb app."""

    def __init__(self, name=""):
        """Initialize amenity with name."""
        super().__init__()
        self.name = name
        self.validator()

    def __str__(self):
        """Return a string amenity."""
        return (f"[Amenity] ({self.id}) {self.name}")

    def validator(self):
        if not self.name or len(self.name) > 50:
            raise ValueError("Name must be a required with a maximum of " 
                             "50 characters")
