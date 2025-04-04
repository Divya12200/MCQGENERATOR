import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.mcqgenerator.logger import logging

logging.info("hi, i am going to start my execution...")