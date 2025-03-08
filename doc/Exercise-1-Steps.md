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
   - Inside this directory, create a file named `python-build.yml` and add the following content:
     ````yaml name=.github/workflows/python-build.yml
     name: Python Build

     on: [push]

     jobs:
       build:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout repository
           uses: actions/checkout@v2

         - name: List repository content
           run: ls -la

         - name: Set up Python 3.11
           uses: actions/setup-python@v2
           with:
             python-version: '3.11'

         - name: Create virtual environment
           run: python -m venv venv

         - name: Activate virtual environment
           run: source venv/bin/activate

         - name: Install dependencies
           run: |
             pip install --upgrade pip || { echo 'Failed to upgrade pip'; exit 1; }
             pip install -r requirements.txt || { echo 'Failed to install dependencies from requirements.txt'; exit 1; }

         - name: List installed packages
           run: pip list

         - name: Error handling
           run: |
             set -e
             echo "All steps completed successfully."
     ````

2. **Commit and Push Changes to `feature/dev-build` Branch**
   ```sh
   git add .github/workflows/python-build.yml
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