# Banking Project
Using concept of classes and inheritance, this is a Python program to implement a banking application that supports three types of accounts: i) Savings, ii) Current and iii) Fixed deposit accounts. Store all data in files. Following tasks should be supported while following rules for each type of account. [25M]

## RULES:

(i) Ensure following minimum balances: 
Savings Account: Rs.1,000 /- 
Current account: Rs. 0 /- 
Fixed account: Rs. 10,000 /-

(ii). Calculate interest at the end of every month using following interest rates and add to the account: 
Savings Account: 4% p.a. 
Current account: 0% p.a. 
Fixed account: 12% p.a.

(iii). Fixed deposit account:
Once it is created, no further deposits can be made into it.
No withdrawal is permitted; only way to withdraw money is to close the account.

## TASKS:

(i). Create account 
INPUT: Type of account to create, Account holder's name, initial balance 
OUTPUT: New account number

(ii). Balance enquiry 
INPUT: Account number 
OUTPUT: Balance

(iii). Deposit amount: 
INPUT: Account number, Deposit amount 
OUTPUT: Final balance

(iv). Withdraw amount: 
INPUT: Account number, Withdrawal amount 
OUTPUT: Final balance

(v). Search by name: 
INPUT: Name (Full or partial) 
OUTPUT: Full name and Account number 
(Note: more than one account might contain specified partial name) 

(vi). Close account: 
INPUT: Account number 
OUTPUT: Closing balance
(this amount will be refunded to customer)
(Note: No subsequent tasks should be permitted on that account)
