# Forms
Government forms to be filled via GUI


Instructions to build application:

Clone into the repository using git on command line:

```git clone https://github.com/nepoz/Forms.git```

!FROM WITHIN THE DIRECTORY WHICH HOLDS REPO FIILES:

Download all dependencies using pip:

```pip3 install -r requirements.txt```

Run cx_Freeze build:

```python3 cx_setup.py build```

The compiled .exe and its dependencies will be in the 'build' folder. Moving the main .exe out of this folder will cause the
application to not launch (as important libraries and files are in the same folder). Use shortcuts if you want to access the
application from other places.
