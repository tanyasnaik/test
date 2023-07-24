class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def print_value(self):
        print(self.title)
        print(self.author)

book1=book('Harry Potter','JK Rowling')
book2=book('The book thief','Markus Zusak')
book3=book('Percy Jackson','Rick Riordan')
book1.print_value()
book2.print_value()
book3.print_value()