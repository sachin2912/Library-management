import datetime


class DLL(object):
    ''' class to create a Double Linked list using class student's objects as elements'''
    def __init__(self):
        self.head = None
        
    def add(self, new_obj):
        ''' method to add node at the end of the linked list'''
        
        if self.head is None:
            self.head = new_obj
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_obj
            new_obj.prev = curr
            
    
    def remove(self, key):
        ''' method to remove the given key/element fro the linked list, if present'''
        curr = self.head
        if curr is None:
            print("List is already empty!")
        elif curr.prn == key:
            self.head = curr.next
            curr.next.prev = None
            print("Removing", key, "...")
            print("\t", key, 'removed successfully from list!')
        else:
            flag = 0
            while curr.next:
                if curr.prn == key:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr = None
                    flag = 1
                    break
                curr = curr.next
            else:
                if curr.next is None and curr.prn == key:
                    curr.prev.next = None
                    curr = None
                    flag = 1
            print("Removing", key, "...")
            print(str(key)+' removed successfully from list!' if flag else str(key)+' not found in list!')        
                
    def search(self, key):
        ''' method to search the given key/element in the linked list'''
        curr = self.head
        if curr is None:
            #print("List is already empty!")
            return None
        else:
            print("Searching", key, "...")
            while curr:
                if curr.prn == key:
                    #print("\t", key, "found in list between", curr.prev.data, "and", curr.next.data)
                    return curr
                curr = curr.next
            else:
                #print(key, "not present in the list!")
                return None
    
    
    def display(self):
        
        curr = self.head
        if curr is None:
            print( 'List is empty!')
        else:
            print ('Student List is:\n')
            while curr:
                print('PRN : ',curr.prn ,' Name ' ,curr.name,' Email: ',curr.email,' Books record : ',(curr.books_issued))
                curr = curr.next
                            


class Student(object):
    """Class for students Details"""
    def __init__(self, name, prn, branch, email):
        self.name = name
        self.prn = prn
        self.branch = branch
        self.email = email
        self.status=int(0)
        self.books_issued=[]
        self.next=None
        self.prev=None
    
    @property
    def prn(self):
        return self.__prn

    @prn.setter
    def prn(self, prn):
        while True:
            if len(prn) != 10 or prn.isnumeric() == False or prn == None:
                print("Error: enter 10 DIGIT number")
                prn = input("Enter PRN: ")
            else:
                self.__prn = prn
                break
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        while True:
            if email[-13:] != '@mitaoe.ac.in':
                email = input("Enter valid Email: ")
            else:
                self.__email = email
                break

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, branch):
        b = ['IT', 'Computer', 'Electrical', 'Civil', 'Chemical', 'Mechanical']
        while True:
            if branch not in b:
                print("Enter correct branch (IT, Computer, Electrical, Civil, Chemical, Mechanical)")
                branch = input("Enter branch: ")
            else:
                self.__branch = branch
                break




class student_reg(object):
    """Class for the staff of Library to manage the students data """

    
    @staticmethod
    def registerStudent(studll):
        
        name = input("Enter name: ")
        prn = input("Enter prn: ")
        branch = input("Enter branch: \n"+\
                       "\ta) IT\n"+\
                       "\tb) Computer\n"+\
                       "\tc) Electrical\n"+\
                       "\td) Civil\n"+\
                       "\te) Chemical\n"+\
                       "\tf) Mechanical\n")
        email = input("Enter college email id: ")
        
        studll.add(Student(name, prn, branch, email))
        print("\n {} is registered".format(name))
    

    @staticmethod
    def delStudent(studll):
        pn = input("PRN to delete : ")
        studll.remove(pn)

    


class books(object):
    """ Books class for books details """
    def __init__(self,bname,author,quantity):
        self.bname=bname
        self.author=author
        self.quantity=quantity
        self.book_holders=[]
        self.left=None
        self.right=None

class books_data(object):
    """books_data to manage the books by library staff """
    root=None                                 # BST root value
    @staticmethod
    def add_book():                             # to add a book
        ch=1
        while ch==1:
            print ("Enter the following details: ")
            bname=input("Book name : ")
            author=input("Author: ")
            quantity=int(input("Quantity : "))
            temp=books(bname,author,quantity)
            books_data.root=insert_books(books_data.root,temp)
            ch=int(input("Press 1 to add More Books ...  "))


    @staticmethod
    def show_books():                                          # to display all the books
        print ("The Books available in Library")
        print ("Book Name \t       Author \t   Quantity Available")
        display(books_data.root)        

    @staticmethod
    def search(key):                                         # to search a particular book
        
        temp=search(books_data.root,key)
        if temp is not None:
            return temp
        else:
            print ("No Such book is found !!")
            return None        
    
    @staticmethod
    def update_quantity(task,temp):                           # update the quantity of a book after issue or return
        if task==1:
            temp.quantity-=1
        elif task == 2:
            temp.quantity+=1    




def insert_books(root,node):                                # bst way of addtion of book
    if root is None:
        root=node
        
    else:
        if root.bname<node.bname:
            if root.right is None: 
                root.right = node 

            else:
                insert_books(root.right,node)
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert_books(root.left, node)
    return root


