# Estrutura dos dados coletados (Lead)

class Lead:
    def __init__(self):
        self.tipo_imovel = None
        self.operacao = None
        self.caracteristicas = None
        self.faixa_preco = None
        self.email = None

    def __str__(self):
        return f"""
        Tipo de Imóvel: {self.tipo_imovel}
        Tipo de Operação: {self.operacao}
        Características: {self.caracteristicas}
        Faixa de Preço: {self.faixa_preco}
        E-mail: {self.email}
        """
