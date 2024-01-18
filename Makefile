.PHONY: run
run:
	@python3 application/app.py

.PHONY: install-on-mac
install-on-mac:
	@pip3 install -r requirements.txt

.PHONY: install
install:
	@pip install -r requirements.txt
