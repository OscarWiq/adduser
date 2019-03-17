import func

file_name = input("Fil med namn: ").lower()
ou = input("OU som användarkontona ska skapas i (RDN): ")
unc = input("UNC-sökväg till mappen med hemkataloger: ")
group = input("Namn på gruppen som kontona ska tillhöra: ")

with open(file_name, 'r') as f:
    names = list(map(lambda name: (name.split()[0], name.split()[1]), f.read().splitlines()))

for (user_id, password, first_name, last_name) in func.generate_candidates(names):
    cmd_command = "dsadd user cn=" + user_id + "," + ou + ",dc=g105,dc=local -memberof "
    cmd_command += "cn=" + group + "," + ou + ",dc=g105,dc=local "
    cmd_command += " -samid " + user_id + "-upn " + user_id
    cmd_command += " -fn " + first_name + " -ln " + last_name + " -hmdir " + unc
    cmd_command += " -hmdrv H -pwd " + password + " -pwdneverexpires no"
    func.run_cmd(cmd_command)

input("Press ENTER to exit")

    
