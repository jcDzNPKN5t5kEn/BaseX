def baseX_encode(data, characters):
    base = len(characters)
    result = []
    num = int.from_bytes(data, byteorder='big')
    while num > 0:
        num, rem = divmod(num, base)
        result.append(characters[rem])
    result.reverse()
    return ''.join(result)

def baseX_decode(encoded_data, characters):
    base = len(characters)
    num = 0
    for char in encoded_data:
        num = num * base + characters.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big')



###### test ######
def hex_range_to_string(start_hex, end_hex):
  return ''.join(chr(i) for i in range(start_hex, end_hex + 1))

data = '''The intrinsic nature of reality, as it is perceived, is a perpetually evolving paradigm, a dynamic mosaic of interrelated experiences and interpretations that resists definitive categorisation or rigid labelling. Thus, to assert that something is simply "is" implies a static state of being, a fixed point in the ever-changing river of time and existence. Upon closer examination, however, this proves to be an illusion, a convenient fiction that we construct to impose a semblance of order upon a fundamentally chaotic and ultimately unknowable universe. Similarly, the ship at sea is never truly at rest, buffeted by currents both seen and unseen. Individuals and species are also perpetually in flux, evolving, adapting, and redefining themselves in response to the myriad forces that shape their collective journey through this grand, perplexing, and ultimately inexplicable cosmic dance.'''.encode('utf-8')
# custom_characters = r''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~''' # base94
# custom_characters = ''.join(chr(i) for i in range(128)).replace("\x00", "").replace("\x10", "").replace("\x13", "").replace("\x34", "").replace("\x38", "").replace("\x92", "") # all ascii characters
custom_characters = hex_range_to_string(0x1F600, 0x1F64F) + hex_range_to_string(0x1F300, 0x1F5FF) + hex_range_to_string(0x1F900, 0x1F9FF) #some emjios

encoded_baseX = baseX_encode(data, custom_characters)
decoded_baseX = baseX_decode(encoded_baseX, custom_characters)

print(encoded_baseX)
print('len=',len(encoded_baseX))
print(decoded_baseX)
print('len=',len(decoded_baseX))
print(len(encoded_baseX) / len(decoded_baseX))