from controller.acoController import AcoController


def main():
    controller = AcoController()
    controller.solve()

    return


if __name__ == '__main__':
    try:
        print('\n\t-- ACO Router --\n')
        main()
        print('\n----------------------------------\n')
    except Exception as err:
        print('- Runtime error: ', err)
