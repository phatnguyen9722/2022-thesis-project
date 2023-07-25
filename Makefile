.PHONY: all
all: black copyright

.PHONY: black	
black:
	@black .
	@echo "All Done!"