## Machine learning project

setup.py -> builds the application as a package itself
the SRC folder behaves as a package

requirements.txt -> takes the mentioned packages in the file and installs when the setup.py is installed

init_.py -> in setup.py the find_packages funtion will go search for this init file and install as its package itself and builds.
so if i install requirements.txt automatically it calls the setup.py and installs everything as package.