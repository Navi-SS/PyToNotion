from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

database_id = "46368b318040455d9bbee4f0355cdbca"
database = notion.get_database(database_id)
print(database)