# DevNet Associate Skill Assessment
Lists of accomplished tasks:

Task 1 -- GitHub
- Preparation
    - Created a GitHub account with readme
    - Created a public repository, named "Devasc_Skill", on Github
- Implementation
    - Created folder named "Devasc_Skill" on the DEVASC VM
    - git init
    - git config <>
    - git remote add origin <>
    - git pull origin main
    - Modification of README.md
    - git add <>
    - git commit -m <>
    - git push origin main
- Troubleshooting
    - git config --list
    - git remote --verbose
    - git log
    - git status
- Verification
    - Same as in troubleshooting 

Task 2 -- Ansible
- Preparation
    - Installed CSR1000v VM
    - Added ansible.cfg and hosts from 7.4.7 Lab
- Implementation
    - Create file ios-status.yml to use as Ansible playbook
    - Copy and modify text from "task source file"
    - Copy and adapt starting text of playbook from 7.4.7 Lab
    - Install cisco.ios collection: ansible-galaxy collection install cisco.ios
    - Run the playbook: ansible-playbook ios-status.yml
- Troubleshooting
    - ping CSR1kv
    - Error output after trying to run playbook
- Verification
    - Output after running playbook