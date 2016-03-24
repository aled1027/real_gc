



from pprint import pprint
import csv

def csv_to_bits(fnin, fnout):
    """
    fnin is filename of csv file to be read.
    fnout is filename of txt file to be written to.
    Takes data in csv file and prints bit representation to fnout
    """
    def my_str(x):
        # x is a binary representation
        # returns string version of x without the '0b'
        return str(x)[2:]

    data = []
    with open(fnin) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            data.append(line[0])
    txt_data = ''.join(list(map(my_str, map(bin, map(int, data)))))
    with open(fnout, 'w') as txt_file:
        txt_file.write(txt_data)

def go():
    csv_to_bits('data.csv', 'data.txt')

if __name__ == '__main__':
    go()





