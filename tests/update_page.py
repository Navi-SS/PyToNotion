from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

page_id = "950d0f16-ab47-432f-afff-ca7fd6921ed9"
content = {
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": "Titulo de prueba"
                        }
                    }
                ]
            }
        }
    }
# print(notion.get_pages())
page = notion.update_page(page_id, content)
print(page)