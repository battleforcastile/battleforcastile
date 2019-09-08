#!/usr/bin/env bash

EMAIL1=$0
USERNAME1=$1
PASSWORD1=$2

EMAIL2=$3
USERNAME2=$4
PASSWORD2=$5

EMAIL3=$6
USERNAME3=$7
PASSWORD3=$8  # SHORT PASSWORD

pipenv install --dev --python 3.6
pipenv run pip install -e .

cd tests/e2e

echo "Scenario: Successful account creation"
pipenv run ./successful_account_creation.sh ${EMAIL1} ${USERNAME1} ${PASSWORD1}
pipenv run ./successful_account_creation.sh ${EMAIL2} ${USERNAME2} ${PASSWORD2}

echo "Scenario: Invalid account creation due to duplicated email"
pipenv run ./invalid_account_creation_due_to_duplicated_email.sh ${EMAIL1} ${USERNAME2} ${PASSWORD2}

echo "Scenario: Invalid account creation due to duplicated username"
pipenv run ./invalid_account_creation_due_to_duplicated_username.sh ${EMAIL2} ${USERNAME1} ${PASSWORD2}

echo "Scenario: Invalid account creation due to short password"
pipenv run ./invalid_account_creation_due_to_short_password.sh ${EMAIL3} ${USERNAME3} ${PASSWORD3}

echo "Scenario: Successful login"
pipenv run ./successful_login.sh ${USERNAME1} ${PASSWORD1}

echo "Scenario: Lose when playing story mode"
pipenv run ./lose_playing_story_mode.sh

echo "Scenario: Win when playing story mode"
pipenv run ./win_playing_story_mode.sh

echo "Scenario: Win when playing match mode"
pipenv run ./win_playing_match_mode.sh ${USERNAME1} ${PASSWORD1} ${USERNAME2} ${PASSWORD2}

echo "Scenario: Successful login"
pipenv run ./successful_login.sh ${USERNAME1} ${PASSWORD1}

echo "Scenario: Successful logout"
pipenv run ./successful_logout.sh ${USERNAME1}

echo "Scenario: Already logout"
pipenv run ./already_logout.sh ${USERNAME1}

echo "Scenario: Successful account deletion"
pipenv run ./successful_login.sh ${USERNAME1} ${PASSWORD1}
pipenv run ./successful_account_deletion.sh
pipenv run ./successful_login.sh ${USERNAME2} ${PASSWORD2}
pipenv run ./successful_account_deletion.sh