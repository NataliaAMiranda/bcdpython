from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

if __name__ == '__main__':

    engine = create_engine('sqlite:///lab05-ex02.sqlite')

    Session = sessionmaker(bind=engine)
    session = Session()

    # Nome das tabelas: Pessoa Telefone

    Base = automap_base()
    Base.prepare(engine, reflect= True)

    Pessoa = Base.classes.Pessoa
    Telefone = Base.classes.Telefones

    pessoas = session.query(Pessoa).all()

    # for p in pessoas:
    #     print("Id: {}".format(p.idPessoa))
    #     print("Nome: {}".format(p.nome))

    pessoas = session.query(Pessoa).filter(Pessoa.nome.ilike('J%')).all()

    # for p in pessoas:
    #     print("Id: {}".format(p.idPessoa))
    #     print("Nome: {}".format(p.nome))


    pessoas = session.query(Pessoa).join(Telefone).all()

    for p in pessoas:
        print("Id: {}".format(p.idPessoa))
        print("Nome: {}".format(p.nome))
        for t in p.telefones_collection:
            print("Tel: {}".format(t.numero))
