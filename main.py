from loguru import logger # type: ignore



logger.add("file.log", level="ERROR")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f'{x} + {y} = {soma}')
        return soma
    except:
        logger.error("Erro ao somar. Valide os valores informados.")

soma(2, 3)
soma(2, "3")