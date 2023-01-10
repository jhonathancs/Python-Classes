from math import radians,cos,sin,tan

a = float(input('digite o angulo que vc deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))


print('para o angulo de {} grau o cos é {:.2f}'.format(a,cos))
print('para o angulo de {} grau o sen é {:.2f}'.format(a,seno))
print('para o angulo de {} grau a tan é {:.2f}'.format(a,tan))