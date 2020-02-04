from parser import parser
from functions import SumaGoles

def main():
    pass

if __name__ == '__main__':
    args=parser()
    SumaGoles(args.fecha, args.temperatura)

    #ME DA ERROR AL IMPORTAR EL ARGPARSE