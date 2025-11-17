-- Create USERS table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Create ACCOUNTS table
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create TRANSACTIONS table
CREATE TABLE transactions (
    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    txn_type TEXT NOT NULL,  -- deposit / withdraw
    amount REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);


-----------------------------------------------------------
-- 2. INSERT SAMPLE USERS
------------------------------------------------------------

INSERT INTO users (name, email, password)
VALUES
('Shresta', 'shresta@gmail.com', '1234'),
('Naveen', 'naveen@gmail.com', 'abcd');


------------------------------------------------------------
-- 3. CREATE SAMPLE BANK ACCOUNTS
------------------------------------------------------------

INSERT INTO accounts (user_id, account_type, balance)
VALUES
(1, 'Savings', 0),
(2, 'Current', 500);


------------------------------------------------------------
-- 4. SAMPLE TRANSACTIONS (DEPOSIT / WITHDRAW)
------------------------------------------------------------

-- Deposit ₹1000 to Shresta (account_id = 1)
UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 1;

INSERT INTO transactions (account_id, txn_type, amount)
VALUES (1, 'deposit', 1000);

-- Withdraw ₹300 from Shresta (account_id = 1)
UPDATE accounts
SET balance = balance - 300
WHERE account_id = 1
AND balance >= 300;

INSERT INTO transactions (account_id, txn_type, amount)
VALUES (1, 'withdraw', 300);
