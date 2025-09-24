#! /usr/bin/env python3

from string import Template
s = "Hello hek"
lunch = ['ice', 'rice']
match lunch:
    case (flavor, "rice"):
        print(f"{flavor}")