import requests
import time

if __name__ == "__main__":
	while True:
		time.sleep(5)
		print("Try")
		requests.get('http://0.0.0.0:80/api/checkOnUser')
