PYTHON = python3
.PHONY: run lint clean
#muc tieu mac dinh: chay main.py

run:
	@echo "running main.py..."
	$(PYTHON) main.py
#muctieu kiem tra cu phap:
lint:
	@echo "checking code quality with pylint..."
	$(PYTHON) -m py_compile main.py
#muc tieu cai dat yeu cau       
clean:
	@echo "cleaning up cache list..."
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -rf {} +

