import pymongo
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv


load_dotenv()
DB_PASS = os.getenv('DB_PASS')
url = f"mongodb+srv://contrailpy:{DB_PASS}@cluster0.xpysx.mongodb.net/"
client = pymongo.MongoClient(url)
db = client['portfolio']

# <--- Skills Collection Management -->
skills = db['skills']
skillset = skills.find()
print((skillset[1]['frontend']).split(","))

# <-- projects Collection Management -->
raw_projects = db['projects']
projects = list(raw_projects.find())

# filter = {"_id":ObjectId('672790caff384ce856517e51')}
# update = {
#     "$set": {
#         "git": "https://github.com/lsahmed/contrail"
#     }
# }
# result = projects.update_one(filter ,update)


# if result.modified_count > 0:
#     print(f'Document with ID  updated successfully.')
# else:
#     print(f'No document found with ID  or no changes made.')