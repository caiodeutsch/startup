### Requirements

- Python 3.8.9
- aws-cli/2.4.12
- Terraform v1.1.3

### Instructions for Terraform
* Create and IAM User with admin permissions
* Install and configure AWS-CLI with credentials from user created above
* Install Terraform
* Run terraform commands below
```shell script
  cd terraform
  terraform plan
  terraform apply
```

### Instructions for Python Requirements
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
  python run.py
```
