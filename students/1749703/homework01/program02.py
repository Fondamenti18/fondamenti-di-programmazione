import math

def elide(a, b):
	return a[:len(a) - ((b or "b")[0] in 'aeiou')] + b
	
def conv(n):
	units = ["uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]

	if n < 20:
		return '' * (n == 0) + units[n - 1] * (0 < n < 20)
		
	tens = ["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
	prefixes = {
	#  pow   rel. prefix
		2  : "cento",
		3  : "cento",
		5  : "mille",
		6  : "mila",
		8  : "unmilione",
		9  : "milioni",
		11 : "unmiliardo",
		12 : "miliardi"
	}
	
	pow = 2 * (n < 100) + math.ceil(len(str(n)) / 3) * 3 * (n >= 100) # 2 3 6 9 12
	nc, nd = 10 ** pow, pow - (1 if pow < 4 else 3)
	
	if nd == 1:	# < 100
		prefix = tens[n // 10 - 2]
		r = conv(n % 10)
		res = elide(prefix, r)
	else: # >= 100
		nf = 10 ** nd
		f = n // nf
		prefix = conv(f) * (f > 1) + prefixes[pow] * (f > 1) + prefixes[pow - 1] * (f == 1)
		r = conv(n % nf)
		res = elide(prefix, r) * (80 <= n % 100 < 90 and pow < 5) or prefix + r
		
	return res