# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:34:44 2024

@author: maana
"""

import turtle

def koch_snowflake(t,length,levels):
    if levels == 0:
        t.forward(length)
        return
    else:
        length = length/3

        koch_snowflake(t, length, levels-1)
        t.left(60)
        koch_snowflake(t, length, levels-1)

        t.right(120)
        koch_snowflake(t, length, levels-1)

        t.left(60)
        koch_snowflake(t, length, levels-1)





t = turtle.Turtle()
t.hideturtle()
t.color('black')

for i in range(3):
    koch_snowflake(t, 200, 4)
    t.right(120)


t.mainloop()