print("""
**********
Bienvenido a Colegio:
    ____                   __    ___                   __        ________    _ ____          
   / __ \___  ____  __  __/ /_  / (_)________ _   ____/ /__     / ____/ /_  (_) / /___ _____ 
  / /_/ / _ \/ __ \/ / / / __ \/ / / ___/ __ `/  / __  / _ \   / /   / __ \/ / / / __ `/ __ \ 
 / _, _/  __/ /_/ / /_/ / /_/ / / / /__/ /_/ /  / /_/ /  __/  / /___/ / / / / / / /_/ / / / /
/_/ |_|\___/ .___/\__,_/_.___/_/_/\___/\__,_/   \__,_/\___/   \____/_/ /_/_/_/_/\__,_/_/ /_/ 
          /_/
**********                                                                                
""")

print("""
Indique concepto a pagar:
(1)-Matricula Basica
(2)-Matricula Media
""")

opcion = int(input("Seleccione: "))
matricula = 0
centroPadres = 10000
mensualidad = 30000

if opcion == 1:
    matricula = 45000
elif opcion == 2:
    matricula = 67000
else:
    print("no existe esa opcion.")
    
opcion2 = input("pagara centro de padres? (S/N): ").upper()

if opcion2 == "S":
    print()

opcion3 = input("pagara mensualidades? (S/N): ").upper()

if opcion3 == "S":
    cantidad = int(input("indique cantidad (1-12): "))

