from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.orm import declarative_base
import random

engine = create_engine('sqlite:///Hemuppgift.db')
Base = declarative_base()

order_product = Table('order_product', Base.metadata,
                      Column('order_id', Integer, ForeignKey('order.id')),
                      Column('product_id', Integer, ForeignKey('product.id')))


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product")
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship("Order", back_populates="items")

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    orders = relationship("Order", secondary=order_product, back_populates="products")

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="orders")
    products = relationship("Product", secondary=order_product, back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

    def __init__(self, customer):
        self.customer = customer


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    orders = relationship("Order", back_populates="customer")

    def __init__(self, name):
        self.name = name


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Skapa test-data
for i in range(1, 301):
    customer = Customer(name=f"Customer {i}")
    session.add(customer)
    for j in range(1, random.randint(1, 5)):
        product = Product(name=f"Product {j}", price=random.randint(1, 100))
        session.add(product)
        quantity = random.randint(1, 4)
        order_item = OrderItem(product=product, quantity=quantity)
        order = Order(customer=customer)
        order.products.append(product)
        order.items.append(order_item)
        session.add(order)

#Denna kodsnutt skapar testdata för databasen genom att skapa kunder, produkter och ordrar.

#För varje värde i intervallet 1 till 300 skapar den en kund med ett unikt namn i formatet "Customer X", 
# där X är värdet i intervallet. Sedan skapar den ett slumpmässigt antal produkter mellan 1 och 5 för varje kund. 
# För varje produkt skapas en OrderItem som beskriver antalet produkter som ingår i ordern, och en Order som länkar produkten och kunden tillsammans med OrderItem. Till slut läggs allt till i sessionen och commit() körs för att spara all data i databasen.
session.commit()

#------------------Hämta ut data-------------------#
#----------------------------------------------------------------#
# Plocka ut bäst säljande produkter
print("Best selling products:")
results = session.query(Product, OrderItem).join(OrderItem).group_by(Product).order_by(OrderItem.quantity.desc()).limit(5).all()
for product, order_item in results:
    print(f"{product.name}: {order_item.quantity} orders")
    #Queryn använder SQLAlchemy's objektrelationella mapper (ORM) för att söka igenom tabellerna "Product" och "OrderItem" och länkar ihop dem genom att använda "join" för att hämta information från båda tabellerna. Sedan grupperar den resultaten per produkt genom att använda "group_by(Product)".
#Resultaten ordnas sedan i fallande ordning efter antalet sålda exemplar med hjälp av "order_by(OrderItem.quantity.desc())" och begränsas till de 5 mest sålda produkterna med "limit(5)". 
# Slutligen hämtas resultaten med "all()" och skrivs ut i en for-loop som skriver ut namnet på produkten och antalet sålda exemplar.

#Flest ordrar
print("Customers with most orders:")
results = session.query(Customer, Order).join(Order).group_by(Customer).order_by(Order.id.desc()).limit(5).all()
for customer, order in results:
    print(f"{customer.name}: {len(customer.orders)} orders")

# Ändra en order
order = session.query(Order).first()
order.items[0].quantity = 10
session.commit()

# Ta bort en order
order = session.query(Order).first()
session.delete(order)
session.commit()

