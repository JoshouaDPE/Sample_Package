# Python_Libs

## Summary
Repository for Steinemann DPE Pyhton libraries

## Working with python packages
Following step has to be taken to generate a new stdpe python package locally.

```
pip install -e .
```

## Install the package from GitHub

```
pip install "git+https://github.com/SteinemannDPE/Python_Libs.git#egg=stdpe"
```


**Links**

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/) <br />
- [GitHub sample project](https://github.com/pypa/sampleproject) <br />
- [tutorial](https://www.youtube.com/watch?v=DhUpxWjOhME&ab_channel=mCoding)
- [Build you first python project](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)
- [Setup Tools](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)




**Deprecated**
- Create a distribution
```
python setup.py sdist
```

- Install the package locally
```
python setup.py install
``` 