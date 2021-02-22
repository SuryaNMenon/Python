class infiniteArgs:
    def __init__(self,*infargs):
        print(f"The passed arguments are {infargs}")
infiniteArgs.__init__(1, 3, 31, 5, 31, 6, 31, 3, 3)

