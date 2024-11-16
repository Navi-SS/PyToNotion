from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))
content = {
            "paragraph": {
                "rich_text": [{
                    "type": "text", 
                    "text": { "content": "Esto es una gran prueba"}
                }]
            }
        }
block = "ad658c3f-b3e1-4511-ad8c-ccec45bcc950"
block = notion.update_block(block, content)
print(block)