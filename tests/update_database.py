from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

query = {
    "title": [
        {
            "text": {
                "content": "Prueba"
            }
        }
    ],
    "properties":{
        "Prueba": { "rich_text": {} } 
    }
}

database_id = "46368b318040455d9bbee4f0355cdbca"
database = notion.update_database(database_id, query)
print(database)