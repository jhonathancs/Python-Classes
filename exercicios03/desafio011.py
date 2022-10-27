l = float(input('largura da parede: '))
a = float(input('altura da parede: '))

area = l*a
tinta = area/2

print('sua parede tem a dimensao de {}x{} e sua area é de {}m2'.format(l,a,area))
print('para pintar essa parede, voce precisara de {}l de tinta'.format(tinta))