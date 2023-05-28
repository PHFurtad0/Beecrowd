while True:
    try:
        Reclamaçoes = int(input())
        if Reclamaçoes == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break        