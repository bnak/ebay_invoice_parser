#!/usr/bin/env python

import functions


def main():
    # Access conf file by config[key] after loading file
    config = {}
    execfile("./ignore_files/project.conf", config)

    file_contents = functions.read_invoice(config["input"])
    sold_items = functions.parse_line_items(file_contents)

    for item in sold_items.keys():
        sold_items[item].display_items()

    print "Main function ran!"


if __name__ == "__main__":
    main()
