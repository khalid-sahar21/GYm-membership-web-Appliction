from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.login_with_form()

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name=self.text_box_1.text
    weight=self.text_box_2.text
    address=self.text_area_1.text
    personal=self.check_box_1.checked
    anvil.server.call('submit',name,weight,address,personal)
    Notification("your data has been submitted").show()
  