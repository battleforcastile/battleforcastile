#!/usr/bin/expect -f

set timeout -1

spawn battleforcastile play story --e2e-mode=True
set user1 $spawn_id

# Press "9" (Invalid number)
send -i $user1 "9\r"

expect -i $user1 "Invalid option"

# Press "1" (Valid number)
send -i $user1 "1\r"

# Press "Enter" (Pass)
send -i $user1 "\r"

# Press "1" (Valid number)
send -i $user1 "1\r"

expect -i $user1 "Congrats! You won this level! :)"

# It starts the second level ----------------------

# Press "1" (Valid number)
send -i $user1 "1\r"

# Press "1" (Valid number)
send -i $user1 "1\r"

expect -i $user1 "Congrats! You won this level! :)"

expect -i $user1 "You finished the story mode!"

expect eof