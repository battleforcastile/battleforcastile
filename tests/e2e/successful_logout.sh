#!/usr/bin/expect -f

set timeout -1

spawn battleforcastile logout
set user1 $spawn_id

sleep 2

expect -i $user1 "Logout Succeeded"

expect eof