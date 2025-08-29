def main():
    s = input()
    print(convert(s))
def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str
main()