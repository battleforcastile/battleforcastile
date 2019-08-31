#!/usr/bin/expect -f

set timeout -1

set user1_username [lindex $argv 0];
set user1_password [lindex $argv 1];

set user2_username [lindex $argv 2];
set user2_password [lindex $argv 3];

# Login User 1
spawn battleforcastile login --username ${user1_username}
set user1_login $spawn_id

sleep 2

send -i user1_login "${user1_password}\r"

expect -i user1_login "Login Succeeded"

# Start game --------
spawn battleforcastile play match --e2e-mode=True
set user1_game $spawn_id

sleep 2

expect -i user1_game "Hello ${user1_username}!"

# Login User 2
spawn battleforcastile login --username ${user2_username}
set user2_login $spawn_id

sleep 2

send -i user2_login "${user2_password}\r"

expect -i user2_login "Login Succeeded"

sleep 2

# Start game --------
spawn battleforcastile play match --e2e-mode=True
set user2_game $spawn_id

sleep 2

expect -i user2_game "Hello ${user2_username}!"

sleep 2

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

sleep 10

expect -i $user1_game "The enemy has won. Better luck next time!"

expect eof