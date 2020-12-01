import random
 
def random_value():
    value = random.randint(0,9);
    return value;

def random_position():
    string_position = '';
    names1 = [1,1,2,2,2,1,1,2,2,2];
    names2 = ['k','q','r','n','b','K','Q','R','N','B'];
    for i in range(8):
        value = random_value();
        while (names1[value] == 0) or  (value >4):
            value = random_value();
        names1[value] -=1;
        string_position += names2[value];
    string_position += "/pppppppp/8/8/8/8/PPPPPPPP/";
    for i in range(8):
        value = random_value();
        while (names1[value] == 0) or (value <5):
            value = random_value();
        names1[value] -=1;
        string_position += names2[value];
    string_position += " w KQkq - 0 1";
    return (string_position)