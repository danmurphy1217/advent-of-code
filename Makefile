clean:
	find . -type f -name '*.pyc' -exec rm -rf {} \;
	find . -type f -name '*.DS_Store' -exec rm -rf {} \;
	find . -type dir -name '__pycache__' -delete;