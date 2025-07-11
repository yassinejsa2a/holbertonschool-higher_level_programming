#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
<<<<<<< HEAD
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
=======
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], 
        sys.argv[2], 
        sys.argv[3]), 
        pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
>>>>>>> 81e32a4ae05c85348b2bc3d1fb9671c67fda66d2
