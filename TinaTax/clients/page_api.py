BASE_URL = "https://www.tinataxresolution.com/"

class Page:
   def __init__(self, session):

      self.session = session

   def get_website(self):

      return self.session.get(BASE_URL)
   


   

