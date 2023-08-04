"""
This module contains the class DBStorage which is a class similar to FileStorage
but it will be interacting with a SQL database instead of JSON files.
"""
import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and retrieves environment variables"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database),
        pool_pre_ping=True
        )
        # start session??
        running_environment = os.getenv("HBNB_ENV")
        if running_environment == "test":
            Base.MetaData.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            print("Querying all objects")
            object_list = self.__session.query(
            User, State, City, Amenity, Place, Review).all()
        else:
            print(f"Querying objects of class {cls}")
            object_list = self.__session.query(cls).all()

        print(f"Retrieved {len(object_list)} objects from the database")

        new_dict = {}
        for obj in object_list:
            obj_key = (obj.to_dict()['__class__'] + '.' + obj.id)
            # can we use to_dict on these obj?
            new_dict[obj_key] = obj

        print(f"Returning a dictionary with {len(new_dict)} entries")

        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        #self.__session = Session()
