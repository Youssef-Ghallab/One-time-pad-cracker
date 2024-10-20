# One-time_pad-cracker
this python code aims to crack cipher texts when one time pad is used multiple times, it leverages the properties of the space character when Xor is performed with alpha characters
The implementation is inspired by the [Many-Time Pad Cracker GitHub repository](https://github.com/riki95/Many-Time-Pad-Cracker/blob/master/cracker.py).

## Description

The Many-Time Pad (MTP) is a cryptographic method that, while theoretically secure, becomes vulnerable when the same key is used to encrypt multiple messages. This program attempts to decrypt such ciphertexts by analyzing patterns and utilizing the properties of the XOR operation.

## Features

- Converts hexadecimal ciphertexts into byte arrays.
- Checks for possible space characters in the decrypted output. (this leverages the space character properties (alpha xor space = alpha, space xor space = 0)
- Utilizes character case to infer decrypted letters. ( when a space character is discovered in one text, the xor property is leveraged to figure out the character lying on the same column on the other texts, this is done by xoring the two cipher texts to get m1 xor m2, then xoring again with the space character to get m2
- Outputs plaintexts from the ciphertexts, unknown characters are replaced with "-" character

 ## Example output:
 - -od-rn cryptogra--- -equ--es c---ful a-- -ig-r-u- a-a-----
- -dd-ess randomiz---o- co--d pr---nt ma--c-ou- -a-l -t-----
- -t -s not practi--- -o r--y so---y on --m-et-i- -nc-y-----
- - s-all never re--- -he --me p---word -- -ul-i-l- a-c-----
- -ee- review of s---r-ty --chan---s red--e- v-l-e-ab-l-----
- -ea-ning how to ---t- se--re s---ware -- - n-c-s-ar- -----
- -ec-re key excha--- -s n--ded --- symm--r-c -e- -nc-y-----
- -ec-rity at the ---e-se -- usa---ity c--l- d-m-g- s-c-----

## Guessed plaintext: 
these are my guesses for the text
- "Modern cryptography requires careful and rigorous analysis."
- "Address randomization could prevent malicious data attacks."
- "It is not practical to rely solely on symmetric encryption."
- "A user shall never reuse the same password for multiple accounts."
- "Deep review of security mechanisms reduces vulnerabilities."
- "Learning how to write secure software is a necessary process."
- "Secure key exchange is needed for symmetric key encryption."
- "Security at the expense of usability could damage success."

 ## Limitations:

 - This approach assumes that the plaintext only has letters and spaces, no numbers or special characters are used
