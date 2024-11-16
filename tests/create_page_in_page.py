from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

properties = {
            "title": [
                {
                    "text": {
                        "content": "Test of a page in a page"
                    }
                }
            ]
        }
page_id = "950d0f16ab47432fafffca7fd6921ed9"

page = notion.create_page_in_page(page_id, properties)
print(page)