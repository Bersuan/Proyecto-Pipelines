from argparse import ArgumentParser

def parser():
    parser = ArgumentParser(description='Devuelve la suma de los gooles marcados')
    parser.add_argument('fecha', type=str, nargs=1, help='Introduce una fecha: ')
    parser.add_argument('temperatura', type=float, nargs=1, help='Introduce una temperatura: ')
    return parser.parse_args()