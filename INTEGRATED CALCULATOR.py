while True:    
    operator=input('what do you want to calculate?\n')
    if operator == '+' or operator=='ADD' or operator=='add' or operator=='Add' or operator=='addition' or operator=='ADDITION' or operator=='Addition'or operator=='Sum'or operator=='SUM' or operator=='sum' or operator=='plus' or operator=='PLUS' or operator=='Plus':
        A=input('FIRST number =')
        B=input('SECOND number =')#addition
        answer=float(A)+float(B)
        a="ANSWER="
        b=str(answer)
        print('\nADDITION:-')
        print(a+b)
    if operator == '-' or operator=='sub' or operator=='difference' or operator=='diff' or operator=='subtraction' or operator=='SUBTRACTION' or operator=='Subtraction' or operator=='SUB'or operator=='Sub' or operator=='minus' or operator=='MINUS' or operator=='Minus':
        A=input('first number =')
        B=input('second number =')#substraction
        answer=float(A)-float(B)
        a="ANSWER="
        b=str(answer)
        print(a+b)
    if operator =='*' or operator=='X' or operator=='x' or operator=='.' or operator=='multi' or operator=='product' or operator=='PRODUCT' or operator=='Product' or operator=='multi' or operator=='xly' or operator=='into':
        A=input('first number =')
        B=input('second number =')#multiplication
        answer=float(A)*float(B)
        a="ANSWER="
        b=str(answer)
        print(a+b)
    if operator =='/' or operator=='division' or operator=='divide' or operator=='ratio' or operator=='RATIO' or operator=='Ratio':
        A=input('first number =')
        B=input('second number =')#division
        answer=float(A)/float(B)
        a="ANSWER="
        b=str(answer)
        print(a+b)
    if operator == '//' or operator == 'square root' or operator == 'sqrt':
        b=input('number=')#square root
        A=float(b)
        a="ANSWER="
        import math
        C=math.sqrt(A)
        B=str(C)
        print(a+B)
    if operator == '**' or operator == 'square' or operator =='squaring' or 'perfect square':
        F=input('just one number or more number\n')
        if F=='just one number':
           A=input('number=')#square 
           B=float(A)**2
           a='answer='
           b=str(B)
           print(a+b)
        if F=='more number':
            f=input('a+b form or a-b\n')
            if f=='a+b':
                A=input('first number=')
                B=input('second number=')
                C=float(A)+float(B)
                D=float(C)**2
                a='answer='
                b=str(D)
                print(a+b)
           # except :
              #  print("still this calculator can only calculate  squares for \n or for number in the form of a+b")
    if operator =='sin' or operator =='sin x' or operator =='sin 0' or operator =='sinx' :
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')        #consists some errors
            b=float(A)
            import math
            B=math.sin(b)
            C=str(B)
            a='answer='
            Z='      note:-consists 1% error'
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=math.sin(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)
            
    if operator =='cos' or operator =='cos x' or operator =='cos 0' or operator =='cosx':
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')
            b=float(A)
            import math
            B=math.cos(b)
            C=str(B)
            Z='      note:-consists 1% error'
            a='answer='
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=math.cos(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)
    if operator =='tan' or operator =='tan x' or operator =='tan 0' or operator =='tanx':
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')
            b=float(A)
            import math
            B=math.tan(b)
            C=str(B)
            Z='      note:-consists 1% error'
            a='answer='
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=math.tan(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)
    if operator =='cosec' or operator =='cosec x' or operator =='cosec 0' or operator =='cosecx':
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')
            b=float(A)
            import math
            B=1/math.sin(b)
            C=str(B)
            Z='      note:-consists 1% error'
            a='answer='
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=1/math.sin(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)
    if operator =='sec' or operator =='sec x' or operator =='sec 0' or operator =='secx':
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')
            b=float(A)
            import math
            B=1/math.cos(b)
            C=str(B)
            Z='      note:-consists 1% error'
            a='answer='
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=1/math.cos(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)        
            
    if operator =='cot' or operator =='cot x' or operator =='cot 0' or operator =='cotx':
        what=input('radian or degree\n')
        if what=='radian':
            A=input('radian=')
            b=float(A)
            import math
            B=1/math.tan(b)
            C=str(B)
            Z='      note:-consists 1% error'
            a='answer='
            print(a+C+Z)
        if what=='degree':
            a=input('degree=')
            b=(float(a)*3.142)/180
            import math
            c=1/math.tan(b)
            Z='      note:-consists 1% error'
            A='answer='
            C=str(c)
            print(A+C+Z)        
    if operator=='log' or operator =='logatithm':
        a=input('numer=')
        b=float(a)
        import math
        c=math.log10(b)
        A='anwer='
        B=str(c)
        print(A+B)
    if operator=='anti log' or operator =='anti-logarithm':
       a=input('number=')
       b=float(a)
       c=10**b
       A='anwer='
       B=str(c)
       print(A+B)
    if operator =='division_remainder':
        X=input('X= ')                  #this program is only for all value of X >Y
        Y=input('Y= ')
        Z=float(X)%float(Y)
        print(Z)
        if Z==0: print('X is exactly divisible by Y')
        else:print('X is not exactly divisible by Y')
    if operator=='gravitational force' or "gravity" or "gravitation":
        G=6.674*10**-11
        M1=input('M1(in kg)=')
        M2=input('M2(in kg)=')
        r=input('r(in m)=')
        m=float(G)*float(M1)*float(M2)
        R=float(r)**2
        F=m/R
        force=str(F)
        answer='F = '
        si_unit=' N'
        print(answer+force+si_unit)
    if operator=='gravity_mass':
        G=6.674*10**-11
        r=input('r(in m)=')
        R=int(r)**2
        M2=input('M2(in kg)=')
        f=input("F=(in N)")
        N=float(f)*float(R)
        m1=float(G)*float(M2)
        M1=N/m1
        mass='Mass='
        si_unit=' Kg'
        print(mass+str(M1)+si_unit)
    if operator=='gravitaty_distance':
        G=6.674*10**-11
        M1=input('M1(in kg)=')
        M2=input('M2(in kg)=')
        f=input('F(in N)=')
        r=(float(G)*float(M1)*float(M2))/float(f)
        import math
        R=math.sqrt(r)
        radius=str(R)
        a='distance ='
        si_unit=' M'
        print(a+radius+si_unit)
    if operator=='weight':
        M=input('mass(in Kg)=')
        g=9.81
        F=float(M)*float(g)
        si_unit=' N'
        f=str(F)
        ans='F='
        print(ans+f+si_unit)
    if operator=='energy_relativity' or "e=mc**2" or "E=mc**2" or "e=mc^2":
        mass=input('mass(in kg)=')
        C=299792458
        E=float(mass)*float(C)**2
        energy='E='
        si_unit=" joules"
        e=str(E)
        print(energy+e+si_unit)
    if operator=='torque_rpm':
        k=9.5488
        power=input('power(kW)=')
        speed=input('RPM=')
        torque=float(k)*float(power)/float(speed)
        si_unit=' N.m'
        t='torque='
        Torque=str(torque)
        print(t+Torque+si_unit)
    if operator=='rpm_torque':
        k=9.5488
        power=input('power(kW)=')
        torque=input('Torque=')
        speed=float(k)*float(power)/float(torque)
        si_unit='RPM'
        t='speed='
        Speed=str(speed)
        print(t+Speed+si_unit)
    if operator=='reynolds_number':
        v=input('velocity ( in m/s )= ')
        p=input(' Density ( in Kg/m^3)(p)= ')
        D=input(' diameter of pipe(in m)=')
        n=input(' co-efficient of viscosity=')
        Reynolds_number=(float(v)*float(p)*float(D))/float(n)
        reynolds_number=str(Reynolds_number)
        print(Reynolds_number)
        if Reynolds_number<1000:print("The given fluid's flow is laminar(streamline flow)")
        elif Reynolds_number>2000:print("The given fliud's flow is turbulant ")
        else: print("The given fluid's flow is unsteady ")
    if operator=='terminal_velocity':
        g=9.81
        r=input('radius of sphere (in m)=')
        p=input('density of sphere (in Kg/m^3)=')
        density=input('density of fluid (in Kg/m^3)=')
        n=input('co-efficient of viscosity of fluid=')
        Vt=(2/9*float(r)**2*(float(p)-float(density))*float(g))/float(n)
        velocity='Terminal velocity ='
        si_unit=' m/s'
        VT=str(Vt)
        print(velocity+VT+si_unit)
    if operator=='planck_formula':
        h=6.134*10**-34
        f=input("F(in Hz)=")
        E=float(h)*float(f)
        print(E)
    if operator=="columb's law":
        K=9*10**9
        q1=input('q1=')
        q2=input('q2=')
        r=input('distance=')
        F=(float(K)*float(q1)*float(q2))/(float(r)**2)
        f=str(F)
        a='F='
        si_unit=' N'
        print(a+f+si_unit)
     
    if operator == '+-*/':
        break
     
