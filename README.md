### Requirements

- Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
- aws-cli/2.4.12 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
- Terraform v1.1.3 on windows_amd64

### Instructions for Terraform
* Create and IAM User with admin permissions
* Install and configure AWS-CLI with credentials from user created above
* Install Terraform
* Run terraform apply
```shell script
  cd terraform
  terraform plan
  terraform apply
```

### Instructions for Python Requirements
* Run the seeder
```shell script
  pip install -r requirements.txt
  pip install pymysql
```

### Instructions for Seeder
* Run the seeder
```shell script	
  python db_seed.py
```

### Instructions for running the Flask Application
* Start the flask application
```shell script	
  pip install -r requirements.txt
  pip install pymysql
  python run.py
```
