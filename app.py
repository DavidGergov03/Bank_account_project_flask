from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)

# Secret key for session management
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.secret_key = 'your_secret_key_here'

Session(app)


class BankAccount:
    def __init__(self, account_number, balance=0.0, interest=0.0, password=''):
        self.account_number = account_number
        self.balance = balance
        self.interest = interest
        self.password = password

    @staticmethod
    def currents_account(account_number, balance, password):
        return {'type': 'Current', 'account_number': account_number, 'balance': balance, 'password': password}

    @staticmethod
    def savings_account(account_number, balance, interest, password):
        return {'type': 'Saving', 'account_number': account_number, 'balance': balance,
                'interest_rate': interest, 'password': password}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        acc_num = request.form['account_number']
        password = request.form['password']

        for account in session.get('accounts', []):
            if account['account_number'] == acc_num and check_password_hash(account['password'], password):
                return render_template('account_details.html', account=account)

        return render_template('index.html', error="Incorrect account number or password")

    return render_template('index.html', active_page='index')


@app.route('/account_manager')
def account_manager():
    return redirect(url_for('current_account'))  # default to current account

@app.route('/account_manager/current_account', methods=['GET', 'POST'])
def current_account():
    if 'accounts' not in session:
        session['accounts'] = []

    if request.method == 'POST':
        acc_num = request.form['account_number']
        balance = float(request.form['balance'])
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        for account in session['accounts']:
            if account['account_number'] == acc_num:
                return render_template('current_account.html',
                                       active_page='current',
                                       error="⚠️ This account number already exists.")

        new_account = {
            'account_number': acc_num,
            'balance': balance,
            'password': hashed_password,
            'type': 'current'
        }
        session['accounts'].append(new_account)
        session.modified = True

        return render_template('current_account.html',
                               active_page='current',
                               acc_num=acc_num,
                               balance=balance)

    return render_template('current_account.html', active_page='current')


# Route for Savings Account Creation
@app.route('/account_manager/savings_account', methods=['GET', 'POST'])
def savings_account():
    if 'accounts' not in session:
        session['accounts'] = []

    if request.method == 'POST':
        acc_num_savings = request.form['account_number']
        balance_savings = float(request.form['balance'])
        interest_rate = float(request.form['interest_rate'])
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')  # Hashing the password for storage

        for account in session['accounts']:
            if account['account_number'] == acc_num_savings:
                return render_template('savings_account.html',
                                       error="⚠️ This account number already exists.")

        # Create new savings account
        new_account = BankAccount.savings_account(acc_num_savings, balance_savings, interest_rate, hashed_password)
        session['accounts'].append(new_account)  # Append to the accounts list
        session.modified = True  # Mark session as modified to ensure it's saved
        return render_template('savings_account.html', acc_num_savings=acc_num_savings,
                               balance_savings=balance_savings, interest_rate=interest_rate, account_created = True)

    return render_template('savings_account.html', active_page='savings')


# Route for Exiting and Clearing the Session
@app.route('/exit', methods=['POST'])
def exit_app():
    session.clear()
    return render_template('goodbye.html')


# ,Goodbye Page
@app.route('/goodbye')
def goodbye():
    return "<h1>Thank you for using our services. Goodbye!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
