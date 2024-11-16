from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

page_id = "6e7476d376a64d419bb3d2afa0169bce"
# print(notion.get_pages())
page = notion.archive_page(page_id)
print(page)