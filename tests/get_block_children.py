from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

page_id = "6f0b2835f764490d8a7fd7b3e4a768cd"
block = notion.get_block_children(page_id)
print(block)