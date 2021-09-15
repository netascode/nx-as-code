Implement NetDevOps practices on Nexus Infrastructure:  NX-OS Management using RESTCONF
=====================================================================================
Automate the management of your Nexus-based Data Center Infrastructure leveraging Open Source Tools. This repository contains an [Ansible](https://www.ansible.com/) role named the `nexus_manage_restconf` which validates, configures and tests the configurations deployed on you Nexus switches.

![alt text](images/netdevops.png?raw=true)

The code uses [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/) Templates to dynamically render JSON files compliant with the NX-OS [OpenConfig](https://www.openconfig.net/) [YANG](https://github.com/YangModels/yang/tree/master/vendor/cisco/nx) Model. The JSON payloads are afterwards sent via HTTPS to the Nexus [RESTCONF](https://datatracker.ietf.org/doc/html/rfc8040) API. The code also uses Jinja2 Templates to dynamically render [Robot Framework](https://robotframework.org/) test suites which verify the operational status of the different protocols configured on the Nexus switches.

The current state of the project only allows you configure the protocols required to spin up a VXLAN-EVPN Fabric, however its modular architecture allows you to easily extend support to other protocols.

The Ansible Playbooks can be executed directly on a shell or can be executed by any CI/CD tool. This repository also contains a simple example of a [Jenkins](https://www.jenkins.io/) CI/CD Pipeline. 

This projects aims to implement GitOps practices on Nexus Switches by declaring the switch configuration as Code.

## Related Sandbox
[Open NX-OS w/ Nexus 9K](https://devnetsandbox.cisco.com/RM/Diagram/Index/0e22761d-f813-415d-a557-24fa0e17ab50?diagramType=Topology)

## Links to DevNet Learning Labs
* [NX-OS Programmability](https://developer.cisco.com/learning/tracks/nxos-programmability)
* [Network Programmability for Network Engineers](https://developer.cisco.com/learning/tracks/netprog-eng)
