from abc import ABC, abstractmethod

class TipoMotor(ABC):
    @abstractmethod
    def display_tipo(self):
        pass

class TipoEletrico(TipoMotor):
    def display_tipo(self):
        print("Motor Elétrico")

class TipoHibrido(TipoMotor):
    def display_tipo(self):
        print("Motor Híbrido")

class TipoCombustao(TipoMotor):
    def display_tipo(self):
        print("Motor a Combustão")



class Veiculo(ABC):
    def __init__(self, tipo_motor):
        self.tipo_motor = tipo_motor
    
    def show_motor(self):
        self.tipo_motor.display_tipo()
    
    def run(self):
        raise NotImplementedError("Ainda não implementado")

    def tipo_veiculo(self):
        raise NotImplementedError("Ainda não implementado")

class Caminhao(Veiculo):
    def run(self):
        print("Estrada para caminhoes")
    
    def tipo_veiculo(self):
        print("Caminhão")

class Automovel(Veiculo):
    def run(self):
        print("Estrada qualquer")
    
    def tipo_veiculo(self):
        print("Automovel")

class Bicicleta(Veiculo):
    def run(self):
        print("Ciclovia")
    
    def tipo_veiculo(self):
        print("Bicicleta")

class BridgePattern:
    @staticmethod
    def test():
        veiculos = [
            Caminhao(TipoCombustao()),
            Automovel(TipoHibrido()),
            Bicicleta(TipoEletrico())
        ]
        for veiculo in veiculos:
            print("Tipo Veiculo:")
            veiculo.tipo_veiculo()
            print("Tipo estrada:")
            veiculo.run()
            print("Tipo Motor:")
            veiculo.show_motor()
            print("\n")


# --------------- TESTES -----------------

BridgePattern.test()







