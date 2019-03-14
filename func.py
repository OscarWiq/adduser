
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

