from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

block_id = "6f0b2835f764490d8a7fd7b3e4a768cd"
comments = notion.get_comments(block_id)
print(comments)