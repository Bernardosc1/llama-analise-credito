import ollama

class Empresa:
    def __init__(self, razao_social, cnae, faturamento_anual, dividas_totais, dividas_vencidas, parcelas_de_operações, certidao_federal, sem_dividas_spc, valor_alvo, objetivo_credito):
        self.razao_social = razao_social
        self.cnae = cnae
        self.faturamento_anual = faturamento_anual
        self.faturamento_mensal = self.faturamento_anual / 12
        self.dividas_totais = dividas_totais
        self.dividas_vencidas = dividas_vencidas
        self.parcelas_de_operações = parcelas_de_operações
        self.certidao_federal = certidao_federal
        self.sem_dividas_spc = sem_dividas_spc
        self.valor_alvo = valor_alvo
        self.objetivo_credito = objetivo_credito
        self.socios = []

class Socio:
    def __init__(self, nome, cpf, dividas_totais, dividas_vencidas, sem_dividas_spc, rendimentos_anuais):
        self.nome = nome
        self.cpf = cpf
        self.dividas_totais = dividas_totais
        self.dividas_vencidas = dividas_vencidas
        self.sem_dividas_spc = sem_dividas_spc
        self.rendimentos_anuais = rendimentos_anuais
        self.rendimentos_mensais = self.rendimentos_anuais / 12


pj = Empresa(
    razao_social='Martinox',
    cnae= 'Fabricação e venda de materiais metalurgicos',
    faturamento_anual= 3512324.00,
    dividas_totais= 153000,
    dividas_vencidas=0,
    parcelas_de_operações= 5600,
    certidao_federal= 'Sim',
    sem_dividas_spc= 'Sim',
    valor_alvo = 800000.00,
    objetivo_credito = 'Compra de maquinas metalúrgicas para aumento da produtividade e performance'
             )
pf = Socio(cpf='321516123', nome= 'Matheus', dividas_totais= 14000, dividas_vencidas=0, sem_dividas_spc= 'Sim', rendimentos_anuais= 152322.00)


prompt = f""""
  Você é um analista de crédito com profundo conhecimento em concessão de crédito empresarial.
    Sua missão é analisar os dados da empresa e dos sócios abaixo, identificar se há viabilidade de crédito,
    destacar os pontos fortes e fracos do perfil, sugerir melhorias para aumento da chance de aprovação
    e recomendar as melhores linhas de crédito e instituições financeiras adequadas ao caso.

    Sua análise deve ser dividida em 5 partes:

    1. **Resumo da situação atual do cliente**  
       - Situação financeira da empresa e do(s) sócio(s)  
       - Nível de endividamento, faturamento e perfil patrimonial  
       - Regularidade fiscal e documental

    2. **Pontos fortes identificados**  
       - Aspectos positivos para aprovação do crédito

    3. **Pontos de atenção ou fragilidades**  
       - Riscos ou impedimentos observados que podem dificultar a aprovação  
       - Sugestões de melhoria (Ex: aumento de pró-labore, redução de dívidas, reforço de garantias, etc)

    4. **Indicação de linha de crédito ideal para o objetivo**  
       - Linha(s) sugerida(s) com base no perfil (Ex: Pronampe, Capital de Giro com Garantia, FINAME, etc.)  
       - Requisitos da linha e por que ela é adequada

    5. **Bancos ou instituições mais indicadas**  
       - Sugestão de 1 a 3 instituições com base no perfil (relacionamento, exigências, aderência ao tipo de operação)

    Ao final, informe uma **estimativa realista do valor provável de crédito que esse cliente conseguiria** hoje com base no perfil.


Dados da Empresa:
Razão Social: {pj.razao_social}
CNAE: {pj.cnae}
Faturamento mensal: {pj.faturamento_mensal} 
Dividas totais: {pj.dividas_totais}
Dividas vencidas: {pj.dividas_vencidas}
Valor pago mensalmente em parcelas de crédito anteriores: {pj.parcelas_de_operações}
Certidão federal está sendo emitida: {pj.certidao_federal}
Está sem dividas no SPC-SERASA: {pj.sem_dividas_spc}
Valor alvo de crédito: {pj.valor_alvo}
Objetivo do crédito: {pj.objetivo_credito}

Dados do Sócio:
Nome: {pf.nome}
Dividas totais: {pf.dividas_totais}
Dividas vencidas: {pf.dividas_vencidas}
sem_dividas_spc: {pf.sem_dividas_spc}
Renda mensal do sócio: {pf.rendimentos_mensais}
"""

stream = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": prompt}
    ],
    stream = True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
