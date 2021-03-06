rm -rf dist
rm -rf build
rm main.spec
wine ~/.wine/drive_c/Python27/python.exe pyinstaller-2.0/pyinstaller.py ../main.py
rm -rf client_only_modules
python makeclientonlycode.py ../modules/
cp -ir client_only_modules dist/modules
cp -r ../extern_modules dist/extern_modules
cp -r ../data dist/data
cp ../extern_modules/pymunk/libchipmunk.so dist/libchipmunk.so
cp ../extern_modules/pymunk/libchipmunk64.so dist/libchipmunk64.so
cp ../extern_modules/pymunk/chipmunk.dll dist/chipmunk.dll
cp ../thm.cfg dist/thm.cfg
