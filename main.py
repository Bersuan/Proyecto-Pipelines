from parser import parser

def main():
    pass

if __name__ == '__main__':
    args=parser()
    MediaGoles(args.fecha, args.temperatura)

    #ME DA ERROR AL IMPORTAR EL ARGPARSE