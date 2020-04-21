import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='nsgvalidation',  
     version='0.2',
     scripts=['nsgvalidation/nsgvalidation'] ,
     author="Sahil Arora",
     author_email="saharora@ciena.com",
     description="A Utility package for Azure NSG validation",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/saharora/nsgvalidation",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.6',
 )
