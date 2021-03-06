# python-boilerplate-script
[![building](https://img.shields.io/travis/fernandojunior/python-boilerplate-script.svg)](https://travis-ci.org/fernandojunior/python-boilerplate-script)

Boilerplate to create a [command line script](http://python-packaging.readthedocs.org/en/latest/command-line-scripts.html#command-line-scripts) project with a Python module. More information at [@fernandojunior/python-boilerplate](https://github.com/fernandojunior/python-boilerplate).

```sh
$ script_name Hello World
Hello World
```

## Features

* [coverage.py](https://coverage.readthedocs.org/) - Code coverage measurement.
* [Flake8](https://flake8.readthedocs.org/) - The modular source code checker: pep8, pyflakes and co.
* [pytest](http://pytest.org/) - A mature full-featured Python testing tool.
* [setuptools](https://pythonhosted.org/setuptools/setuptools.html) - Easily download, build, install, upgrade, and uninstall distribution packages.
* [tox](https://tox.readthedocs.org/) - Auto builds and tests distributions in multiple Python versions using virtualenvs.

## Structure

```sh
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── MANIFEST.in
├── README.md
├── requirements
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt
├── script_name.py  # The core code of the project
├── setup.cfg
├── setup.py
├── tests.py
└── tox.ini
```

More datails [here](https://github.com/fernandojunior/python-boilerplate#structure).

## Keywords

* author_name - Full name of the author.
* github_username - GitHub username.
* project_name - Short name of your project using [slug style](https://en.wikipedia.org/wiki/Semantic_URL#Slug).
* script_name - Name of the script using [PEP8 style](https://www.python.org/dev/peps/pep-0008/#package-and-module-names).

You can use your preferred text editor or IDE to find the keywords. In [Sublime](https://www.sublimetext.com/) and [Atom](https://atom.io/) this is done by `Ctrl + Shift + F`.

## Contributing

See [CONTRIBUTING](/CONTRIBUTING.md).

## License

[![CC0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The MIT License.

-

Copyright (c) 2016 [Fernando Felix do Nascimento Junior](https://github.com/fernandojunior/).
