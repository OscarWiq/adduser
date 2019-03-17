import func

file_name = input("Fil med namn: ").lower()
ou = input("OU som användarkontona ska skapas i (RDN): ")
unc = input("UNC-sökväg till mappen med hemkataloger: ")
group = input("Namn på gruppen som kontona ska tillhöra: ")

def splitter(str):
    str = str.split()
    return (str[0], str[1])

with open(file_name, 'r') as f:
    full_name = f.read().splitlines()  # splitlines removes \n from each array element
    # names = list(map(lambda name: (name.split()[0], name.split()[1]), full_name))
    names = list(map(splitter, full_name))

for (user_id, password, fname, lname) in func.generate_candidates(names):
    cmd_command = "dsadd user cn=" + user_id + "," + ou + ",dc=g105,dc=local -memberof "
    cmd_command += "cn=" + group + "," + ou + ",dc=g105,dc=local "
    cmd_command += " -samid " + user_id + "-upn " + user_id
    cmd_command += " -fn " + fname + " -ln " + lname + " -hmdir " + unc
    cmd_command += " -hmdrv H -pwd " + password + " -pwdneverexpires no"
    func.run_cmd(cmd_command)

input("Press ENTER to exit")

    
