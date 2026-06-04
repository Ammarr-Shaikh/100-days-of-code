import random

print("Welcome to the password generator! ")
alpha = int(input("Enter how many letters you want in yo pass: "))
beta = int(input("Enter how many numbers you want in yo pass: "))
theta = int(input("Enter how many special symbols you want in yo pass: "))



# List of lowercase alphabets
alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

# List of numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

# List of special symbols (common set)
special_symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
    "'", '"', ',', '.', '<', '>', '/', '?', '|', '\\'
]
# easy
'''password = ""
for char in range(0,alpha):
    rand_aplha = random.choice(alphabets)
    password += rand_aplha

for num in range(0,beta):
    rand_beta = random.choice(numbers)
    password += rand_beta

for char in range(0,theta):
    rand_theta = random.choice(special_symbols)
    password += rand_theta

print(password)
'''
pass_list = []
for char in range(0,alpha):
    rand_aplha = random.choice(alphabets)
    pass_list += rand_aplha

for num in range(0,beta):
    rand_beta = random.choice(numbers)
    pass_list += rand_beta

for char in range(0,theta):
    rand_theta = random.choice(special_symbols)
    pass_list += rand_theta

random.shuffle(pass_list)
password = ""
for i in pass_list:
    password += i
print("password: ", password)
