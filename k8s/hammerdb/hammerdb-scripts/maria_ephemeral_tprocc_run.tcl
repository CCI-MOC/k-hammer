#!/bin/tclsh

# This is moved to the env of the container as this causes hammerdb auto to fail
# Set the path for logs directory. By Default logs are logged in /tmp
# export TMP="/tmp"

# parameters that can be changed with diset:
#
#  connection {
#   maria_host               = mariadb-ephemeral
#   maria_port               = 3306
#   maria_socket             = /tmp/mariadb.sock
#   maria_ssl                = false
#   maria_ssl_two_way        = false
#   maria_ssl_linux_capath   = /etc/mysql/certs
#   maria_ssl_windows_capath = C:\mysql\certs
#   maria_ssl_ca             = ca-cert.pem
#   maria_ssl_cert           = client-cert.pem
#   maria_ssl_key            = client-key.pem
#   maria_ssl_cipher         = server
#  }
#  tpcc  {
#   maria_count_ware       = 1
#   maria_num_vu           = 1
#   maria_user             = root
#   maria_pass             = pass
#   maria_dbase            = tpcc
#   maria_storage_engine   = innodb
#   maria_partition        = false
#   maria_prepared         = false
#   maria_total_iterations = 10000000
#   maria_raiseerror       = false
#   maria_keyandthink      = false
#   maria_driver           = test
#   maria_rampup           = 2
#   maria_duration         = 5
#   maria_allwarehouse     = false
#   maria_timeprofile      = false
#   maria_async_scale      = false
#   maria_async_client     = 10
#   maria_async_verbose    = false
#   maria_async_delay      = 1000
#   maria_connect_pool     = false
#  }
# 
# parameters that can be changed with vuset:
#
#  Virtual Users = 1
#  User Delay(ms) = 500
#  Repeat Delay(ms) = 500
#  Iterations = 1
#  Show Output = 1
#  Log Output = 0
#  Unique Log Name = 0
#  No Log Buffer = 0
#  Log Timestamps = 0
#
# parameters that can be changed with tcset:
#  tc_refresh_rate    = 10
#  tc_log_to_temp     = 0
#  tc_unique_log_name = 0
#  tc_log_timestamps  = 0

puts "SETTING CONFIGURATION"
dbset db maria
dbset bm TPC-C

diset connection maria_host mariadb-ephemeral
diset connection maria_port 3306

diset tpcc maria_user root
diset tpcc maria_pass pass
diset tpcc maria_dbase tpcc
diset tpcc maria_driver timed
diset tpcc maria_rampup 2
diset tpcc maria_duration 5
diset tpcc maria_timeprofile false

print dict
vuset logtotemp 1
loadscript
puts "TEST STARTED"
vuset vu 1
vucreate
tcstart
tcstatus
vurun
runtimer 500
vudestroy
tcstop
puts "TEST COMPLETE"
quit

#For Advanced configuration changes, check configuration parameters using command "print dict" in ./hammerdbcli

#Command to run the script
# ./hammerdbcli auto /dev_src/maria_tprocc_run.tcl


