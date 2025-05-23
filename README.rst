Clear Lambda code storage
===========================


Motivation
-----------
AWS limits the total code storage for Lambda functions to `75GB <https://docs.aws.amazon.com/lambda/latest/dg/limits.html#limits-list>`_.

The main reason of reaching such size is because for every deployment of existing function, AWS stores the previous version ("qualifier").

Usually, when you reach that point, you want to remove old version.
This tool will help you to!


Setup
-----
Install via pip

.. code-block:: bash

    pip install clear-lambda-storage
    clear_lambda_storage

Install via source

.. code-block:: bash

    git clone https://github.com/epsagon/clear-lambda-storage
    cd clear-lambda-storage/
    pip install -r requirements.txt
    python clear_lambda_storage.py


Advanced usage
---------------

Provide credentials:

.. code-block:: bash

    python clear_lambda_storage.py --token-key-id <access_key_id> --token-secret <secret_access_key>

Alternate usage:

.. code-block:: bash

    python clear_lambda_storage.py --profile <profile_id> --num-to-keep 2

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
    pip install -r requirements.txt
    sam build
    sam deploy --guided

The first time you run `sam deploy --guided`, you will be prompted for parameters such as your S3 bucket and region. These will be saved in `samconfig.toml` for future deployments.

**Schedule:**
The Lambda is scheduled to run every Sunday at 12:00pm UTC by default. You can change the schedule by editing the `Schedule` property in `template.yaml`:

.. code-block:: yaml

    Events:
      ScheduledEvent:
        Type: Schedule
        Properties:
          Schedule: cron(0 12 ? * SUN *)
