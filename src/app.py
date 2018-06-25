from controller.acoController import AcoController


def main():
    controller = AcoController()
    controller.solve()

    return


if __name__ == '__main__':
    print('\n\t-- ACO Router --')

    main()

# TODO Try-catch so no final
#    try:
#        main()
#    except Exception as err:
#        print('- Runtime error: ', err)
