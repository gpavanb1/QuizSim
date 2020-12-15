from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='QuizSim',
      version='0.1',
      description='Play with the rules of quizzing',
      url='https://github.com/gpavanb1/QuizSim',
      author='gpavanb1',
      author_email='gpavanb@gmail.com',
      license='MIT',
      packages=["quizsim"],
      install_requires=["numpy"],
      long_description=long_description,
      long_description_content_type= "text/markdown",
      classifiers=[
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
      ],
      keywords='quiz trivia python simulation datascience',
      project_urls={  # Optional
        'Bug Reports': 'https://github.com/gpavanb1/QuizSim/issues',
        'Source': 'https://github.com/gpavanb1/QuizSim/',
      },
      zip_safe=False)