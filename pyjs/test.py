import pyjd

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.Label import Label
from pyjamas import Window

from pyjamas.ui.Grid import Grid
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.TextBox import TextBox

#Constants

class RegisterWidget:
    def __init__(self):
        #We need to check if the user is already logged in
        #If the user is not logged in a form should appear
        #The form contains all data to fill a row in the User table
        #The user must accept the User Agreement and our privacy policy
        #If all fields are correctly filled a button becomes active
        #The button sends the data from the form to the server for validation
        #The server will then insert the data into the Database
        #The user can now log in.

        self.registerService = RegisterService(self);


        #UI init:
        self.nameField = TextBox()
        self.passwordField = TextBox()
        self.passwordConfirmField = TextBox()
        self.emailField = TextBox()
        self.ssnField = TextBox()
        self.phoneField = TextBox()
        self.zipCodeField = TextBox()
        self.addressField = TextBox()

        self.statusLabel = Label()
        self.registerButton = Button()

        self.buildForm()


    def buildForm(self):
        formGrid = Grid(2, 10)
        formGrid.setVisible(False)

        formGrid.setWidget(1, 0, self.statusLabel)
        formGrid.setWidget(0, 1, Label("Name: "))
        formGrid.setWidget(1, 1, self.nameField)
        formGrid.setWidget(0, 2, Label("Password: "))
        formGrid.setWidget(1, 2, self.passwordField)
        formGrid.setWidget(0, 3, Label("Password: "))
        formGrid.setWidget(1, 3, self.passwordConfirmField)
        formGrid.setWidget(0, 4, Label("E-mail: "))
        formGrid.setWidget(1, 4, self.emailField)
        formGrid.setWidget(0, 5, Label("SSN: "))
        formGrid.setWidget(1, 5, self.ssnField)
        formGrid.setWidget(0, 6, Label("Phone: "))
        formGrid.setWidget(1, 6, self.phoneField)
        formGrid.setWidget(0, 7, Label("Address: "))
        formGrid.setWidget(1, 7, self.addressField)
        formGrid.setWidget(0, 8, Label("Zip Code: "))
        formGrid.setWidget(1, 8, self.zipCodeField)

        self.formGrid = formGrid

        RootPanel().add(formGrid)


#Not sure how this class is supposed to be yet.
class User:
    def __init__(self, name = "", ssn = "", address = "", email = "", zipCode = "", phone = "", password = ""):
        self.name = name
        self.ssn = snn
        self.address = address
        self.email = email
        self.zipCode = zipCode
        self.phone = phone
        self.password = passwoFailedrd

class RegisterService:
    def __init__(self, callback):
        self.callback = callback

    def addUser(self, user):
        self.callback.service_eventAddUserSuccessful()

    def updateUser(self, user):
        self.callback.service_eventUpdateUserSuccessful()

    def removeUser(self, user):
        self.callback.service_eventRemoveUserSuccessful()



if __name__ == __main__:
    pyjd.setup("templates/register.html")
