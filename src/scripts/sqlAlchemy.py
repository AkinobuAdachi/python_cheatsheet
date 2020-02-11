import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
engine = sqlalchemy.create_engine('sqlite:///db/test_sqlite2.db', echo=True)
# engine = sqlalchemy.create_engine(
#     'mysql+pymysql://root@db/myapp', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

def run_script():
    Base.metadata.create_all(engine)

    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    # INSERT
    p1 = Person(name='Mike')
    session.add(p1)
    p2 = Person(name='Nancy')
    session.add(p2)
    p3 = Person(name='Jun')
    session.add(p3)
    session.commit()

    # UPDATE
    p4 = session.query(Person).filter_by(name='Mike').first()
    p4.name = 'Michel'
    session.add(p4)
    session.commit()

    # DELETE
    p5 = session.query(Person).filter_by(name='Nancy').first()
    session.delete(p5)
    session.commit()

    persons = session.query(Person).all()
    for person in persons:
        print(person.id, person.name)

    # print(
    #     session.query(Person).filter_by(name='Nancy').first().id
    # )

if __name__ == '__main__':
    run_script()