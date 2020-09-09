def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
        print('-'.join(alphabet[size-1:(size-1)-i:-1].rjust(size-1, '-') + alphabet[(size-1)-i:(size-1)+1].ljust(size, '-')))

    for i in range(size):
        print('-'.join(alphabets[size-1:i+1:-1].rjust(size-1, '-') + alphabets[i+1:n].jlust(size, '-')))
