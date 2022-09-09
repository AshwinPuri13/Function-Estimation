def toBin(x):
  return [int(i) for i in"{0:b}".format(x)]

def toDec(x):
  return int(''.join([str(i) for i in x]), 2)

def padList(x, pad_length):
  return [0] * (pad_length - len(x)) + x