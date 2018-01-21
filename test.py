import stardict;
import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# dict = stardict.open_dict("ecdict.csv")

# word = dict.query("persuade")

stardict.convert_dict_by_tag("cet4.sqlite","ecdict.csv","cet4")
# print(word)