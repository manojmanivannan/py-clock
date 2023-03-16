from .mylogger import logger

# 0   ITLISASTHPMA
# 1   ACFIFTEENDCO
# 2   TWENTYFIVEXW
# 3   THIRTYFTENOS
# 4   MINUTESETOUR
# 5   PASTORUFOURT
# 6   SEVENXTWELVE
# 7   NINEDIVECTWO
# 8   EIGHTFELEVEN
# 9   SIXTHREEONEG
# 10  TENSEZO'CLOCK

class TimeFonts:

    PURPLE      = '\033[95m'
    CYAN        = '\033[96m'
    DARKCYAN    = '\033[36m'
    BLUE        = '\033[94m'
    GREEN       = '\033[92m'
    YELLOW      = '\033[93m'
    RED         = '\033[91m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'
    END         = '\033[0m'    

    #          0   1   2   3   4   5   6    7   8   9   10  11  12
    line0 =  ["I","T","L","I","S","A","S", "T","H","P","M","A"," "]
    line1 =  ["A","C","F","I","F","T","E", "E","N","D","C","O"," "]
    line2 =  ["T","W","E","N","T","Y","F", "I","V","E","X","W"," "]
    line3 =  ["T","H","I","R","T","Y","F", "T","E","N","O","S"," "]
    line4 =  ["M","I","N","U","T","E","S", "E","T","O","U","R"," "]
    line5 =  ["P","A","S","T","O","R","U", "F","O","U","R","T"," "]
    line6 =  ["S","E","V","E","N","X","T", "W","E","L","V","E"," "]
    line7 =  ["N","I","N","E","D","I","V", "E","C","T","W","O"," "]
    line8 =  ["E","I","G","H","T","F","E", "L","E","V","E","N"," "]
    line9 =  ["S","I","X","T","H","R","E", "E","O","N","E","G"," "]
    line10 = ["T","E","N","S","E","Z","O'","C","L","O","C","K"," "]

    all_lines = [line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,]
    
    time_key_maps = {
        'it'        : [0,   0,  2],
        'is'        : [0,   3,  5],
        'one'       : [9,   8,  11],
        'two'       : [7,   9,  -1],
        'three'     : [9,   3,  8],
        'six'       : [9,   0,  3],
        'twenty'    : [2,   0,  6],
        'half'      : [0,   0,  5], # Fix it, half does not exists
        'minutes'   : [4,   0,  7],
        'to'        : [4,   8,  10],

        
    }

    def __init__(self,time_sentence) -> None:
        self.time_sentence = time_sentence
        self.get_word_locations()

    def get_word_locations(self):
        logger.debug(f'Showing matrix for "{self.time_sentence}"')
        
        # from the time as sentence, take each word
        logger.debug(self.time_sentence.split(' '))
        self.word_locations = []
        for each_word in self.time_sentence.split(' '):

            logger.debug(f'Checking word "{each_word}" in lines')
            logger.debug(f'--------------------------------------')

            # check that word in each line
            for each_line in self.all_lines:

                # logger.debug(f'Checking in line {"".join(each_line).lower()}')

                if each_word.lower() in ''.join(each_line).lower():

                    logger.debug(f'MATCH found for {each_word.lower()} in {"".join(each_line).lower()}')
                    word_location = self.time_key_maps.get(each_word.lower())

                    if word_location is not None:
                        logger.debug(f'Appending location of {each_word.lower()}')
                        self.word_locations.append(word_location)

                    # if match is found break
                    break
    
    def clean_location(self,locations):
        locations = [   [0,   0,  2],
                        [0,   3,  5],
                        [2,   0,  6], 
                        [4,   0,  7], 
                        [9,   3,  8]
                    ]
        cleaned_locations = []

        def get_column(matrix, i):
            return [row[i] for row in matrix]

        def indices(lst, item):
            return [i for i, x in enumerate(lst) if x == item]


        index_col = get_column(locations,0)
        duplicates = (dict((x, indices(index_col, x)) for x in set(index_col) if index_col.count(x) > 1))
        
        logger.debug(f'Duplicates found {duplicates}')

        for dup in duplicates:
            tmp = [dup]
            for each in duplicates[dup]:
                logger.debug(f'For duplicate item {each} | {locations[each]}')
                tmp.append([locations[each][1],locations[each][2]])
                logger.debug(f'Before delting {locations}')
                del locations[0]
            cleaned_locations.append(tmp)


        for loc in locations:
            cleaned_locations.append(loc)
        

        logger.debug(cleaned_locations)

            


    def show(self):
        
        # locations = self.get_word_locations 
        # each item in this list is a word
        
        locations = self.clean_location([   [0,   0,  2],
                        [0,   3,  5],
                        [2,   0,  6], 
                        [4,   0,  7], 
                        [9,   3,  8]
                    ])
        logger.debug(locations)

        for line_no,line in enumerate(self.all_lines):
            logger.debug(f'line #{line_no}')
            for word_loc in locations:
                if word_loc[0] == line_no:
                    logger.debug(f'{word_loc}')
                    print(self.CYAN + 
                            " ".join(self.all_lines[line_no][word_loc[1]:word_loc[2]]) + 
                            " " +  
                            self.END + 
                            " ".join(self.all_lines[line_no][word_loc[2]:])
                            )

        

                        
            