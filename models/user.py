
#!/usr/bin/python3
"""The class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """The class User that inherit BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
