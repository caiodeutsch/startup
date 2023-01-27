<<<<<<< HEAD
### This repository is for EC2 clonning only
=======
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
python3.10 db_seed.py # TODO: include check schema
nohup python3.10 run.py &
```

### Instructions for running Flask Application locally
```shell script
  pip install -r requirements.txt
  python run.py
```

### Instructions for running tests
```shell script	
  python -m pytest
```
>>>>>>> 7b30f3f62120929eced66569c5387cc414e8c7cf
