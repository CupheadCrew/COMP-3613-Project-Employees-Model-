from App.database import db
from .user import User

class Company(User):
    company_name = db.Column(db.String, unique=True, nullable=False)

    company_address = db.Column(db.String(120))

    contact = db.Column(db.String())

    company_website = db.Column(db.String(120))

    # set up relationship with Listing object (1-M)
    listings = db.relationship('Listing', backref='company', lazy=True)

    def __init__(self, username, company_name, password, email, company_address, contact, company_website):
        super().__init__(username, password, email)
        self.company_name = company_name
        self.company_address = company_address
        self.contact = contact
        self.company_website = company_website
        
    def get_json(self):
        return{
            'id': self.id,
            'company_name': self.company_name,
            'email': self.email,
            'company_address':self.company_address,
            'contact':self.contact,
            'company_website':self.company_website
        }
    
    def get_name(self):
        return self.company_name
    