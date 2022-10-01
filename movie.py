
import getpass

# menu print function
def print_menu(menu_options):
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# movie template
class MovieLists:
    def __init__(self,Title,Genre,Length,Cast,Director,AdminRating,shows,UserRating) :
        # taking 50 seats only for this platform
        times={show:50 for show in shows}
        self.dict={
            'title':Title,
            'genre':Genre,
            'length':Length,
            'cast':Cast,
            'director':Director,
            'adminRating':AdminRating,
            'show':times,
            'userRating':UserRating
        }
    def ini(self):
        return self.dict
    
# movie add
def adminAdd():
    name=input("Enter Movie Name\n")

    genre=input("Enter movie Genre\n")
    leng=input("Enter movie length\n")
    cast=input("Enter cast details\n")
    dire=input("Enter directore name\n")
    adminrate=input("Enter admin rating \n")
    showNum=list(input("Enter show timings seperated by comma \n").split(','))
    userRate=[]

    movie=MovieLists(name,genre,leng,cast,dire,adminrate,showNum,userRate)
    movieList.append(movie.ini())
    print(movieList)
    adminMenu()

# movie update
def adminUpdate():
    name=input("Enter the movie name \n")
    field=input("Enter the Field need to be changed\n")
    
    if field !='show':
        val=input("Enter the value\n")

        for d in movieList:
            if d['title']==name:
                    d.update((k,val) for k in d.keys() if k== field)
                    print("UPDATED\n")
                    print(movieList)
                    adminMenu()
    else:
        # update the show slots or add more slots
        print("\n1. Update existing show slots")
        print("\n2. Add new show and seats")
        print('\n3. Return Back')

        opU=int(input("Enter your choice"))
        
        for d in range(len(movieList)):
             if movieList[d]['title']==name:
                row=d

        if opU==1:
            print("SHOWS\n")
            for i in movieList[row]['show'].keys():
                print(i,end="\n")
            
            print("\n")
            key=input('Enter the show\n')
            val=int(input("Enter the new seats\n"))

            movieList[row]['show'][key]=val
            print("Updated\n",movieList[row]['show'])
            adminMenu()
      
        if opU==2:
            showNum=list(input("Enter new show timings seperated by comma \n").split(','))
            showSeat=list(input("Enter new show slots seperated by comma \n").split(','))

            newDict=dict(zip(showNum,showSeat))
            movieList[row]['show'].update(newDict)
            print("UPDATED\n",movieList[row]['show'])
            
            adminMenu()
        
        else:
            adminMenu()

# movie delete
def adminDelete():
    name=input("Enter Movie name\n")
    for i in range(len(movieList)):
        if movieList[i]['title']==name:
            del movieList[i]
            print("DELETED\n")
            print(movieList)
            adminMenu()

# movie details
def movieDetail(num):
    print("** MOVIE DETAILS **\n")
    print("Title        :",movieList[num]['title'],end='\n')
    print("Genre        :",movieList[num]['genre'],end='\n')
    print("Movie Length :",movieList[num]['length'],end='\n')
    print("Movie Cast   :",movieList[num]['cast'],end='\n')
    print("Director     :",movieList[num]['director'],end='\n')
    # if rating not present 
    if len(movieList[num]['userRating'])>0:
     rate=(sum(movieList[num]['userRating']))/(len(movieList[num]['userRating']))
    else:
        rate=0
    print("Avg User rating  :",rate,end='\n')
    
    while True:
        print("\n*************\n\n")
        print("1.Book Tickets\n")
        print("2.Cancel Tickets\n")
        print("3.Back to main menu\n")

        optionD=int(input("Enter Choice\n"))

        if optionD==1:
            print("\n\nSHOW DETAILS\n\n")
            # print show details
            for k  in movieList[num]['show'].keys():
                print(k,end='\n')
                
            print("\n")
            print("0- to return back\n")
            showNum=input("Enter Show Timing\n")

            if showNum==0:
                movieDetail(num)
            else:
                # print show seat
                print("AVAILABLE SEATS   :",movieList[num]['show'][showNum],end='\n')
                tickets=int(input("Enter Tickets"))
                if tickets<=movieList[num]['show'][showNum]:
                    # check if seat available
                    print("** TICKET BOOKED ** \n")
                    print("\n** THANKS FOR WATCHING \n Enter the rating")
                    rate=int(input("\n")
                    )
                    # get rating
                    movieList[num]['userRating'].append(rate)
                    # deduct ticket
                    movieList[num]['show'][showNum]-=tickets
                    print(movieList[num])
                   
                    userMenu()
                else:
                    # if less seats
                    print("** TICKETS NOT AVAILABLE \n")
                    movieDetail(num)
        if optionD==2:
            num=int(input("Enter the ticket number you want to Cancel"))
            # add once cancelled
            movieList[num]['show'][showNum]+=num
            print("Ticket canceled")
            movieDetail(num)
        
        else:
            userMenu()


