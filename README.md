# Bank_account_project_flask
A Flask-based banking application with Docker support

# Bank Account App

A simple Flask-based banking application that allows users to:
- Create current and savings accounts with a password.
- View account details after authentication.
- Store session data for 30 minutes using Flask-Session.
- Run the app in a Docker container for easy deployment.

---

## Features
- **Current Account Creation**: Create accounts with a balance and password.
- **Savings Account Creation**: Includes interest rate setup.
- **Account Authentication**: Securely view account details using account number and password.
- **Session Persistence**: Data persists for 30 minutes using Flask-Session.
- **Docker Support**: Easily run the app using Docker.
- **CI/CD Support**: Has an integrated Jenkinsfile to create a CI/CD pipeline for the project.

---

## Prerequisites
- Python 3.10+
- Docker installed on your system

---

## Running the App Locally with Flask

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/bank_account_project_flask.git
   cd bank-account-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   flash run
   ```
5. Open your browser and navigate to:
   ```arduino
   http://localhost:5000
   ```
## Running the App with Docker

1. Build the Docker image:
   ```bash
   docker build -t bank_account_app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 bank_account_app
   ```
3. Open your browser and navigate to:
   ```arduino
   http://localhost:5000
   ```
