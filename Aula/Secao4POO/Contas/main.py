from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

cc = ContaCorrente(100, 12, 0)

cp = ContaPoupanca(1000, 1550, 2000)
cp.depositar(1000)
cp.sacar(1500)
cp.sacar(2000)

cc.sacar(50)
cc.sacar(25)
cc.sacar(26)
