run:
	python3 main.py

deploy: 
	ngrok http 5000

start:
	make -j2 run deploy

