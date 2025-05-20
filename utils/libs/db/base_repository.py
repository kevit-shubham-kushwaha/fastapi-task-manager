from datetime import datetime
class BaseRepository:
  """
      Base repository class that provides a common interface for all repositories.
  """   

  def __init__(self, collection):
      """
      Initialize the repository with a database connection.

      Args:
      db: The database connection object.
      """
      self.collection = collection
      
  
  def get_name(self):
    return self.collection.name
        
  
  def insert_one(self,data):
    '''
      Insert Single Document to Databse
    '''
    return self.collection.insert_one(data)
    
    
  def insert_many(self,data):
    '''
      Insert Multiple Documents to Databse
    '''
    return self.collection.insert_many(data)
    
   
  def find_one(self,query):
    '''
      Find Single Document from Databse
    '''
    return self.collection.find_one(query)
    
  def find_many(self,query):
    '''
      Find Multiple Documents from Databse
    '''
    return self.collection.find(query)
  
  def update_one(self,query,data):
    '''
      Update Single Document in Databse
    '''
    return self.collection.update_one(query, data)
  
  def update_many(self,query,data):
    '''
      Update Multiple Documents in Databse
    '''
    return self.collection.update_many(query, data)
  
  