from sqlalchemy import create_engine, MetaData, Table, ForeignKey, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# import os
# os.chdir(r'C:\Users\David\Desktop\F73-prep\kw21_js\4_köpek')

Base = declarative_base()

class Köpek(Base):
    __tablename__ = 'köpek'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    breed = Column(String)

    def __str__(self):
        return f'Breed: {self.breed} URL: {self.url}'
    def __repr__(self):
        return str(self)

engine = create_engine('sqlite:///köpek.db')
Base.metadata.create_all(engine)

def add_row(dct):
    with sessionmaker(bind=engine)() as session:
        new_dog = Köpek(url=dct['url'], breed=dct['breed'])
        session.add(new_dog)
        session.commit()


def get_dog_info(dog_id):
    with sessionmaker(bind=engine)() as session:
        dog = session.query(Köpek).filter_by(id=dog_id).first()
        return str(dog) + f' <img src={dog.url}>'


def get_all_dogs() -> str:
    with sessionmaker(bind=engine)() as session:
        result = session.query(Köpek).all()
    # print(result)
    tabelle = '\n<br>'.join( map(str, result) )
    return tabelle


if __name__=='__main__':
       
    print( get_all_dogs()  )


