from parser import parser
from functions import SumaGoles

def main():
    pass

if __name__ == '__main__':
    fecha, temperatura=parser()
    SumaGoles(fecha, temperatura)

    #ME DA ERROR AL IMPORTAR EL ARGPARSE