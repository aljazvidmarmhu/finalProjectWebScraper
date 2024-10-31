from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mysql.connector
from mysql.connector import Error
from OpenPage import OpenPage
from InglesClick import InglesClick
from StoreToDatabase import StoreToDatabase
from GetAllProducts import GetAllProducts
from PublixClick import PublixClick
from selenium.webdriver.common.action_chains import ActionChains