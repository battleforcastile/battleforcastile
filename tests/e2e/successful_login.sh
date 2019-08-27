#!/usr/bin/expect -f

set timeout -1

set username [lindex $argv 0];
set password [lindex $argv 1];

spawn battleforcastile login --username ${username}
set user1 $spawn_id

sleep 2

send -i $user1 "${password}\r"

expect -i $user1 "Login Succeeded"

expect eof