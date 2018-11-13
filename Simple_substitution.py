import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
   message = ''
   if len(sys.argv) > 1:
      with open(sys.argv[1], 'r') as f:
         message = f.read()
   else:
      message = input("Enter your message: ")
   mode = input("[E]ncrypt|[D]ecrypt: ").upper()
   if mode not in ['E','D']:
      print("Error: mode is not Found!"); raise SystemExit
   key = ''
   k_1 = input("Enter key (leave blank for random key): ")
   if k_1 == '':
      key = getRandomKey()
   else:
      k_2 = set(LETTERS) - set(k_1)
      key = "".join([j for i,j in enumerate(k_1) if j not in k_1[:i]]) + (''.join(sorted(set(k_2))))
   translated = translateMessage(message, key, mode)
   print("Our real  alphabet will be: ", LETTERS)
   print("The cipheralphabet will be: ", key)
  
   
   if len(sys.argv) > 1:
      fileOut = 'enc.' + sys.argv[1]
      with open(fileOut, 'w') as f:
         f.write(translated)
      print('Success! File written to: %s' % (fileOut))
   else: print('Result: ' + translated)

def translateMessage(message, key, mode):
   translated = ''
   charsA = LETTERS
   charsB = key
   
   
   if mode == 'D':
      charsA, charsB = charsB, charsA
   for symbol in message:
      if symbol.upper() in charsA:
         symIndex = charsA.find(symbol.upper())
         if symbol.isupper():
            translated += charsB[symIndex].upper()
         else:
            translated += charsB[symIndex].lower()
      else:
         translated += symbol
   return translated

def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)

if __name__ == '__main__':
    main()

#MY KEY - CIPHERABDFGJKLMNOQSTUVWXYZ
    #PMKNUTEQ
