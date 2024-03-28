# =============  Clear screen function   ================
import os


# Imported os system to create a clear() method
# The console gets clustered and hard to read and follow if
# the user keeps using the app


def clear():
    """Clears the console from all text if its called"""
    os.system('cls')


# =============  Final code  =========================

# --- OOP Email Simulator --- #


emails_dict = {
    "email1": {
        "send_email": "johndoe1234@gmail.com",
        "sub_line": "Product Specifications Inquiry",
        "content": """\nHi,

Could you please provide the specifications for your latest product line?
Specifically interested in dimensions, material, and color options.

Thanks,
John"""
    },
    "email2": {
        "send_email": "eventplanning456@yahoo.com",
        "sub_line": "Collaboration Opportunity",
        "content": """\nHi there,

We're interested in collaborating with your company.
Let's discuss further.

Best,
Marketing Team Alpha""",
    },
    "email3": {
        "send_email": "eventplanning456@yahoo.com",
        "sub_line": "Volunteer Orientation Invite",
        "content": """\nHello,

Join us for a volunteer orientation session to learn about upcoming
events and responsibilities.
Save the date!

Regards,
Event Planning Team""",
    },
}


# --- Email Class --- #
# Create the class, constructor, and methods to create a new Email object.
class Email:
    """This class initializes an object with a has_been_read variable as False

    Then it initializes an object with these attributes:

    > Sender email_address
    > subject_line
    > email_content

    It contains a method that changes a has_been_read status of the variable
    to True that the object can call.
    > mark_As_read()

    """

    # Declare the class variable, with default value, for emails.
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        """ Changes the email object has_been_read attribute to True """
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []


# --- Functions --- #
# Build out the required functions for your program.

# Create 3 sample emails and add it to the Inbox list.
def populate_inbox():
    """Generates an email object using the Email() class and populates the inbox list with
    the objects

    The emails are generated from the emails_dictionary
    """

    email1 = Email(emails_dict["email1"]["send_email"], emails_dict["email1"]["sub_line"],
                   emails_dict["email1"]["content"])
    inbox.append(email1)

    email2 = Email(emails_dict["email2"]["send_email"], emails_dict["email2"]["sub_line"],
                   emails_dict["email2"]["content"])
    inbox.append(email2)

    email3 = Email(emails_dict["email3"]["send_email"], emails_dict["email3"]["sub_line"],
                   emails_dict["email3"]["content"])
    inbox.append(email3)


# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    """Prints out all the emails in the inbox it prints the emails subject_line attribute
    and the emails corresponding number:

    > 0 email subject lines
    > 1 email subject line
    > 2 email subject line

    """
    print("\nThis is your inbox:\n")
    enum_inbox = enumerate(inbox)
    for email in enum_inbox:
        print(f"{email[0]}  {email[1].subject_line}")


# Create a function which displays a selected email.
# Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email(index):
    """Uses index argument

    Prints out the entire Email that the user chose to read
    and calls on the function mark_as_read() on that email object
    and updates the status of has_been_read to True

    If the user input index doesn't exist, it catches the exception
    and lets the user know that email doesn't exist
    """
    try:
        print(f"""
        \nEmail: {inbox[index].email_address}
        \nSubject line: {inbox[index].subject_line}
        \n{inbox[index].email_content}""")

        # marks as read and lets user know
        inbox[index].mark_as_read()
        print("This email has been marked as: Read")
    except IndexError:
        print("Sorry that Email doesn't exist \n  Check you inbox content again")


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Create a variable that triggers the end of the while loop
MENU = True

# Create a while loop that keeps requesting user input for what they want to do in the app
while MENU:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    # If a user chose to read email, clears the terminal list all emails in inbox
    # and requests input to what email they want to read.
    # Prints pout the email based on choice
    if user_choice == 1:
        clear()
        list_emails()
        email_index = int(input("\nEnter index number of Email to read: "))

        clear()
        read_email(email_index)

    # if a user chose to view unread emails, clear the terminal and print emails subject lines
    # of emails with has_been_read status as False
    elif user_choice == 2:
        clear()
        print("\nThese are the Unread emails:\n")
        for item in inbox:
            if item.has_been_read is False:
                print(f"- {item.subject_line}")

    # If a user chose to exit clears terminal and lets them know they exited
    elif user_choice == 3:
        clear()
        print("You Have closed the Emails app \nRun the program again to access the app\n")
        MENU = False

    # if the input is not on the menu lets user know
    else:
        clear()
        print("Oops - incorrect input.")
