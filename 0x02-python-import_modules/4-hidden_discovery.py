#!/usr/bin/python3
# 4-hidden_discovery.py
if __name__ == "__main__":
    """a program to print the contents of a compile python module"""
    import hidden_4
    contents = dir(hidden_4)
    for i in contents:
        if "__" not in i:
            print("{}".format(i))
