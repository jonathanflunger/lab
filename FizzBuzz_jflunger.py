#my partner was Muhamad

import sys
 
#add here all number and words with which you want to play fizzbuzz

fizzbuzz_dict = {
    3:'Fizz',
    5:'Buzz',
    7:'Fang',
    11:'Bang',
    13:'Ping',
    17:'Pong'
}

###########################################

def is_divisible(number, factor, dict):
    if number%factor == 0:
        return dict[factor]
    else:
        return number

#just need this function if you only want to play with one word
def single_fizzbuzz(number_list, factor, dict): 
    single_fizzbuzz_list = [is_divisible(num, factor, dict) for num in number_list]                 
    return single_fizzbuzz_list

def fizzbuzz_array(number_list, dict):
    fizzbuzz_array = [single_fizzbuzz(number_list,fac,dict) for fac in list(dict.keys())]
    return [list(x) for x in zip(*fizzbuzz_array)] #reshape the array
                                                   #length = length of number range, width = length of dict
 
def join_strings(number_list, dict):               #get rid of numbers and join the words, get 1d array
    string_list = []
    for package in fizzbuzz_array(number_list, dict):
        string = [elm for elm in package if isinstance(elm, str)]
        string_list.append(string)
    joined_list = [''.join(x) for x in string_list]
    return joined_list

def play_fizzbuzz(number_list, dict): #refill the blanc spaces with the corresponding numbers
    count = number_list[0]
    fizzbuzz_list = []
    for i in join_strings(number_list, dict):
        if i == '':
            fizzbuzz_list.append(count)
        else:
            fizzbuzz_list.append(i)
        count += 1
    return fizzbuzz_list

def main(num_list, dict):
    result = "\n".join("{:>10} : {:}".format(x, y) for x, y in zip(list(num_list),\
        play_fizzbuzz(num_list, dict)))
    return result

if __name__ == "__main__":
    if len(sys.argv) == 3:
        start_stop = range(int(sys.argv[1]), int(sys.argv[2])+1)
        print(main(num_list = start_stop, dict = fizzbuzz_dict))
    else:
        print('Please provide a start and stop range in order to play FizzBuzz, e.g. python Fizzbuzz_jflunger 1 100')
