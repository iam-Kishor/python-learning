while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted.')
print('Welcome, Joe! Here is the secret message: The treasure is buried under the old oak tree.')

