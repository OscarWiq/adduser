import subprocess

def generate_candidates(names):
    tokens = []
    id_num = 1
    for (first_name, last_name) in names:
        first_token = first_name[0].lower() + first_name[-1].lower()
        last_token = last_name[0].lower() + last_name[-1].lower() + str(id_num)
        candidate_id = first_token + last_token
        candidate_pw = first_token + '-' + last_token + '!'
        tokens.append((candidate_id, candidate_pw, first_name, last_name))
        id_num += 1
    return tokens

def run_cmd(cmd_line):
    cmd_res = subprocess.Popen(cmd_line, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communitecate()
    msg = cmd_res[0].decode("cp1252", "ignore")
    error = cmd_res[1].decode("cp1252", "ignore")
    if msg:
        print("OK: " + msg)
    if error:
        print("ERROR: " + error + "\n")
