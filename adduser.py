import func

with open('names.txt', 'r') as f:
    name = f.read().splitlines()  #splitlines removes /n from each array element
    first_name = [x.split()[0] for x in name]
    last_name = [y.split()[1] for y in name]

for first_name, last_name in zip(first_name, last_name):
    func.generate_id(first_name, last_name)
    func.generate_pw(first_name, last_name)

print(func.existing_ids)
print(func.passwords)

