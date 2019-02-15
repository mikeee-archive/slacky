# slacky

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/76578ffcfd130b117eb9/maintainability)](https://codeclimate.com/github/mikeee/slacky/maintainability)

IFTTT->Slack as an alternative to single channel webhooks. Written in Python utilising the Tornado framework

## Usage

### Configuration

Create a new `config.yml` file from the example and add your slack token which has the `chat:write` permission.

### Docker

To start this project you'll need to clone the repository, navigate to it and ensure that you have docker & compose installed. Dockerfile and compose template has been provided - use the following command to build the image and run an instance.

```bash
docker-compose up --build
```

### Standalone

You can run the project using just python by making sure that you have the required version (3.7) installed.

Install *pipenv* which is used for dependancy management.

```bash
pip install pipenv
```

Run the project.

```bash
python run.py
```

### Making Requests

Default route to call from IFTTT is: POST `your.hostname/slack/message`

```json
{
    "channel":"test",
    "text":"test",
    //Optional
    "as_user":"user"
}
```

## Licence

Released under the MIT License - For full details check out [LICENSE](https://github.com/mikeee/slacky/blob/master/LICENSE)