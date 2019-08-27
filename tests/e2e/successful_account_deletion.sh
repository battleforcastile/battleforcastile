#!/usr/bin/expect -f

set timeout -1

spawn battleforcastile account delete
set user1 $spawn_id

sleep 2

expect -i $user1 "Account Deleted"

expect eof