
Find And Move
======

CLI tool that scrapes through all the text files in the specified directory(Defaults to the current directory by default) and then searches through each file for the provided keyword. All the files that contain the keyword are moved to a folder with the name of a keyword(A New folder will be created if it does not exist).

Installation
============

Clone this repo,change directory to mover directory conatining setup.py

```
git clone https://github.com/Warlord-K/FindAndMoveCLI.git
```

```
cd mover
```
Install setuptools if not already installed

```
pip install setuptools
```

Run the following command to perform a local Install
```
python setup.py install
```


Usage
============

With Path:

```
fam --keyword KEYWORD --path PATH
```

Without Path(Not Recommended):
Defaults to the current directory
```
fam --keyword KEYWORD
```

