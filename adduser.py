import func

file_name = input("Fil med namn: ").lower()
ou = input("OU som användarkontona ska skapas i (RDN): ")
unc = input("UNC-sökväg till mappen med hemkataloger: ")
group = input("Namn på gruppen som kontona ska tillhöra: ")

with open(file_name, 'r') as f:
    name = f.read().splitlines()  # splitlines removes /n from each array element
    first_name = [x.split()[0] for x in name]
    last_name = [y.split()[1] for y in name]

for first_names, last_names in zip(first_name, last_name):
    func.generate_id(first_names, last_names)
    func.generate_pw(first_names, last_names)

user_ids = func.existing_ids
passwords = func.existing_pws

for i in range(0, len(user_ids)):
    cmd_command = "dsadd user cn=" + first_name[i] + "," + last_name[i] + "," + ou + ",dc=g105,dc=local -memberof "
    cmd_command += "cn=" + group + "," + ou + ",dc=g105,dc=local "
    cmd_command += "-upn " + user_ids[i] + " -samid " + user_ids[i] + " -hmdir " + unc
    cmd_command += " -hmdrv H -pwd " + passwords[i] + " -pwdneverexpires no"
    func.run_cmd(cmd_command)

input("Press ENTER to exit")
    
