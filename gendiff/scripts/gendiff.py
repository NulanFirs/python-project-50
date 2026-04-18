import argparse
import json

def read_file(filepath):
    with open(filepath) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    parser.add_argument(
        '-f', '--format', 
        metavar='FORMAT', 
        help='set format of output')

    args = parser.parse_args()

    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)
    
    print(data1)
    print(data2)

if __name__ == '__main__':
    main()