from random import sample

WORD_FILE_NAME = "/usr/share/dict/words"
    
    
def city_names(number=None):
    with open(WORD_FILE_NAME, 'r') as word_file:
        words = word_file.read().splitlines()
    
    cities = [word[:-4] for word in words if (
        len(word) > 4
        and word.endswith('city')
        and word.isalpha()
        and word.islower()
    )]
    
    city_count = max(0, min(
        1 if number is None else int(number),
        len(cities)
    ))
        
    return sorted(sample(cities, city_count))


if __name__ == '__main__':
    import sys   
    arguments = sys.argv[1:]
    if len(arguments) > 0:
        argument = arguments[0]
    else:
        argument = None
    for city in city_names(argument):
        print(city)
