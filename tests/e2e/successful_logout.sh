#!/usr/bin/expect -f

set timeout -1

set username [lindex $argv 0];

spawn battleforcastile logout --username ${username}
set user1 $spawn_id

sleep 2

expect -i $user1 "Logout Succeeded"

expect eof