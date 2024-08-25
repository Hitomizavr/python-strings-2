string = "  ssf   s sasd asdv s sdd bawwfw    z x c h";
string = string.split(' ');
n = 0
while n < len(string):
    if string[n] == '':
        del string[n]
    else:
        n += 1
string = ' '.join(string);
print(string);