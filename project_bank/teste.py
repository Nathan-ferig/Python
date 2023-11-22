from models.cliente import Cliente
from models.conta import Conta

Brad: Cliente = Cliente('Brad Pitt', 'bradpitt@gamil.com', '123.456.789-00', '01/05/1978')
Angelina: Cliente = Cliente('Angelina Jolie', 'angelinajolie@gamil.com', '123.456.987-00', '01/04/1984')

#print(Brad)
#print(Angelina)

contab: Conta = Conta(Brad)
contab: Conta = Conta(Angelina)

#print(contab)
#print(contab)