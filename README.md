# Under & Over Game

## Запуск игры на разных платформах

### 1. Web-версия (работает на всех платформах)

1. Установите Python 3.7+ и pip
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Соберите веб-версию:
```bash
make web
```
4. Запустите веб-сервер и откройте браузер по адресу http://localhost:8000

### 2. Windows

1. Установите Python 3.7+ и pip
2. Установите необходимые инструменты:
```bash
pip install -r requirements.txt
pip install pyinstaller
```
3. Соберите исполняемый файл:
```bash
make windows
# или вручную:
pyinstaller --onefile --windowed --icon=assets/icon.ico game.py
```
4. Запустите игру через `dist/game.exe`

### 3. Linux

1. Установите зависимости:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev
# Fedora
sudo dnf install python3 python3-pip python3-devel
```
2. Установите инструменты сборки:
```bash
pip3 install -r requirements.txt
pip3 install pyinstaller
```
3. Соберите исполняемый файл:
```bash
make linux
# или вручную:
pyinstaller --onefile game.py
```
4. Запустите игру:
```bash
./dist/game
```

### 4. Android

1. Установите необходимые инструменты:
```bash
pip install buildozer
```
2. Инициализируйте buildozer:
```bash
buildozer init
```
3. Соберите APK:
```bash
make android
# или вручную:
buildozer android debug
```
4. Установите полученный APK-файл из папки `bin/` на устройство

## Сборка из исходников

Для сборки из исходников используйте команды:
```bash
# Сборка для всех платформ
make all

# Сборка для конкретной платформы
make windows
make linux
make android
make web
```

## Требования к системе

### Для разработки
- Python 3.7 или выше
- pip
- make (опционально)
- 1GB RAM
- 500MB свободного места

### Для запуска
- Windows 7/10/11 (64-bit)
- Ubuntu 18.04+ / Fedora 30+
- Android 7.0+
- 512MB RAM
- 100MB свободного места