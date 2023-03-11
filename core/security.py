from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está corretta, comparando a senha em texto puro,
    informanda pelo usuario, e o hash da senha que estara salvo no banco de dados
    durante a criacao da conta
    """
    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return CRIPTO.hash(senha)

def decode_senha(senha: str) -> str:
    pass