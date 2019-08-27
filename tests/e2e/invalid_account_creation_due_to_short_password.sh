#!/usr/bin/expect -f

set timeout -1

set email [lindex $argv 0];
set username [lindex $argv 1];
set password [lindex $argv 2];

spawn battleforcastile account create --email ${email} --username ${username}
set user1 $spawn_id

sleep 2

send -i $user1 "${password}\r"

expect -i $user1 "password too short (minimum 8 characters)"

expect eof