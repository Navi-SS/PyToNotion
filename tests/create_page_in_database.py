from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "Name of person"
                    }
                }
            ]
        },
        "Status": {
            "multi_select": [
                    {
                    "name": "Test"
                }
            ]
        },
        "Info": {
            "rich_text": [
                {
                    "text": {
                        "content": "Text for test"
                    }
                }
            ]
        }
    }
database_id = "46368b318040455d9bbee4f0355cdbca"
page = notion.create_page_in_database(database_id, properties)
print(page)