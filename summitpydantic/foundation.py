from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

def RunFoundation(run: bool):
    if not run:
        return
    
    user = {'id': 102, 'name': "Usiey", 'is_active': True}

    result = User(**user)
    print(result)