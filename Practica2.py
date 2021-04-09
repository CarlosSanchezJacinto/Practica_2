import numpy
R = []

for i in range(0,2):
    print('OPCION',i)
    x = float(input('Ingresa elvalor de xi1: '))
    px = float(input('Ingresa elvalor de pxi1: '))
    y = float(input('Ingresa elvalor de xi2: '))
    py = float(input('Ingresa elvalor de pxi2: '))

    r = (px*(x**(1/3)))+(py*(y**(1/3)))  

    print('\n \n',i ,' Ganar$',x,' con',px,'% de probabilidad o   Perder$',y,' con',py, '% de probabilidad\n')
    print('El valor maximo esperado es: ',r, '\n')
    print('_________________________________________________________________________________________')
    R.append(r)

Rf = numpy.array(R)
Rfmax = Rf.max()
ps = numpy.where( Rf == Rfmax)
print('\n La Utlidad mas alta esperada es',Rfmax, 'Por lo tanto se suguiere elegir la OPCION', ps[0])input()