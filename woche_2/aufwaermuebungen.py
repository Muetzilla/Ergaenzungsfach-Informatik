from mylib.math import ifac, rfac

def count_words(text):
    words = text.split()
    word_dictionary = {}
    for i in range(0, len(words)):
        if words[i] in word_dictionary:
            word_dictionary[words[i]] =  word_dictionary[words[i]] + 1
        else:
            word_dictionary[words[i]] =  1

    print(f"Das Wort \"{max(word_dictionary, key=word_dictionary.get)}\" kommt am häufigsten vor. Die absolute Häufigkeit ist: {word_dictionary[max(word_dictionary, key=word_dictionary.get)]} und die relative Häufigkeit: {word_dictionary[max(word_dictionary, key=word_dictionary.get)]/len(word_dictionary) *100}%")


def roman_to_decimal(roman_number):
    translation_table = {"I" : 1, "V" : 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
    return 0

#Tests
number = 6
text_to_count = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem"
roman_number = "MMXXV"
print(f"Die Fakultät von {number} ist {ifac(number)}")
print(f"Die Fakultät von {number} ist {rfac(number)}")
count_words(text_to_count)
print(f"Die römische Zahl \"{roman_number}\" ist {roman_to_decimal(roman_number)}")


