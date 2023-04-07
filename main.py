from functions import *

way = 'operations.json'


def main():
    print('main')
    box_list = born_list(way)
    box_list = filter_by_state(box_list)
    box_list = sort_by_date(box_list)
    box_list = formated_output(box_list)
    for d in box_list:
        print(d)
        print('\n\n')


if __name__ == '__main__':
    main()
