import os
import sys
import json
import shutil
import re
import openpyxl
from bs4 import BeautifulSoup

# Paths
BASE_DIR = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SARAV_XLSX = r"D:\YouTube\Sarav AI\YouTube_Shorts_Schedule_Ep01_to_100_Copy.xlsx"
SARAV_COVERS_DIR = r"D:\YouTube\Sarav AI\saravxai6-100\covers"
SARAV_SHORTS_JSON = r"D:\Websites\SaravsWorld\public\ai\shorts_data.json"

LOOP_XLSX = r"D:\sdrv\inklingtales\TheLoop_Shorts_Schedule_Ep01_to_300.xlsx"
LOOP_COVERS_DIR = r"D:\sdrv\inklingtales\covers"

SIDISHA_HTML = r"D:\StorytellingArt\SidIsha-HomeWasYou\SidIsha_Instagram_Days_01_to_30.html"
SIDISHA_SLIDE1_DIR = r"D:\StorytellingArt\SidIsha-HomeWasYou\images\stamped"
SIDISHA_SLIDE2_DIR = r"D:\StorytellingArt\SidIsha-HomeWasYou\images\carousel_slide2"

INKLING_IG_HTML = r"D:\sdrv\inklingtales\InklingTales_Instagram_Ep51_to_100.html"

print("All source paths configured.")
