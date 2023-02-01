#ost.py
import os
try:
	os.rename("D:\\timepass","D:\\kvr")
	print("floder is remove")
except FileNotFoundError:
	print("file not found")