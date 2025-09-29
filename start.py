import os

from dotenv import load_dotenv

def load_env():
    load_dotenv()
    if os.getenv("TEST_PRINT") == "True" or os.getenv("TEST_PRINT") == "true":
        print(f"Test Print: {os.getenv("TEST_PRINT")}")
        print(f"API Port: {os.getenv("PORT")}")
        print(f"API Host: {os.getenv("HOST")}")
        print(f"Debug: {os.getenv("DEBUG")}")