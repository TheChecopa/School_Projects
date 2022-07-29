from pprint import pprint, pformat

grafo = dict()

grafo = {(0, 100): [ (100, 100, 100), (200, 150, 206)],
	(100, 100): [(0, 100,100), (300, 0, 223)],
	(200, 150): [(0, 100, 206)],
    (300, 0): [(100, 100, 223)]}

str = pformat(grafo, width=60, indent=1)
print(str)