s = float(input('qual é o salario do funcionario ? R$ '))

if s >= 1250:
    a = s*1.10
else:
    a = s*1.15

print('quem ganhanva R${:.2f} vai receber agora R${:.2f}'.format(s,a))