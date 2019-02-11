# slacky

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/76578ffcfd130b117eb9/maintainability)](https://codeclimate.com/github/mikeee/slacky/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/76578ffcfd130b117eb9/test_coverage)](https://codeclimate.com/github/mikeee/slacky/test_coverage)
[![Build Status](https://travis-ci.org/mikeee/slacky.svg?branch=master)](https://travis-ci.org/mikeee/slacky)

IFTTT->Slack as an alternative to single channel webhooks. Written in Python utilising the Tornado framework

## Usage

### Docker

To start this project you'll need to clone the repository, navigate to it and ensure that you have docker & compose installed. Dockerfile and compose template has been provided - use the following command to build the image and run an instance.

```bash
docker-compose up
```

### Standalone

You can run the project using just python by making sure that you have the required version (3.7) installed.

Install *pipenv* which is used for dependancy management.

```bash
pip install pipenv
```

Run the project.

```bash
python helloworld.py
```

## Testing/coverage

Testing

```bash
python helloworld_test.py
```

Coverage

```bash
pip install coverage
```

```bash
coverage run helloworld.py
```

## Licence

Released under the MIT License - For full details check out [LICENSE](https://github.com/mikeee/slacky/blob/master/LICENSE)