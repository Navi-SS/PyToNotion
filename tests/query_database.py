from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

query = {
    "filter": {
        "property": "Status",
        "multi_select": {
            "contains": "Reading"
        }
    },
    "sorts": [
        {
        "property": "Name",
        "direction": "ascending"
        }
    ]
}

database_id = "46368b318040455d9bbee4f0355cdbca"
database = notion.query_database(database_id, query)
print(database)