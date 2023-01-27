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

### Starting the application
* the userdata.tpl will start the application, no need to run the script bellow
```shell script
#!/bin/bash
apt-get update -y
apt-get install -y python3-pip
git clone https://github.com/caiodeutsch/startup.git
cd startup/
pip3.10 install -r requirements.txt
nohup python3.10 run.py &
```

### Instructions for running locally
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