def display(root):                                   # bst inorder way to display 
    if root is not None:
        display(root.left)
        print(root.bname," \t\t ",root.author," \t\t ",root.quantity)
        display(root.right)



def search(root,key):                                     # bst search
    if root is None or root.bname == key: 
        return root 
  
    if root.bname < key: 
        return search(root.right,key) 
    
    return search(root.left,key) 
            

class library(object):
    """to manage the library day to day work like books issue and return"""
    @staticmethod
    def issue_book(student):                                     # issue of books
        bk=input("Enter Book Name : ")
        root_b=books_data.search(bk)
        if root_b is not None:
            if student.status >= 2:
                print (" Sorry Only two books allowed at a time")
               
            else:
                if root_b.quantity != 0:
                    fl=0
                    for j in student.books_issued:
                
                        if j[0] == bk and len(j)<5:
                            fl=1
                            break

                    if fl==1:
                        print (bk," CURRENTLY ISSUED TO YOU ")
                    else:
                        tod = datetime.date.today().strftime("%d-%m-%Y")
                        student.books_issued.append(list((root_b.bname,root_b.author,tod,"Issued")))
                    
                        books_data.update_quantity(1,root_b)                                # 1 denotes task code for Issue
                        root_b.book_holders.append(list((student.prn,student.name,tod)))
                        student.status+=1
                        print (" Book Successfully Issued ")
                else:
                    print ("Sorry Book unavailable !!!")


    @staticmethod
    def return_book(student):                                  # to return a book
        if student.status == 0:
            print ("No Books to be returned !!!")
        else:
            bk_name=input("Book name : ")
            fl=0
            
            for b in student.books_issued:
                
                if bk_name == b[0]:
                    
                    tod = datetime.date.today().strftime("%d-%m-%Y")
                    b.extend([tod,"Returned"])
                    
                    fl=1
                    root_b=books_data.search(bk_name)
                    
                    books_data.update_quantity(2,root_b)                        # 2 denotes the task code for return
                    for i in root_b.book_holders:
                        if student.prn==i[0]:
                            root_b.book_holders.remove(i)
                            break
                    
                    student.status-=1
                    print (bk_name," Returned Successfully ")
                    break
            
            if fl==0:
                print ("No Book Found !!")


def books_holders_data():                                         # to know the who has a particular book
    bk_name=input("Book Name : ")
    root_b=books_data.search(bk_name)
    if root_b is not None:
        print ("Student PRN \t \t Student Name \t  Date of issue")
        for i in root_b.book_holders:
            print (i)

    else:
        print ("No Such Book Exist!!")
    

def main():
    """Main """
    
    studll=DLL()
    ch=1
    while ch==1:
        print("\n{} Welcome TO The Library {}\n".format("="*25, "="*25))
        print("Select Who you are: ")
    
        user = int(input("press '1' for Student and '2' for Teacher: "))
    
        while user != 1 and user != 2:
            print("Ooops! You are none of them!")
            break    
    
        else:
    
            if user == 2:
                print("\n{} Welcome TO TEACHER's MENU {}\n".format("-"*25, "-"*25))
                while True:
                    
        
                    print("\nSelect the option: ")
                    print("1) Register the student.\n2) Delete the Student.\n3) See the list of students.\n4)Add Books \n5) Search Books holder \n6) EXIT Teacher's Menu")
                    opt = int(input())
            
                    if opt == 1:
                        student_reg.registerStudent(studll)
                
                    elif opt == 2:
                        student_reg.delStudent(studll)
                
                    elif opt == 3:
                        studll.display()

                    elif opt==4:
                        books_data.add_book()

                    elif opt == 5:
                        books_holders_data()

                    elif opt == 6:
                        print("Thank You!")
                        break
                    else:
                        print (" Wrong Choice (1-6 only)")    
                    print("\n{}\n".format("-"*50))
        
            elif user == 1:
                print("\n{} Welcome TO STUDENT's MENU {}\n".format("-"*25, "-"*25))
        
                pn=input("PRN : ")
                stu_addr=studll.search(pn)
        
                if stu_addr is not None:
        
                    while True:
                        print("\nSelect the option: ")
                        print("1) Explore the library.")
                        print("2) Take the book.")
                        print("3) Return the book.")
                        print("4) See your status.")
            
                        print("5) EXIT Student' Menu")
                        opt = int(input())

                        if opt == 1:
                            books_data.show_books()
        
                        elif opt == 2:
                            library.issue_book(stu_addr)
        
                        elif opt == 3:
                            library.return_book(stu_addr)
        
                        elif opt == 4:
                            print("List of Books Issued \n",stu_addr.books_issued)
                
                        elif opt == 5:
                            print("Thank You!")
        
                            break
                        else:
                            print ("Wrong Choice (1-5 only)")    
                        print("\n{}\n".format("-"*50))
        
                else:
                    print ("PRN NOT FOUND !!!!")
                    print ("Register Yourself with the Library to avail the Facilities \n Thank You")
    
        ch=int(input("Press 1 to go MAIN MENU ...   "))


if __name__ == "__main__":
    main()



