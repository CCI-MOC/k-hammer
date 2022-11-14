#!/python3
# hammerdb pexpect script
import os
import time
import json
import pexpect


def run_pexpect_json(pexpect_json):
    """Processes an dictionary with pexpect"""
    setup = pexpect.spawn(pexpect_json["cmd"])
    print(f"running comand {pexpect_json['cmd']}")
    for prompt_resp in pexpect_json["do_list"]:
        print(f"{prompt_resp['prompt']}\n")
        time_out = 30
        if "timeout" in prompt_resp:
            time_out = prompt_resp["timeout"]
        setup.expect(prompt_resp["prompt"], timeout=time_out)
        nap_time = 0.2
        if "sleep" in prompt_resp:
            nap_time = prompt_resp["sleep"]
        time.sleep(nap_time)
        setup.sendline(prompt_resp["resp"])

def run_tpc_c:
    pexpect_json={
       "cmd": "/home/hammerdb//hammerdbcli" 
    }

# --> ./hammerdbcli
# --> help
# HammerDB v4.5 CLI Help Index
#
# Type "help command" for more details on specific commands below
#
# 	buildschema
# 	clearscript
# 	customscript
# 	datagenrun
# 	dbset
# 	dgset
# 	diset
# 	distributescript
# 	librarycheck
# 	loadscript
# 	print
# 	quit
# 	runtimer
# 	steprun
# 	switchmode
# 	tcset
# 	tcstart
# 	tcstatus
# 	tcstop
# 	vucomplete
# 	vucreate
# 	vudestroy
# 	vurun
# 	vuset
# 	vustatus
# 	waittocomplete


# --> librarycheck
# Checking database library for Oracle
# Error: failed to load Oratcl - can't read "env(ORACLE_HOME)": no such variable
# Ensure that Oracle client libraries are installed and the location in the LD_LIBRARY_PATH environment variable
# Checking database library for MSSQLServer
# Error: failed to load tdbc::odbc - couldn't load file "libiodbc.so": libiodbc.so: cannot open shared object file: No such file or directory
# Ensure that MSSQLServer client libraries are installed and the location in the LD_LIBRARY_PATH environment variable
# Checking database library for Db2
# Error: failed to load db2tcl - couldn't load file "/home/hammerdb/HammerDB-4.5/lib/db2tcl2.0.1/libdb2tcl.so": libdb2.so.1: cannot open shared object file: No such file or directory
# Ensure that Db2 client libraries are installed and the location in the LD_LIBRARY_PATH environment variable
# Checking database library for MySQL
# Success ... loaded library mysqltcl for MySQL
# Checking database library for PostgreSQL
# Success ... loaded library Pgtcl for PostgreSQL
# Checking database library for MariaDB
# Success ... loaded library mariatcl for MariaDB

# --> dbset db maria
# Database set to MariaDB

# --> dbset bm TPC-C (or TPROC-C)
# Benchmark set to TPC-C for MariaDB

# ---> print dict

# ---> diset connection maria_host mariadb
# ---> diset tpcc maria_pass pass
# ---> diset tpcc maria_total_iterations 1
# ---> buildschema

# ---> loadscript
# ---> vuset vu 4  #virtual userss
# ---> vuset logtotemp 1
# ---> print vuconf
# ---> vucreate
# ---> vustatus
# ---> vurun
# ---> test result
