# AWS-Asset-Conversion
A collection of scripts to move our assets from Netsuite to AWS and then some.

# Using upload-files
## Set Up
### Python 3 is required to run this script. Navigate to [python.org](https://www.python.org/downloads/) and download the latest version.

### Install [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
```
$ pip install boto3
```
### Install [AWS CLI](https://github.com/aws/aws-cli), if you don't already have it installed.
```
$ sudo pip install awscli
```
### Configure your AWS credentials
```
$ aws configure
AWS Access Key ID: foo
AWS Secret Access Key: bar
Default region name [us-west-2]: us-west-2
Default output format [None]: json
```

## Run in REPL

### Start REPL with imported file
```
$ python3 -i scripts/upload-files.py
```

### Call the function
```
>>> read_file('test.csv', 'bucket.name.com')
```

