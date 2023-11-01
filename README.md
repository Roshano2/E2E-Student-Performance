## Machine learning project

setup.py -> builds the application as a package itself
the SRC folder behaves as a package
(basically a python script to ensure that the program is installed correctly iwth the aid of pip or we can use this to install any module without having to call setup.py directly)

requirements.txt -> takes the mentioned packages in the file and installs when the setup.py is installed

init_.py -> in setup.py the find_packages funtion will go search for this init file and install as its package itself and builds.
so if i install requirements.txt automatically it calls the setup.py and installs everything as package.

OneHotEncoding for categorical variables
