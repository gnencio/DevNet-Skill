# DevNet Associate Skill Assessment
Lists of accomplished tasks:

## Task 1 -- GitHub
- Preparation
    - Created a GitHub account with readme
    - Created a public repository, named "Devasc_Skill", on Github
- Implementation
    - `git clone <>`
    - Modification of README.md
    - `git add <>`
    - `git commit -m <>`
    - `git push origin main`
- Troubleshooting
    - `git config --list`
    - `git remote --verbose`
    - `git log`
    - `git status`
- Verification
    - Same as in troubleshooting 

## Task 2 -- Ansible
- Preparation
    - Installed CSR1000v VM
    - Added ansible.cfg and hosts from 7.4.7 Lab
- Implementation
    - Create file ios-status.yml to use as Ansible playbook
    - Copy and modify text from "task source file"
    - Copy and adapt starting text of playbook from 7.4.7 Lab
    - Install cisco.ios collection: `ansible-galaxy collection install cisco.ios`
    - Run the playbook: `ansible-playbook ios-status.yml`
- Troubleshooting
    - ping CSR1kv
    - Error output(s) after trying to run playbook
- Verification
    - Output after running playbook

## Task 3 -- Docker
- Preparation
    - Understand the Ansible playbook
    - Understand the Linux commands equivalent to the playbook
- Implementation
    - Create bash script that build and run Docker image: build.sh
- Troubleshooting
    - Error output(s) during the building of the Docker image
- Verification 
    - `docker ps -a` (included in the biuld script)

## Task 4 -- Jenkins
- Preparation
    - Download Jenkins Docker image: `docker pull jenkins/jenkins:lts`
    - Run Jenkins Docker container: `docker run <>`
    - Initial set up of Jenkins
- Implementation
    - Create a "Freestyle project" named "Task4BuildJob"
        - Add GitHub repo and credential
        - Add build `bash ./Task3/build.sh`
    - Create a "Freestyle project" named "Task4TestJob"
        - Set to build after "Task4BuildJob" is build
        - Add build:
            ```
            if docker ps -a | grep "myinstance"; then
	            exit 0
            else
	            exit 1
            fi
            ```
    - Create a "Pipeline" named "Task4Pipeline"
        ```
        node {
            stage('Preparation') {
                catchError(buildResult: 'SUCCESS') {
                    sh 'docker stop myinstance'
                    sh 'docker rm myinstance'
                } 
            }
            stage('Build') {
                build 'Task4BuildJob'
            }
            stage('Results') {
                build 'Task4TestJob'
            }
        }
        ```   
    - Build the "Task4Pipeline"
- Troubleshooting
    - After/while building, a job see "Console Output"
- Verification
    - Stage view of the "Task4Pipeline"

## Task 5 -- RESTCONF
- Preparation
    - Set logging monitor on CSR1kv:
        ```
        # conf t
        # logging monitor
        # end
        ```
    - Test curl instructions
- Implementation
    - Create file "restconf.py"
    - Adapt Python code from "RESTCONF Tutorial" webpage
- Troubleshooting
    - response.content has weird content, printed the header instead
    - Adapt to python3
    - Check response codes
- Verification
    - Check response codes


## Task 6 -- Webex Teams API
- Preparation
    - Get the Webex API key
- Implementation
    - Create file named task6.py
    - Adapt the code from Lab 8.6.7
- Troubleshooting
    - Use the documentation of developer.webex.com to discover how to upload files
- Verification
    - Check on the Webex app


## Task 7 -- BASH
- Preparation
    - Copy the configuration files to ios_config subfolder
- Implementation
    - Create check_ios.sh and edit it by adapting "bash_scripting_exam_questions.txt" file
    - Make it executable: `chmod +x check_ios.sh`
    - Run it: `./check_ios.sh > check_ios.rep`
- Troubleshooting
    - Take care of error notification
    - Note that in the string comparison maybe the line delimiter is included
- Verification
    - Verify correctness check_ios.rep file