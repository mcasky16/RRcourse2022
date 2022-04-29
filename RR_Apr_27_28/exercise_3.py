import us  # Module that contains information of states in USA
import pandas as pd  # Pandas module to help with data frame


list = us.states.mapping('abbr','name')  # Extracting the states from the us module

# Making a loop to make a list of states
uppercase_states = ['UpperCase']
for i in list:
    state_name = list[i].upper()  # Changes the list to capital letters
    uppercase_states += [state_name]
    
    
lowercase_states = ['LowerCase']
for i in list:
    state_name = list[i].lower()  # Changes the list to small letters
    lowercase_states += [state_name]
    
# Making a data frame from the two list
data_frame = pd.DataFrame(uppercase_states,lowercase_states)

# Creating a csv file to the active directory
data_frame.to_csv('file1.csv', header = True)