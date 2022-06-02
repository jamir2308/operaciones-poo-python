class Operaciones:

    def suma(A,B,N):
        print("El resultado es: ", (A + B) % N )

    def resta(A,B,N):
        print("El resultado es: ", (A - B) % N )

    def multiplicacion(A,B,N):
        print("El resultado es: ", (A * B) % N )

    def exponenciacionModular(A,B,N):
        print("El resultado Modular es: ", A**B % N )
    
    def inversoModular(A,N):
        if (A * A**-1) % N == 1:
            print("El resultado es: ", (A * A**-1) % N)
        else:
            print("El inverso Modular no existe")