# user,admin login
def login():
    username=''
    try:
        username=input('Enter Email\n') 
    
        pswd = getpass.getpass('Password:\n')      
 
    except:
        print('Inavlid input type')
    
    
    if '@admin.com' in username :
        # check if mail is admin type then validate
            for k in adminList:
                if k['username']==username and k['password']==pswd:
                        print('admin')
                        adminMenu()
                else:
                        print('wrong password')
                        main()
           
        
    else:
        try:
            # get the user
            filterd=list(filter(lambda person: person['username'] == username,userList)).pop()
            # validate
            if filterd['password']==pswd:
    
                userMenu()
            else:
                print("Wrong password\n")
                userMenu()
            
        except:
                print('user Not found')

# user reg template
class UserReg:
    def __init__(self,Name,userName,Phone,Age,Password) :
        self.dict={
            'name':Name,
            'username':userName,
            'phone':Phone,
            'age':Age,
            'password':Password
        }
    def ini(self):
        return self.dict

# user register
def register():
        username=input('Enter Email\n')
       
        for k in userList:
            # check if user present
            if k['username']==username:
                print("** ACCOUNT ALREADY PRESENT ** \n")
                main()
        else:
           
            user=UserReg(Name=input('Enter Name\n'),userName=username,Phone=input("Enter Phone Number\n"),Age=int(input('Enter Age\n')),Password=getpass.getpass('Enter Password\n'))
            userList.append(user.ini())
            # print(userList)
            main()
       
# main menu
def main():
 
   while(True):
        print('\n****MAIN MENU****')
        print_menu(menu_user)
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
    
        if option == 1:
           login()
        elif option == 2:
           register()
        elif option == 3:
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
            exit()

# admin menu
def adminMenu():
     while(True):
        print('\n****ADMIN MENU****')
        print_menu(menu_admin)
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
    
        if option == 1:
            adminAdd()
        elif option == 2:
            adminUpdate()
        elif option == 3:
            adminDelete()
        elif option==4:
            print('logout')
            main()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
            main()

# user menu
def userMenu():
    print("\n** WELCOME USER ***\n")
    print("LIST OF MOVIES \n Press one number")
                
    while True:
        # display all movie to user
        for i in range(len(movieList)):
            print(i+1,'--',movieList[i]['title'],'\n')
        print('\n\n 0 -- to exit menu')
        option=int(input("Enter option\n"))

        if option==0:
            main()
        elif option>0:
            movieDetail(option-1)
        
#entry point
if __name__=="__main__":
    # initialization
    userList=[]
    movieList=[]

    adminList=[
        {
        'username':'blr@admin.com',
        'password':'3456'
    },
    {
        'username':'mumbai@admin.com',
        'password':'1234'
    }]

    menu_user = {
    1: 'Login',
    2: 'Register New Account',
    3: 'Exit',

}
    menu_admin={
    1: 'Add New Movies',
    2: 'Update Movie details',
    3: 'Delete A Movie',
    4:'Admin Logout'
}


    main()