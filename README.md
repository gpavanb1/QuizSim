# QuizSim

![Made with Love in India](https://madewithlove.org.in/badge.svg) 
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)
[![Downloads](https://pepy.tech/badge/quizsim)](https://pepy.tech/project/quizsim)

## How to install and execute?

Just run 
```
pip install quizsim
```

The following program illustrates a basic example
```python
from quizsim import runQuiz

print(runQuiz())
```

## Parameters

* NUM_QUESTIONS - Number of questions in the quiz (default: 30)
* TEAM_STRENGTH - List giving chance (between 0 and 1) that team answers a question correctly (default: [1.0, 0.0])
* POUNCE_DARE - List giving chance (between 0 and 1) that team pounces on a question (default: [1.0, 0.0])
* CAN_POUNCE - Boolean whether pounce is allowed in quiz (default: True)
* BOUNCE_TYPE - When nobody answers the previous question on bounce, the direct moves to either next team to previous (Bengaluru) or same team as previous gets it (Chennai) - (default: Bengaluru)
* POUNCE_RIGHT - Points for right answer on pounce (default: 15)
* POUNCE_WRONG - Points for wrong answer on pounce (default: -10)
* BOUNCE_RIGHT - Points for right answer on bounce (default: 10)

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
