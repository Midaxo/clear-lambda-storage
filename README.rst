Clear Lambda code storage
===========================


Motivation
-----------
AWS limits the total code storage for Lambda functions to `75GB <https://docs.aws.amazon.com/lambda/latest/dg/limits.html#limits-list>`_.

The main reason of reaching such size is because for every deployment of existing function, AWS stores the previous version ("qualifier").

Usually, when you reach that point, you want to remove old version.
This tool will help you to!

⚡️ AWS SAM CLI usage
----------------------
This project now supports deployment using the AWS SAM CLI.

**Prerequisites:**
- AWS SAM CLI installed (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- An S3 bucket for deployment artifacts

**Deploy steps:**

.. code-block:: bash

    git clone https://github.com/epsagon/clear-lambda-storage
    cd clear-lambda-storage/
    make build
    make deploy

**Schedule:**
The Lambda is scheduled to run every Sunday at 12:00pm UTC by default. You can change the schedule by editing the `Schedule` property in `template.yaml`:

.. code-block:: yaml

    Events:
      ScheduledEvent:
        Type: Schedule
        Properties:
          Schedule: cron(0 12 ? * SUN *)
