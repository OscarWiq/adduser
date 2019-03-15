#!/usr/bin/env python
# -*- coding: utf-8 -*-
import func

namefile = input("Fil med namn: ").lower()
ou = input("OU som användarkontona ska skapas i (RDN): ")
unc = input("UNC-sökväg till mappen med hemkataloger: ")
grupp = input("Namn på gruppen som kontona ska tillhöra: ")

with open(namefile, 'r') as f:
    name = f.read().splitlines()  # splitlines removes /n from each array element
    first_name = [x.split()[0] for x in name]
    last_name = [y.split()[1] for y in name]

first_name_generate = first_name.copy()
last_name_generate = last_name.copy()

for first_name_generate, last_name_generate in zip(first_name_generate, last_name_generate):
    func.generate_id(first_name_generate, last_name_generate)
    func.generate_pw(first_name_generate, last_name_generate)

userid = func.existing_ids
password = func.existing_pws

i = 0
for user in userid:
    cmd_command = "dsadd user cn=" + user + "," + ou + ",dc=g105,dc=local -memberof "
    cmd_command = cmd_command + "cn=" + grupp + "," + ou + ",dc=g105,dc=local "
    cmd_command = cmd_command + "-upn " + user + " -samid " + user + " -hmdir " + unc
    cmd_command = cmd_command + " -hmdrv H -pwd " + password[n] + " -pwdneverexpires no"
    func.run_cmd(cmd_command)
    i += 1
    
input("Press ENTER to exit")
    
