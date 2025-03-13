# Exercise-1: Using GitHub for Source Control and Build

## Objective
Use GitHub for source control management and build automation. Create a repository, set up branches, add a requirements file, and create a GitHub Action workflow to automate the build process.

## Technologies Used
- GitHub
- GitHub Actions
- Python

## Steps

### Step 1: Create a GitHub Repository

1. **Create a Repository**
   - Go to your GitHub account.
   - Click on the "+" icon at the top right corner and select "New repository".
   - Name the repository `harsha-config-dev`.
   - Add a description if you like and choose whether the repository is public or private.
   - Click on "Create repository".

2. **Clone the Repository to Your Local Machine**
   ```sh
   git clone https://github.com/your-username/harsha-config-dev.git
   cd harsha-config-dev
   ```

3. **Create Branches**
   - Create and checkout the `feature/dev-build` branch:
     ```sh
     git checkout -b feature/dev-build
     ```
   - Create and checkout the `debug/dev-test` branch:
     ```sh
     git checkout main
     git checkout -b debug/dev-test
     ```

### Step 2: Create Requirements File

1. **Create `requirements.txt` File**
   - In your repository, create a file named `requirements.txt` and add the following content:
     ```plaintext
     paramiko
     pymssql
     urllib3
     certifi # NOT certify its certifi
     ansible
     requests
     ```

2. **Commit and Push Changes to `feature/dev-build` Branch**
   ```sh
   git add requirements.txt
   git commit -m "Add requirements.txt file"
   git push origin feature/dev-build
   ```

### Step 3: Create GitHub Action Workflow

1. **Create GitHub Action Workflow File**
   - In your repository, create a directory named `.github/workflows`.
   - Inside this directory, create a file named `python-package.yml`

## Explanation of Workflow Steps

1. **Workflow Trigger**:

    ```yaml
    on: [push]
    ```
    on: This key specifies the event that triggers the workflow. The value [push] indicates that the workflow will be triggered whenever there is a push event to the repository. This means that any time you push changes to any branch in the repository, this workflow will be executed.

    ex.:
        
        1. on: [pull_request]: Triggers on pull request events - such as opened, synchronized, and reopened.
        ex:  pull_request:
              types: [opened, synchronized, reopened]

        2. on: [schedule]: Triggers on a schedule using a cron expression - runs at 2:00 AM UTC every day.
        ex: schedule:
              - cron: '0 2 * * *'

        3. on: [workflow_dispatch]: Triggers manually using the workflow dispatch event.

2. **Jobs**:

    ```yaml
    jobs:
      build:
    ```
    1. jobs: This key defines a collection of jobs that will be run as part of the workflow. Each job is an independent unit of work that executes on a fresh virtual machine.
    2. build: This is the identifier (name) of the job. You can name jobs anything you like. In this case, it's named build.

3. **Job Configuration**:
    ```yaml
    runs-on: ubuntu-latest
    ```
    runs-on: This specifies the type of virtual machine (runner) that the job will run on. In this case, it is set to ubuntu-latest, which means the job will run on the latest version of an Ubuntu Linux virtual machine provided by GitHub Actions.

    ex.:ubuntu-latest: Latest Ubuntu Linux (default).
        windows-latest: Latest Windows Server.
        macos-latest: Latest macOS.
        ubuntu-20.04: Specific version of Ubuntu.

    These virtual machines are pre-configured with a variety of tools and utilities commonly used in software development, including various versions of programming languages, compilers, build tools, and more.


4. **Checkout repository**:
   ```yaml
   - name: Checkout repository
     uses: actions/checkout@v2
   ```
   This step uses the `actions/checkout` action to check out the source code of the repository.

5. **List content of repo**:
   ```yaml
   - name: List content of repo
     run: ls -al
   ```
   This step lists the contents of the repository directory for verification purposes.

6. **Set up Python 3.11**:
   ```yaml
   - name: Set up Python 3.11
     uses: actions/setup-python@v2
     with:
       python-version: 3.11
   ```
   This step sets up Python 3.11 on the virtual machine.

7. **Create virtual environment**:
   ```yaml
   - name: Create virtual environment
     run: python -m venv venv
   ```
   The command python -m venv venv is used to create a virtual environment in Python.

   1. python: This is the Python interpreter. Depending on our system i.e.python3, if python defaults to Python 2.x.
   2. -m venv: The -m flag allows us to run a library module as a script. In this case, venv is a module that comes with Python's standard library and is used to create virtual environments.
   3. venv: This is the name of the directory where the virtual environment will be created. We can set name for this directory anything, but venv is a common convention.

8. **Activate virtual environment**:
   ```yaml
   - name: Activate virtual environment
     run: source venv/bin/activate
   ```
   This step activates the previously created virtual environment.
   
   The command source venv/bin/activate is used to activate a Python virtual environment on Unix-like systems (e.g., Linux, macOS). The bin directory is where the activation script is located by default when a virtual environment is created using python -m venv venv.
   ex: source myenv/bin/activate (Unix-like systems)
      .\myenv\Scripts\activate (Windows)
        

9. **Install dependencies**:
   ```yaml
   - name: Install dependencies
     run: |
       set -e
       pip install --upgrade pip
       pip install -r requirements.txt
     continue-on-error: false
   ```
   This step installs the dependencies listed in the `requirements.txt` file.
   
   The `set -e` command ensures that the script exits immediately if a command exits with a non-zero status(failure).

   The continue-on-error option determines whether the workflow should continue executing subsequent steps if the current step fails.
   
   1. continue-on-error: false: This is the default behavior. If the step fails (i.e., returns a non-zero exit code), the workflow will stop executing further steps and mark the job as failed.
   2. continue-on-error: true: If this option is set to true, the workflow will continue executing subsequent steps even if the current step fails. The job will not be marked as failed due to this step.

10. **List installed packages**:
   ```yaml
   - name: List installed packages
     run: pip list
   ```
   This step lists all the installed Python packages in the virtual environment.


11. **Save, Commit and Push Changes to `feature/dev-build` Branch**
  Save the changes and
   ```sh
   git add .github/workflows/python-package.yml
   git commit -m "Add GitHub Action workflow"
   git push origin feature/dev-build
   ```

### Summary

1. Created a repository named `harsha-config-dev`.
2. Created three branches: `main`, `feature/dev-build`, and `debug/dev-test`.
3. Added `requirements.txt` file to the `feature/dev-build` branch.
4. Created a GitHub Action workflow to automate the build process on push events.

### Conclusion

By following these steps, you can set up a repository with proper source control management and build automation using GitHub Actions. This exercise demonstrates the ability to manage branches, handle dependencies, and automate workflows.