# Kubernetes


# yml
write your yml code here and save it as sam-yaml-file.yaml

## to install yml for python
pip install pyyml 

## run the python file
python test-sam-yaml-file.py

# make & run docker compose

# to ssh from one ubuntu server to another
# copy the content of .pem key (which was used during the lauch of ec2) in a file and save it. Use nano editor.
sudo ssh -i <location & name of the file where .pem key content is saved> ubuntu@<IP of destination server>


## ANSIBLE
# create a hosts file which is an inventory file to hold the details of the servers
# generally this file is in the location /etc/ansible/hosts. If not then create a hosts file anywhere in ubuntu server
nano hosts

[servers]
server1 ansible_host=<IP address>
server2 ansible_host=<IP address>
server3 ansible_host=<IP address>

[all:vars]
ansible_python_interpreter=user/bin/python3

ansible-inventory --list -y -i <path of the hosts file>

