python -m venv ./venv
START /B .\venv\Scripts\activate
TIMEOUT /T 3
START /wait pip install pyside2
mkdir .\venv\Lib\site-packages\PySide2\bin
xcopy .\venv\Scripts\pyside2-uic.exe .\venv\Lib\site-packages\PySide2\bin\uic.exe