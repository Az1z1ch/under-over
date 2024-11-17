# Переменные
PYTHON = python3
PIP = pip3
VENV = venv
BIN = $(VENV)/bin

# Основные команды
.PHONY: all clean test install run

all: install test

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install -r requirements.txt

install: $(VENV)

test: install
	$(BIN)/python tests/test_game.py

run-windows: install
	$(BIN)/python game.py

run-linux: install
	$(BIN)/python game.py

run-web: install
	$(BIN)/python game.py

clean:
	rm -rf $(VENV)
	rm -rf logs/*.txt
	rm -rf __pycache__
	rm -rf tests/__pycache__ 