class Contact:

    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number

class Contact_list():

    def __init__(self):
        self.contact_list = []

    def add_contact(self, Contact):
        auxiliary_list = [Contact.name, Contact.last_name, Contact.number]
        self.contact_list.append(auxiliary_list)

    def search_contact(self, Contact):
        flag = 0
        for i in self.contact_list:
            if i[0] == Contact.name and i[1] == Contact.last_name and i[2] == Contact.number:
                flag = 1
                for j in i:
                    print(str(j) + ' ', end='')
        if flag == 0:
            print('There is no this man, duuude')

    def remove_contact(self, Contact):
        for i in range(len(self.contact_list)):
            cl0 = self.contact_list[i][0]
            cl1 = self.contact_list[i][1]
            cl2 = self.contact_list[i][2]
            if cl0 == Contact.name and cl1 == Contact.last_name and cl2 == Contact.number:
                remove_index = i
        self.contact_list.pop(remove_index)

    def print_contacts(self):
        for i in self.contact_list:
            for j in i:
                print(str(j) + ' ', end='')
            print('\n')


subject_one = Contact('Vasily', 'Pupkin', 89260582820)
subject_two = Contact('Genadiy', 'Bejinov', 8999567232)
subject_three = Contact('Ilya', 'Kuleshov', 89280376133)
directory = Contact_list()

#directory.print_contacts()
directory.add_contact(subject_one)
directory.add_contact(subject_two)
directory.add_contact(subject_three)
directory.print_contacts()
print('----------------------------')
directory.search_contact(subject_two)
print('\n----------------------------')
directory.remove_contact(subject_two)

directory.print_contacts()
