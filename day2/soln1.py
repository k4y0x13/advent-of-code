
with open("./input.txt", 'r') as f:
    gifts = f.readlines()

cleaned = []
for gift in gifts:
    cleaned.append(gift.removesuffix('\n'))

def wrapper(gift):
    l, w, h = [int(x) for x in gift.split('x')]
    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = l*w*h / max(l,w,h)

    return int(surface_area+slack)

print('sum:', sum([wrapper(x) for x in cleaned]))
