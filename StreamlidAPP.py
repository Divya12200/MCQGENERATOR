import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.logger import logging
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.mcqgenerator import generate_evaluate_chain


