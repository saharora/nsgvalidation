from setuptools import setup
setup(
     name='nsgvalidation',  
     version='0.2',
     py_modules=["nsgvalidation"] ,
     package_dir={'': '.'},
     author="Sahil Arora",
     author_email="saharora@ciena.com",
     description="A Utility package for Azure NSG validation",
     install_requires = [
         "pyhcl==0.4.2",
         "glob3",
     ],
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
