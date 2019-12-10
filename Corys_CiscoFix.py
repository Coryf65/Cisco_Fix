## Cory's Fix for the Cisco breaking on load
import os
import getpass

text_to_replace = "<DefaultHostName>HOSTNAME</DefaultHostName>\n"
new_text = "<DefaultHostName></DefaultHostName>\n"

# getting the current user
user = getpass.getuser()
# need a easy way to ask for username in path
cisco_xml_path = os.path.abspath("C:\\Users\\" + user + "\\AppData\\Local\\Cisco\\Cisco AnyConnect Secure Mobility Client\\preferences.xml")
# holding old file values
new_stuff = ""
# Open the file, with read permissions
my_file = open(cisco_xml_path, "r")
# read the file
lines_of_file = my_file.readlines()

for line in lines_of_file:
  if line == text_to_replace:
    line = new_text
  
  print(line)
  # save new data
  new_stuff += line
my_file.close()

# dump old file
os.remove(cisco_xml_path)

# create a new file
new_dude = open(cisco_xml_path, "w")
new_dude.writelines(new_stuff)
new_dude.close()