import subprocess

def generate_candidates(names):
    def recursion(names, acc, id_num, iterations):
        if len(names) <= 0:
            return acc
        (fname, lname) = names[0]
        first_token = fname[0].lower() + fname[-1].lower()
        last_token = lname[0].lower() + lname[-1].lower() + str(id_num)
        candidate_id = first_token + last_token
        candidate_pw = first_token + '-' + last_token + '!'
        if len(acc) <= 0 or not candidate_id in [x for (x,y,z,v) in acc]:
            acc.append((candidate_id, candidate_pw, fname, lname))
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
