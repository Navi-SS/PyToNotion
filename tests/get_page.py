from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

page_id = "6f0b2835-f764-490d-8a7f-d7b3e4a768cd"
page = notion.get_page(page_id)
print(page)