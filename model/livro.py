from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Avaliacao

class Livro(Base):
    __tablename__ = 'livro'

    id = Column("pk_livro", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    genero = Column(String(70))
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o livro e a avaliacao.
    # Essa relação é implicita, não está salva na tabela 'livro',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    avaliacoes = relationship("Avaliacao")

    def __init__(self, nome:str, genero:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Livro

        Arguments:
            nome: nome do livro.
            genero: genero do livro
            quantidade: quantidade que se espera comprar daquele livro
            valor: valor esperado para o livro
            data_insercao: data de quando o livro foi inserido à base
        """
        self.nome = nome
        self.genero = genero
        self.quantidade = quantidade
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_avaliacao(self, avaliacao:Avaliacao):
        """ Adiciona uma nova avaliação ao livro
        """
        self.avaliacoes.append(avaliacao)

