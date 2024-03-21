======================  Program Description =========================

This program create a class Email()

it initializes an object with a variable has_been_read set to False
then it gives the initialized object attributes:

>   email_address
>   subject_line
>   email_content

and finally it has a class function called marked_as_read which changes
the has_been_read variable of the object that calls it to True.

the program itself has 4 functions

clear()    

* this is a function i personally taught the program could benefit
from and its function is to clear the terminal of all text on it
this is for the sake of keeping the readability and user friendlies

populate_inbox()

* This function generates 3 email objects by suing the Email class and
populates previously defined empty list named inbox

list_emails()

* This function lists the emails objects by enumerating the inbox list and
printing out the index number of each object(email) in the inbox and the
corresponding subject line attribute of the object to the index

read_email()

* This function simply prints out the email that the user wants to read
it prints out the whole contents of it (all attributes of the object) in
an easy to read format for the user. it also calls on to the class function
mark_as_read for the chosen object(email) and cages the variable has has_been_read
to True


==============================   Program    ==================================
an empty list called inbox is set 

the program uses the email_dictionary to populate the inbox
with some emails

It sets a constant variable that will trigger the while loop
to exit

Creates a while loop with user input request and a menu for
what user can chose
    1. Read an email
    2. View unread emails
    3. Quit application

if user chose 1 it clears the terminal and calls list_emails
then request user input for what email to read finally prints
out email of users choice and lets them know the email has been
marked as read

if user chose 2 it clears the terminal checks the status of 
has_been_read of all the objects(emails) in the inbox and if that
status is False it prints out the subject line for that object

if user chose 3 clears terminal if ends the while loop and lets the
user know the app is closed now

finally if user chose an option that doesn't exist it lets them know
and asks again.