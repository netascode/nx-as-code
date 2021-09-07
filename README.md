Implement NetDevOps practices on Nexus Infrastructure:  NX-OS Management using RESTCONF
=====================================================================================
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/netascode/nexus-as-code)

A modular Ansible role to validate, configure and test VXLAN-EVPN Fabrics on NX-OS switches from a Jenkins Pipeline

## Use Case Description

Automate the management of your Nexus-based Data Center Infrastructure leveraging Open Source Tools. This repository contains an [Ansible](https://www.ansible.com/) role named the `nexus_manage_restconf` which validates, configures and tests the configurations deployed on you Nexus switches.

The code uses [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) Templates to dynamically render JSON files compliant with the NX-OS [OpenConfig](https://www.openconfig.net/) [YANG](https://github.com/YangModels/yang/tree/master/vendor/cisco/nx) Model. The JSON payloads are afterwards sent via HTTPS to the Nexus [RESTCONF](https://datatracker.ietf.org/doc/html/rfc8040) API. The code also uses Jinja2 Templates to dynamically render [Robot Framework](https://robotframework.org/) test suites which verify the operational status of the different protocols configured on the Nexus switches.

The current state of the project only allows you configure the protocols required to spin up a VXLAN-EVPN Fabric, however its modular architecture allows you to easily extend support to other protocols.

The Ansible Playbooks can be executed directly on a shell or can be executed by any CI/CD tool. This repository also contains a simple example of a [Jenkins](https://www.jenkins.io/) CI/CD Pipeline. 

This projects aims to implement GitOps practices on Nexus Switches by declaring the switch configuration as Code.

## Prerequisites 

Make sure to have Python 3.7+ and Ansible 2.9+ installed on your computer or Jenkins server.

## Installation

The Ansible playbooks in this repository can be executed on your machine or on a Jenkins Server. In any case make sure to install the libraries listed in the `requirements.txt` file

 1. Clone the Github repository

        git clone https://github.com/jgomezve/nexus-as-code

 2. Install the required python libaries

        cd nexus-as-code       
        pip install -r requirements.txt

## Usage 

* Modifiy the Ansible inventory `inventory/hosts.yaml` with the Nexus switches you would like to manage and its corresponding management IP addresses. Here an example:

```yaml
---
network:
  children:
    nexus:
      hosts:
        LEAF1:
          nexus_host: 192.168.0.1
          ansible_connection: local
        LEAF2:
          nexus_host: 192.168.0.2
          ansible_connection: local
        SPINE1:
          nexus_host: 192.168.0.3
          ansible_connection: local
```

* Modify the the Host variables `inventory/host_vars/` based on the configuration you would like to deploy. The schema file (`roles/nexus_manage_restconf/files/nexus_schema`) helps you to verify the supported variables/attributes. Here an example of the BGP configuration on a Spine switch

```yaml
nexus:
  bgp:
    asn: 65001
    router_id: 192.168.1.1
    address_families:
      - type: ipv4
        subtype: unicast
      - type: l2vpn
        subtype: evpn
        retain_rt: all
    neighbors:
      - ip_address: 192.168.1.3
        remote_asn: 65001
        update_source: lo0
        address_families:
          - type: ipv4
            subtype: unicast
            send_community: enabled
            route_reflector: enabled
          - type: l2vpn
            subtype: evpn
            send_community: enabled
            route_reflector: enabled
```
**Note**: As of today the code supports only the configuration required to set up a VXLAN-EVPN Fabric (OSPF, PIM, BGP, VXLAN). 

### Local execution - Single Ansible Playbooks

This repository contains four different Ansible playbooks, each of them in charge of executing a task withing the network management lifecycle (Validate, Prepare, Deploy & Test)


* `nexus_validate.yaml` uses [yamale](https://github.com/23andMe/Yamale) to verify the variables defined on your host_vars against a pre-defined schema (`roles/nexus_manage_restconf/files/nexus_schema.yaml`).

        ansible-playbook -i inventory/ nexus_validate.yaml 

* `nexus_prepare.yaml` uses Ansible built-in modules to enable the RESTCONF API on the managed Nexus devices

        ansible-playbook -i inventory/ nexus_prepare.yaml -e "username=<<username>> password=<<password>>"

* `nexus_deploy.yaml` uses Jinja2 Templates to render JSON files which are latter sent to the Nexus RESTCONF API

        ansible-playbook -i inventory/ nexus_deploy.yaml -e "username=<<username>> password=<<password>>"

* `nexus_test.yaml` uses Jinja2 Templates to render RobotFramework Test suites which verify the operational status of the protocols configured on the Nexus switches

        ansible-playbook -i inventory/ nexus_deploy.yaml -e "username=<<username>> password=<<password>>"

### Jenkins CI/CD Pipeline

This respository also contains a sample of a __Jenkinsfile__ which in a declarative way describes the Pipeline stages. Folow these steps in order to link you GitHub repository with a Jenkins server:   

* Configure a Webhook on your Github repository. More information here https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks

![alt text](images/webhook.png?raw=true)

* The __Jenkins__ file uses the credentials named `nexus_credentials` to configure the Nexus switches. Set up global credentials with that name on the Jenkins server. More information here https://www.jenkins.io/doc/book/using/using-credentials/

![alt text](images/credentials.png?raw=true)

* Create a Pipeline through the Jenkins classic UI. More information here https://www.jenkins.io/doc/book/pipeline/getting-started/#defining-a-pipeline-in-scm

![alt text](images/pipeline_creation_jenkins.png?raw=true)

* Now everytime you push changes to your Git repository a Pipeline execution will be triggered on Jenkins which in turn will execute the Validation, Preparation, Deployment and Testing phases on your managed Nexus switches. Jenkins will display the outcome of each stage and  publish Robot Framework HTML reports and JUnit tests results.

![alt text](images/jenkins_status.png?raw=true)
