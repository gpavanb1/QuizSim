# QuizSim

![Made with Love in India](https://madewithlove.org.in/badge.svg) 
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
[![Downloads](https://pepy.tech/badge/quizsim)](https://pepy.tech/project/quizsim)

# How to install and execute?

Just run 
```
pip install quizsim
```

The following program illustrates a basic example
```python
from quizsim import runQuiz

print(runQuiz())
```

## How to test?

You can run the default tests using

```
python -m unittest
```

Code coverage can be obtained using [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/) as follows

```
coverage run --source=quizsim -m unittest
```

You can obtain a quick report on the coverage as follows
```
coverage report --show-missing
```

## Whom to contact?

Please direct your queries to [gpavanb1](http://github.com/gpavanb1)
for any questions.
