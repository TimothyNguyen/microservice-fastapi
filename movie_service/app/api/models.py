from typing import List, Optional
from pydantic import BaseModel

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

class MovieOut(MovieIn):
    id: int

class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts: Optional[List[str]] = None

# Here MovieIn is the base model that you use to add the movie to 
# the database. You have to add the id to this model while getting 
# it from the database, hence the MovieOut model. MovieUpdate 
# model allows us to set the values in the model to be optional 
# so that while updating the movie only the field that needs to 
# be updated can be sent.

# Now, head over to the browser documentation site and start 
# playing with the API.

'''
class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]
'''