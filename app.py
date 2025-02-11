from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

app = Flask(__name__)

# Secret key for session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.secret_key = 'your_secret_key_here'

Session(app)

class BankAccount:
    def __init__(self, account_number, balance=0, interest=0, password=''):
        self.account_number = account_number
        self.balance = balance
        self.interest = interest
        self.password = password

    def currents_account(self, account_number, balance, password):
        return {'type': 'Current', 'account_number': account_number, 'balance': balance, 'password': password}

    def savings_account(self, account_number, balance, interest, password):
        return {'type': 'Saving', 'account_number': account_number, 'balance': balance, 'interest_rate': interest, 'password': password}


# Route for the Main Menu
@app.route('/')
def index():
    return render_template('index.html')


# Route for Current Account Creation
@app.route('/current_account', methods=['GET', 'POST'])
def current_account():
    if 'accounts' not in session:
        session['accounts'] = []

    if request.method == 'POST':
        acc_num = request.form['account_number']
        balance = float(request.form['balance'])
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Hashing the password for storage

        # Create new current account
        bank_acc_instance = BankAccount(acc_num, balance, password=hashed_password)
        new_account = bank_acc_instance.currents_account(acc_num, balance, hashed_password)
        session['accounts'].append(new_account)  # Append to the accounts list
        session.modified = True  # Mark session as modified to ensure it's saved
        return redirect(url_for('index'))

    return render_template('current_account.html')


# Route for Savings Account Creation
@app.route('/savings_account', methods=['GET', 'POST'])
def savings_account():
    if 'accounts' not in session:
        session['accounts'] = []

    if request.method == 'POST':
        acc_num_savings = request.form['account_number']
        balance_savings = float(request.form['balance'])
        interest_rate = float(request.form['interest_rate'])
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Hashing the password for storage

        # Create new savings account
        bank_acc_instance = BankAccount(acc_num_savings, balance_savings, interest_rate, password=hashed_password)
        new_account = bank_acc_instance.savings_account(acc_num_savings, balance_savings, interest_rate, hashed_password)
        session['accounts'].append(new_account)  # Append to the accounts list
        session.modified = True  # Mark session as modified to ensure it's saved
        return redirect(url_for('index'))

    return render_template('savings_account.html')


# Route for Viewing Accounts (Requires Account Number and Password)
@app.route('/view_accounts', methods=['GET', 'POST'])
def view_accounts():
    if request.method == 'POST':
        acc_num = request.form['account_number']
        password = request.form['password']

        # Search for the account
        for account in session.get('accounts', []):
            if account['account_number'] == acc_num:
                # Check if the password matches the stored hashed password
                if check_password_hash(account['password'], password):
                    # If password is correct, return account details
                    return render_template('account_details.html', account=account)

        # If no matching account or incorrect password
        return render_template('view_accounts.html', error="Incorrect account number or password")

    return render_template('view_accounts.html')


# Route for Exiting and Clearing the Session
@app.route('/exit', methods=['POST'])
def exit_app():
    return render_template('goodbye.html')


# Goodbye Page
@app.route('/goodbye')
def goodbye():
    return "<h1>Thank you for using our services. Goodbye!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

