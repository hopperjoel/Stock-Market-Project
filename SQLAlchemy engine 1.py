# Attempt 1 at establishing SQLAlchemy engine

import sqlalchemy as sa

engine = create_engine("mysql:///?User=root&Password=Elmakano132!&Database=investing&Port=3306")

#sqlalchemy.ext.declarative.declarative_base  goes somewhere

base = declarative_base()
class Orders(base):
	__tablename__ = "exchange_history"
	ticker = Column(String,primary_key=True)
	date = Column(String)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adj_close = Column(Float)
    volume = Column(Float)
    
#using the query method
"""    
engine = create_engine("mysql:///?User=root&Password=Elmakano132!&Database=investing&Port=3306")
factory = sessionmaker(bind=engine)
session = factory()
for instance in session.query(Orders).filter_by(ShipCountry="USA"):
	print("ShipName: ", instance.ShipName)
	print("Freight: ", instance.Freight)
	print("---------")
    
"""
    
#for an execute
"""   
Orders_table = Orders.metadata.tables["Orders"]
for instance in session.execute(Orders_table.select().where(Orders_table.c.ShipCountry == "USA")):
	print("ShipName: ", instance.ShipName)
	print("Freight: ", instance.Freight)
	print("---------")
"""