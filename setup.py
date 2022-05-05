
from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Search for a keyword in various text files in a directory \
      and move those files to a new directory'
  
setup(
        name ='find_and_move',
        version ='1.0.0',
        author ='Yatharth Gupta',
        author_email ='cse210001083@gmail.com',
        url ='https://github.com/Warlord-K/FindAndMoveCLI',
        description ='Finds Keyword in files and moves them',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'fam = mover.main:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='Find and Move by Yatharth Gupta',
        install_requires = requirements,
        zip_safe = False
)
