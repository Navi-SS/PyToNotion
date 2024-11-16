from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

data = {
    "discussion_id": "f2f0213b-1611-4a13-b8d7-efb2951d21f0",
    "rich_text": [
        {
            "text": {
                "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
                "link": {
                    "type": "url",
                    "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
                }
            }
        }
    ]
}

comments = notion.add_comments_discussion(data)
print(comments)