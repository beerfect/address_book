import pickle

#########################
# 
#         BACKUP
# 
##########################

backup = 'backup.data'

# find backup
try:
    f = open('backup.data')
    f.close()
    backup_doesnt_exist = False
    print('backup exist')

# create backup
except FileNotFoundError:
    backup_doesnt_exist = True
    print('Backup DOESNT exist')




if backup_doesnt_exist:
    print('we create backup')
    
    addressBook = []
    f = open(backup, 'wb')
    pickle.dump(addressBook,f)
    f.close()
    

else:    
    print('we dont need create backup')
    
    f = open(backup, 'rb')
    addressBook = pickle.load(f)
    f.close()
    
    
#########################
# 
#         MESSAGES
# 
##########################

msh_book_is_empty = 'Address book is empty'




while True:

    # needAutosave = False
    
    command = input('\nadd/del/show/edit/exit: ')
    
    #########################
    # 
    #          ADD
    # 
    ##########################
   
    if command == 'add':

        new_contact = {'name': '',
                       'phone': '',
                       'email': '',
                       'group': ''}
        
        for key in new_contact:
            new_contact[key] = input(f'{key}: ')

        contact_already_exist = False
        
        for existed_contact in addressBook:
            if new_contact['name'] == existed_contact['name']:
                print(existed_contact['name'], 'already exist')
                contact_already_exist = True
                
        if not contact_already_exist:
                addressBook.append(new_contact)
                print(new_contact['name'], 'was added')
    
    
    
    #########################
    # 
    #          DEL
    # 
    ##########################
    
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

    
    
    
    #########################
    # 
    #          SHOW
    # 
    ##########################
               
    elif command == 'show':
       
        if len(addressBook) == 0:
            print(msh_book_is_empty)
        
        else:
            command = input('all/name/group?: ')
            
            if command == 'all':
                for contact in addressBook:
                    for key in contact:
                        print(key, contact[key],end=' ')
                    print()
                    
            elif command =='name':
                print('name case')
                
            elif command == 'group':
                print('group case')
                
            else:
                print('unknown command')
    
    
    #########################
    # 
    #          EDIT
    # 
    ##########################
    
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
    
    
    
    
    #########################
    # 
    #          EXIT
    # 
    ##########################
    elif command == 'exit':
        print('See you!')
        break
    
    else:
        print('unknowh command')    


    #########################
    # 
    #          AUTOSAVE
    # 
    ########################## 
    
    print('all data was saved')    
    f = open(backup, 'wb')
    pickle.dump(addressBook,f)
    f.close()
    



# backup only when data was changed
# NO GROUP when group doesnt set
# show 