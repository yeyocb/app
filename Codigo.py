class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre #atributo privado
        self.__edad = edad #atributo privado
    def getNombre(self): return self.__nombre
    def getEdad(self): return self.__edad
    def mostrarInfo(self):
        return f"La persona con nombre: {self.__nombre} con edad: {self.__edad}"

#Clase derivada
class Paciente(Persona):
    def __init__(self, nombre, edad, diagnostico):
        super().__init__(nombre, edad)
        self.__diagnostico = diagnostico
    def getDiagnostico(self): return self.__diagnostico
    def mostrarInfo(self):
        return f"{super().mostrarInfo()} es de tipo Paciente y tiene el siguiente diagnonostico: {self.__diagnostico}"

#Clase derivada
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario
    def getSalario(self): return self.__salario
    def mostrarInfo(self):
        return f"{super().mostrarInfo()} es de tipo Empleado cuyo sueldo es: {self.__salario}"
    
#Clase derivada de Empleado
class Medico(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.__especialidad = especialidad
    def getEspecialidad(self): return self.__especialidad
    def mostrarInfo(self):
        return f"{super().mostrarInfo()} con la especialidad medica: {self.__especialidad}"

def main():
    per = Persona ("Juan", 25)
    pac = Paciente("Maria", 30, "Rotura de ligamentos")
    emp = Empleado("Jose", 35, 5500)
    med = Medico("Liam", 25, 6000, "Traumatologia")

    print(per.mostrarInfo())
    print(pac.mostrarInfo())
    print(emp.mostrarInfo())
    print(med.mostrarInfo())

if __name__ =="__main__":
    main()