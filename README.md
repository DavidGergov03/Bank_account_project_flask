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

---

## Prerequisites
- Python 3.10+
- Docker installed on your system

---

## Running the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/bank-account-app.git
   cd bank-account-app
