import pickle

#######################################################################################################
# 
#                                               BACKUP
# 
########################################################################################################

# backup file name
backup = 'backup.data'

# try load from existed backup
try:
    f = open(backup, 'rb')
    addressBook = pickle.load(f)
    f.close()     

# or create backup
except FileNotFoundError:
    addressBook = []
    f = open(backup, 'wb')
    pickle.dump(addressBook,f)
    f.close()

    
#######################################################################################################
# 
#                                               MSG'S
# 
########################################################################################################

msh_book_is_empty = 'Address book is empty'




while True:

    # main menu
    command = input('\nadd/del/show/edit/exit: ')
    
    #######################################################################################################
    # 
    #                                           ADD
    # 
    ########################################################################################################
   
    if command == 'add' or command == 'a':
        
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
        for existed_contact in addressBook:
            if new_contact['name'] == existed_contact['name']:
                print(existed_contact['name'], 'already exist')
                new_name_is_unique = False
            
        # the name is unique - add to the book  
        if new_name_is_unique:
            addressBook.append(new_contact)
            print(new_contact['name'], 'was added')        
    
    
    
    #######################################################################################################
    # 
    #                                            DEL
    # 
    ########################################################################################################
    
    elif command == 'del':
        
        if len(addressBook) == 0:
            print(msh_book_is_empty)
            
        else:
            command = input('all/name/group? ')
            
            # confirm before delete all contacts
            if command == 'all':
                command = input('are you shure? (y/n)')
                
                if command == 'y':
                    addressBook = []
                    print('all contacts was deleted')
                else:
                    continue
            
            
            elif command == 'name':
                
                someoneWasRemoved = False
                
                command = input('enter the name: ')
                i = 0
                for contact in addressBook:
                    
                    if contact['name'] == command:
                        del addressBook[i]
                        print(contact['name'], 'was deleted')
                        someoneWasRemoved = True
                    i += 1
                    
                if not someoneWasRemoved:
                    print('no contact whith that name')
            
            elif command == 'group':                
                
                command = input('enter the group: ')
                
                i = 0
                ids_for_del = []
                
                for contact in addressBook:
                    if contact['group'] == command:
                        ids_for_del.append(i)
                    i += 1
                
                if len(ids_for_del) == 0:
                    print(f'group \'{command}\' doesn\'t exist')
                
                else: 
                    for i in ids_for_del[::-1]:
                        del addressBook[i]
                    
                    print(f'group \'{command}\' was deleted')
           
            else:
                print('unknown command')

    
    
    
    #######################################################################################################
    # 
    #                                            SHOW
    # 
    ########################################################################################################
               
    elif command == 'show':
       
        if len(addressBook) == 0:
            print(msh_book_is_empty)
        
        else:
            command = input('all/name/group?: ')
            
            if command == 'all':
                for contact in addressBook:
                    for key in contact:
                        print(key, contact[key],end='; ')
                    print()
                    
            elif command =='name':
                print('name case')
                
            elif command == 'group':
                print('group case')
                
            else:
                print('unknown command')
    
    
    #######################################################################################################
    # 
    #                                               EDIT
    # 
    ########################################################################################################
    
    elif command == 'edit':
        
        # we cant edit emty address book
        if len(addressBook) == 0:
            print(msh_book_is_empty)
            continue        
        
        # contact name for editing
        command = input('enter the name: ')        
        
        # searching contact whith required name
        i = 0        
        contac_found = False
        for contact in addressBook:
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
            if command in addressBook[i].keys():
                # print(addressBook[i][command])
                addressBook[i][command] = input(f'enter new {command}: ')
                print(f'{command} was changed')
            
            # nonexistent field selected
            else:
                print('Nonexisted field')
                continue
    
    
    
    
    #######################################################################################################
    # 
    #                                               EXIT
    # 
    ########################################################################################################
    elif command == 'exit':
        print('See you!')
        break
    
    else:
        print('unknowh command')    


    #######################################################################################################
    # 
    #                                              AUTOSAVE
    # 
    ########################################################################################################
    
    f = open(backup, 'wb')
    pickle.dump(addressBook,f)
    f.close()
    print('all data was saved')















#######################################################################################################
# 
#                                                   TO DO
# 
########################################################################################################

# BACKUP
# autosave only when data was changed

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