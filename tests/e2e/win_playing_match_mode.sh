#!/usr/bin/expect -f

set timeout -1

set user1_username [lindex $argv 0];
set user1_password [lindex $argv 1];

set user2_username [lindex $argv 2];
set user2_password [lindex $argv 3];

# Login User 1
spawn battleforcastile login --username ${user1_username}
set user1_login $spawn_id

sleep 1

send -i user1_login "${user1_password}\r"

# Start game --------
spawn battleforcastile play match --e2e-mode=True
set user1_game $spawn_id

sleep 1

# Login User 2
spawn battleforcastile login --username ${user2_username}
set user2_login $spawn_id

sleep 1

send -i user2_login "${user2_password}\r"

# Start game --------
spawn battleforcastile play match --e2e-mode=True
set user2_game $spawn_id

sleep 5

## Turn 1

##### User 2

# Press "1" (Valid number)
send -i $user2_game "1\r"

sleep 5

##### User 1

# Press "1" (Valid number)
send -i $user1_game "1\r"

sleep 5

## Turn 2

##### User 2

# Press "1" (Valid number)
send -i $user2_game "1\r"

sleep 5

##### User 1

# Press "1" (Valid number)
send -i $user1_game "1\r"

sleep 5

expect -i $user2_game "Congrats! You won! :)"

expect eof