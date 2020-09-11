def designerPdfViewer(h, word):
    mx = 0
    for l in word:
        z = ord(l)-97
        if h[z] > mx:
            mx = h[z]
    return len(word)*mx
