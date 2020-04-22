from setuptools import setup
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
     name='nsgvalidation',  
     version='0.2',
     py_modules=["nsgvalidation"] ,
     package_dir={'': 'src'},
     author="Sahil Arora",
     author_email="saharora@ciena.com",
     description="A Utility package for Azure NSG validation",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.8",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.5',
 )
