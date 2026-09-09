from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SIMULATION = os.getenv("SIMULATION")

if SIMULATION == True:
    MAX_OUTPUT_TOKENS_SEARCH = 1024
else:
    MAX_OUTPUT_TOKENS_SEARCH = 3000
