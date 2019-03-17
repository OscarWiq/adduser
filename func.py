import subprocess

def generate_candidates(names):
    def recursion(names, acc, id_num, iterations):
        if len(names) <= 0:
            return acc
        (first_name, last_name) = names[0]
        first_token = first_name[0].lower() + first_name[-1].lower()
        last_token = last_name[0].lower() + last_name[-1].lower() + str(id_num)
        candidate_id = first_token + last_token
        candidate_pw = first_token + '-' + last_token + '!'
        if len(acc) <= 0 or not candidate_id in [x for (x,y,z,v) in acc]:
            acc.append((candidate_id, candidate_pw, first_name, last_name))
            return recursion(names[1:], acc, id_num - iterations, 0)
        else:
            return recursion(names, acc, id_num + 1, iterations + 1)
    return recursion(names, [], 1, 0)


def run_cmd(cmd_line):
    cmd_res = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    msg = cmd_res[0].decode("cp1252", "ignore")
    error = cmd_res[1].decode("cp1252", "ignore")
    if msg:
        print('OK: ' + msg)
    if error:
        print('ERROR: ' + error + '\n')
