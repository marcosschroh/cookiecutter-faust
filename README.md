Cookiecutter Faust
===================

Features
---------

* For Faust 1.5.4
* Python 3.7
* Docker and docker-compose support
* Useful commands included in Makefile
* project skeleton is defined as a medium/large project according to [faust layout](https://faust.readthedocs.io/en/latest/userguide/application.html#projects-and-directory-layout)
* The `setup.py` has the entrypoint to resolve the [entrypoint problem](https://faust.readthedocs.io/en/latest/userguide/application.html#problem-entrypoint)


Usage
------

Let's pretend you want to create a Faust project called "super faust".

First, install `Cookiecutter`.

```bash
pip install "cookiecutter>=1.4.0"
```

Now run it against this repo::

```
cookiecutter https://github.com/marcosschroh/cookiecutter-faust
```

You'll be prompted for some values. Provide them, then a Faust project will be created for you
based on the convention of medium/large project mentioned above


Answer the prompts with your own desired options_. For example:

```
project_name [My Awesome Faust Project]: super faust
project_slug [super_faust]:
description [My Awesome Faust Project!]:
long_description [My Awesome Faust Project!]:
author_name [Marcos Schroh]:
author_email [marcos-schroh@gmail.com]:
version [0.1.0]:
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]:
use_pycharm [n]:
use_docker [n]: y
include_docker_compose [n]: y
include_page_view_tutorial [n]: y
worker_port [6066]:
kafka_server_environment_variable [KAFKA_BOOTSTRAP_SERVER]:
Select faust_loglevel:
1 - CRITICAL
2 - ERROR
3 - WARNING
4 - INFO
5 - DEBUG
6 - NOTSET
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]: 4
```

Enter the project and take a look around:

```
cd super_faust/
ls
```

Create a git repo and push it there:

```
git init
git add .
git commit -m "first awesome commit"
git remote add origin git@github.com:marcosschroh/super-faust.git
git push -u origin master
```

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?
