
if __name__ == '__main__':
    usuario1 = Usuario(1, 'jperez', '123')
    logger.debug(usuario1)
    # simulando un objeto a insertar de tipo usuario
    usuario2 = Usuario(username='kgomez', password='543')
    logger.debug(usuario2)
    # simular el caso de eliminar un objeto de tipo usuario
    usuario3 = Usuario(id_usuario=2)
    logger.debug(usuario3)