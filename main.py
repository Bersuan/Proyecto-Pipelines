from argparse import ArgumentParser

def main():
    pass

def parser():
    parser = ArgumentParser(description='Devuelve la suma de los gooles marcados')
    parser.add_argument('fecha', type=str, nargs=1, help='Introduce una fecha')
    parser.add_argument('temperatura', type=float, nargs=1, help='Introduce una fecha')
    return parser.parse_args()

if __name__ == '__main__':
    args=parser()
    MediaGoles(args.fecha, args.temperatura)

    #ME DA ERROR AL IMPORTAR EL ARGPARSE