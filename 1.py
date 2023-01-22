from utils import all, one



querry =  f"""
   SELECT * FROM netflix
   WHERE title = 'The InBESTigators'
   ORDER BY date_added desc
   """

print(all(querry))