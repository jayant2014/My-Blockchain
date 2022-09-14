# Initializing our (empty) blockchain list
blockchain = []
open_transactions = []
owner = 'Jay'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    """ Mining the block.
    
    """
    pass


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    
    txn_recipient = input('Enter the recipient of the transaction: ')
    txn_amount = float(input('Your transaction amount please: '))
    return txn_recipient, txn_amount


def get_user_choice():
    """Prompts the user for its choice and return it."""
    
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """

    for block in blockchain:
        print('Printing Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            # Skip the iteration for first block
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False

    return is_valid


waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        txn_data = get_transaction_value()
        recipient, amount = txn_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        # Exit loop
        waiting_for_input = False
    else:
        print('Input is invalid, please pick a value from the list!')
        
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User left!')


print('Done!')
