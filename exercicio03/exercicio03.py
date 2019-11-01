from base import Session, engine, Base
from pessoa import Pessoa
from telefone import Telefone


def popular_banco():
    session = Session()
    emerson = Pessoa("Emerson")
    juca = Pessoa("Juca")
    natalia = Pessoa("Natalia")

    # session.add(emerson)
    # session.add(juca)
    session.add(natalia)

    natalia_casa = Telefone("(48) 3242-1119", natalia)
    session.add(natalia_casa)

    session.commit()
    session.close()

if __name__ == "__main__":

    # Criando o banco de dados
    Base.metadata.create_all(engine)

    popular_banco()