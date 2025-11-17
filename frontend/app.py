from flask import Flask, request
from backend.customer_data import read_customers
from backend.savings_account import SavingsAccount

app = Flask(__name__)

# Create a sample account
account = SavingsAccount(1001, "Alice", 5000)

@app.route("/", methods=["GET", "POST"])
def home():
    customers = read_customers()
    message = ""

    # Handle POST form (deposit/withdraw/interest)
    if request.method == "POST":
        action = request.form.get("action")
        amount = float(request.form.get("amount", 0))
        if action == "Deposit":
            message = account.deposit(amount)
        elif action == "Withdraw":
            message = account.withdraw(amount)
        elif action == "Interest":
            message = account.add_interest()

    # Build full HTML page as string (no templates)
    html = "<h1>🏦 Simple Banking System</h1>"
    html += "<h2>📋 Customer List</h2><ul>"
    for c in customers:
        html += f"<li>{c['CustomerID']}: {c['Name']} ({c['City']})</li>"
    html += "</ul><hr>"

    html += f"<h2>💳 {account.name}'s Account</h2>"
    html += f"<p>Current Balance: ₹{account.get_balance()}</p>"

    html += """
        <form method="POST">
            <label>Amount (₹):</label>
            <input type="number" name="amount" step="0.01" required>
            <button type="submit" name="action" value="Deposit">Deposit</button>
            <button type="submit" name="action" value="Withdraw">Withdraw</button>
            <button type="submit" name="action" value="Interest">Add Interest</button>
        </form>
    """

    if message:
        html += f"<p style='color:green;'><b>{message}</b></p>"

    html += "<hr><p>© 2025 Simple Banking System</p>"
    return html

@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
