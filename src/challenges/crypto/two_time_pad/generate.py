import binascii
import itertools

# encrypt, decrypt, xor_str fucntions come from
# the `onetimepad` Python library:
# https://github.com/jailuthra/onetimepad

# More info about this kind of attack can be found here:
# http://www.crypto-it.net/eng/attacks/two-time-pad.html
# https://samwho.dev/blog/toying-with-cryptography-crib-dragging/

def encrypt(msg, key):
    '''
    Return cipher text
    @msg: plaintext
    @key: plaintext
    ret: hex-text (aka "ascii armor")
    '''
    cipher = xor_str(msg, key)
    # ascii armor the cipher text
    cipher = (binascii.hexlify(cipher.encode())).decode()
    return cipher

def decrypt(cipher, key):
    '''
    Return plain text message
    @cipher: hex-text (aka "ascii armor")
    @key: plaintext
    ret: plaintext
    '''
    # get back the string from ascii armored cipher
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    msg = xor_str(cipher, key)
    return msg

def xor_str(a, b):
    '''
    Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.
    @a: plaintext
    @b: plaintext
    ret: plaintext
    '''
    xorred = ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xorred

def xor_hex_text(a, b):
    '''
    Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.
    @a: hex-text (aka "ascii armor")
    @b: hex-text (aka "ascii armor")
    ret: plaintext
    '''
    a = (binascii.unhexlify(a.encode())).decode()
    b = (binascii.unhexlify(b.encode())).decode()
    msg = xor_str(a, b)
    return msg

# Our two messages that will use the same OTP (key)
msg1 = "HTH{ill_t4k3_two_pl34s3}"
msg2 = "WhenIsNextTacoTuesday???"

# Our OTP (which call the `key`)
key = "randomrandomrandomrandom"

cipher1 = encrypt(msg1, key)
plaint1 = decrypt(cipher1, key)
print(f"encrypt(\"{msg1}\", \"{key}\") = {cipher1}")
print(f"decrypt({cipher1}, \"{key}\") = \"{plaint1}\"\n")

cipher2 = encrypt(msg2, key)
plaint2 = decrypt(cipher2, key)
print(f"encrypt(\"{msg2}\", \"{key}\") = {cipher2}")
print(f"decrypt({cipher2}, \"{key}\") = \"{plaint2}\"\n")

# show that: cipher1 ^ cipher2 = msg1 ^ msg2
print(f"xor_hex_text(cipher1, cipher2) = {xor_hex_text(cipher1, cipher2).encode('utf-8').hex()}")
print(f"xor_str(msg1, msg2)            = {xor_str(msg1, msg2).encode('utf-8').hex()}")

# now we need to crib drag
