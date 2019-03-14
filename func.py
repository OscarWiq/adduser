import subprocess

existing_ids = []
passwords = []

def generate_id(first_name, last_name):
    id_num = 1
    while True:
        candidate_id = first_name[0].lower() + first_name[-1].lower() \
                       + last_name[0].lower() + last_name[-1].lower() + str(id_num)
        if not candidate_id in existing_ids:
            existing_ids.append(candidate_id)
            return candidate_id
        id_num += 1

def generate_pw(first_name, last_name):
    id_num = 1
    while True:
        candidate_pw = first_name[0].lower() + first_name[-1].lower() + ('-') + last_name[0].lower() + last_name[-1].lower() + str(id_num) + ('!')
        if not candidate_pw in passwords:
            passwords.append(candidate_pw)
            return candidate_pw
        id_num += 1

def run_cmd(cmd_line):
    cmd_res = subprocess.Popen(cmd_line, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communitecate()
    msg = cmd_res[0].decode("cp1252", "ignore")
    error = cmd_res[1].decode("cp1252", "ignore")
    if msg:
        print("OK: " + msg)
    if error:
        print("ERROR: " + error + "\n")
