#!/usr/bin/expect -f

set timeout -1

spawn battleforcastile play story --e2e-mode=True
set user1 $spawn_id

# Press "1" (Valid number)
send -i $user1 "1\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "1" (Valid number)
send -i $user1 "1\r"

expect -i $user1 "You lost... Please try again!"

expect eof