class elements :

    def __init__(self, title, autor, price, disponibility, link):
        self.title = title
        self.autor = autor
        self.price = price
        self.disponibility = disponibility
        self.link = link

    def get_title(self):
        return self.title

    def get_autor(self):
        return self.autor

    def get_price(self):
        return self.price

    def get_disponibility(self):
        return self.disponibility

    def get_link(self):
        return self.link

    def set_title(self, title):
        self.title = title

    def set_autor(self, autor):
        self.autor = autor

    def set_price(self, price):
        self.price = price

    def set_disponibility(self, disponibility):
        self.disponibility = disponibility

    def set_link(self, link):
        self.link = link
        