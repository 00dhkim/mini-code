# 2019.06.09. Kim DoHyun for just fun

table = {
 'a':'0110'
,'b':'00010'
,'c':'01111'
,'d':'0010'
,'e':'111'
,'f':'101001'
,'g':'11001'
,'h':'00111'
,'i':'1101'
,'j':'11000000'
,'k':'101000'
,'l':'10101'
,'m':'00011'
,'n':'010'
,'o':'01110'
,'p':'110001'
,'q':'1100000100'
,'r':'1011'
,'s':'1001'
,'t':'1000'
,'u':'0000'
,'v':'1100001'
,'w':'001101'
,'x':'1100000101'
,'y':'110000011'
,'z':'001100'
}

def bitsToChar(bits):
    for i in range(ord('a'),ord('z')+1):
        if(table[chr(i)] == bits):
            return chr(i)

# START INCODING
bits = list()
input_strings = list(input('Input strings:\n'))
input_size = len(input_strings)
input_strings.reverse()

while(input_strings):
    c = input_strings.pop()
    bits.append(table[c])
# END INCODING

'''
for x in bits:
    print(x)
'''

# START DECODING
bits = list(''.join(bits))
bits_size = len(bits)
bits.reverse()

output_strings = list()

while(bits):
    s = ''
    while(s not in table.values()):
        s += bits.pop()
    output_strings.append(bitsToChar(s))
# END DECODING

print('','###########RESULT###########','',''.join(output_strings),sep='\n')

print('input size:',input_size*8,'bit')
print('compressed size:',bits_size,'bit')
print('comression rate: %f'%(bits_size/input_size/8))
