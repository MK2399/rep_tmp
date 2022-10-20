def hw_04_02(x):
    kvadrat = [i**2 for i in range(1, x+1)]
    print(kvadrat, *kvadrat, sep='\n')
    return
hw_04_02(3)
