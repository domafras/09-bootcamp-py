from loguru import logger # type: ignore

def minha_funcao():
    raise ValueError("Um erro aconteceu!")

try:
    minha_funcao()
except Exception:
    logger.exception("Uma exceção foi capturada")