import subprocess

existing_ids = []
existing_pws = []

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
        candidate_pw = first_name[0].lower() + first_name[-1].lower() \
                       + '-' + last_name[0].lower() + last_name[-1].lower() + str(id_num) + '!'
        if not candidate_pw in existing_pws:
            existing_pws.append(candidate_pw)
            return candidate_pw
        id_num += 1


def run_cmd(command):
    cmd_res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    msg = cmd_res[0].decode()
    error = cmd_res[1].decode()
    if msg:
        print("OK" + cmd_res[0].decode("ascii"))
    if error:
        print("ERROR" + cmd_res[1].decode("ascii") + "\n")
