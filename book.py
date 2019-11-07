import pickle

#######################################################################################################
# 
#                                               BACKUP
# 
########################################################################################################

# backup file name
backup = 'backup.data'

# try load address book from existed backup
try:
    f = open(backup, 'rb')
    address_book = pickle.load(f)
    f.close()     

# or create empty address book and backup
except FileNotFoundError:
    address_book = []
    f = open(backup, 'wb')
    pickle.dump(address_book,f)
    f.close()

    
#######################################################################################################
# 
#                                               MSG'S
# 
########################################################################################################

msg_book_is_empty = 'Address book is empty'
msg_unknown_command = 'Unknown command'
msg_welcome = '''This is address book
for choose command - enter only first letter
exapmple:   add  --> a
            del  --> d
            show --> s
What do you want to do?'''



print(msg_welcome)

while True:

    data_has_been_changed = False
    # main menu
    command = input('add/del/show/edit/quit: ')
    
    #######################################################################################################
    # 
    #                                           ADD
    # 
    ########################################################################################################
   
    if command == 'a':
        
        # boilerplate for new contact 
        new_contact = {'name': '',
                       'phone': '',
                       'email': '',
                       'group': ''}
        
        # user enters new contact details
        for key in new_contact:
            new_contact[key] = input(f'{key}: ')
            if new_contact[key] == '':
                new_contact[key] = '<not set>'
        
        new_name_is_unique = True
        
        # compare new name with existed names
        for existed_contact in address_book:
            if new_contact['name'] == existed_contact['name']:
                print(existed_contact['name'], 'already exist')
                new_name_is_unique = False
            
        # the name is unique - add to the book  
        if new_name_is_unique:
            address_book.append(new_contact)
            print(new_contact['name'], 'was added')
            data_has_been_changed = True     
    
    
    
    #######################################################################################################
    # 
    #                                            DEL
    # 
    ########################################################################################################
    
    elif command == 'd':
        
        # we cant edin empty book 
        if len(address_book) == 0:
            print(msg_book_is_empty)
            continue
        
        # user pick removal options
        delete_option = input('Delete all/name/group: ')
            
        # delete all contacs
        if delete_option == 'a':
                
            # confirm before delete all contacts
            delete_all_confirmation = input(f'Are you sure you want to delete all {len(address_book)} contacts? (y/n): ')
                
            if delete_all_confirmation == 'y':
                address_book = []
                print('All contacts was deleted!')
                data_has_been_changed = True
            
        # delete contact by name
        elif delete_option == 'n':
                
            name_for_deleted = input('Enter the name: ')                

            # compare name with existed names
            no_one_removed = True
            for contact in address_book:                    
                if contact['name'] == name_for_deleted:
                    address_book.remove(contact)
                    print(f'{name_for_deleted} was deleted')                        
                    no_one_removed = False
                    data_has_been_changed = True
            
            # name not found   
            if no_one_removed:
                print('No contact whith that name')
            
        # delete group of contacts
        elif delete_option == 'g':                
                
            command = input('Which group do you want to delete: ')

            deleted_contacts_counter = 0
            
            # compare group name with contacts group
            for contact in address_book[::-1]:
                if contact['group'] == command:
                    address_book.remove(contact)
                    deleted_contacts_counter += 1
            
            # group no found
            if deleted_contacts_counter == 0:
                print(f'Group \'{command}\' doesn\'t exist')
            
            # group found and destroyed
            else:
                print(f'{deleted_contacts_counter} contacts was deleted')
                data_has_been_changed = True            
        
        # unknown command    
        else:
            print(msg_unknown_command)

    
    
    
    #######################################################################################################
    # 
    #                                            SHOW
    # 
    ########################################################################################################
               
    elif command == 's':
       
        if len(address_book) == 0:
            print(msg_book_is_empty)
        
        else:
            command = input('Show all/name/group?: ')
            
            if command == 'a':
                for contact in address_book:
                    for key in contact:
                        print(key, contact[key],end='; ')
                    print()
                    
            elif command =='n':
                print('name case')
                
            elif command == 'g':
                print('group case')
                
            else:
                print('unknown command')
    
    
    #######################################################################################################
    # 
    #                                               EDIT
    # 
    ########################################################################################################
    
    elif command == 'e':
        
        # we cant edit emty address book
        if len(address_book) == 0:
            print(msg_book_is_empty)
            continue        
        
        # contact name for editing
        command = input('enter the name: ')        
        
        # searching contact whith required name
        i = 0        
        contac_found = False
        for contact in address_book:
            if command == contact['name']:
                contac_found = True
            else:
                i += 1
        
        # the search has not given any results 
        if not contac_found:
            print(f'{command} is not found')
        
        # search returned results
        else:
            # field selection for editing
            print('what field you wanna edit?')
            command = input('name/phone/email/group: ')            
            
            # existing field selected
            if command in address_book[i].keys():
                # print(address_book[i][command])
                address_book[i][command] = input(f'enter new {command}: ')
                print(f'{command} was changed')
                data_has_been_changed = True
            
            # nonexistent field selected
            else:
                print(f'Field {command} doesn\'t exist')
                continue
    
    
    
    
    #######################################################################################################
    # 
    #                                               EXIT
    # 
    ########################################################################################################
    elif command == 'q':
        print('See you!')
        break
    
    else:
        print(f'Unknowh command \'{command}\'')    


    #######################################################################################################
    # 
    #                                              AUTOSAVE
    # 
    ########################################################################################################
    if data_has_been_changed:
        f = open(backup, 'wb')
        pickle.dump(address_book,f)
        f.close()
        print('Backup complete')















#######################################################################################################
# 
#                                                   TO DO
# 
########################################################################################################

# SHOW
#  show name/group
#  beautify displaying

# ADD
# fix options to create noname contact
# name checking after entering new name

# MSG'S --> SYSTEM MSG'S 
# unknown command

# GLOBAL
# add or input commands

# DEL
# deleting by name works incorrect when there are 3 contacts with same name