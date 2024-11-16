from pyNotion.pyNotion import pyNotion
import os
from dotenv import load_dotenv

load_dotenv()

notion = pyNotion(os.getenv("API_KEY"))

block = "9d08382f-8bf7-47c6-8dbe-4a3369d438f4"
block = notion.delete_block(block)
print(block)