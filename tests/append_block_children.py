from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

content ={
        "children": [
            {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                {
                    "type": "text",
                    "text": {
                    "content": "Lacinato kale"
                    }
                }
                ]
            }
            },
            {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                {
                    "type": "text",
                    "text": {
                    "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                    "link": {
                        "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                    }
                    }
                }
                ]
            }
            }
        ]
        }

block = "ad658c3f-b3e1-4511-ad8c-ccec45bcc950"
block = notion.append_block_children(block, content)
print(block)