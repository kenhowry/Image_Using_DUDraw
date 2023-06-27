"""
Explain the purpose of the program

File Name: howry_project1_drawing.py
Author: Ken Howry
Date: 22.9.14
Course: COMP 1351
Assignment: Project I
Collaborators: N/A
Internet Source: N/A
"""
import dudraw
def edward_the_cat()->None:
    #canvas
    dudraw.set_canvas_size(500, 500)
    dudraw.clear_rgb(28, 212, 196)

    #right_ear
    dudraw.set_pen_color_rgb(79, 78, 76)
    dudraw.filled_triangle(0.7, 0.6, 0.65, 0.8, 0.6, 0.7)

    #left_ear
    dudraw.set_pen_color_rgb(199, 214, 213)
    dudraw.filled_triangle(0.3, 0.6, 0.35, 0.8, 0.4, 0.7)

    #head
    dudraw.filled_circle(0.5, 0.5, 0.25)

    #right_eye
    dudraw.set_pen_color_rgb(25, 255, 221)
    dudraw.filled_ellipse(0.5 + 0.125, 0.5 + 0.05, 0.025, 0.05)

    #eye_spot
    dudraw.set_pen_color_rgb(79, 78, 76)
    dudraw.filled_circle(0.5 - 0.125, 0.5 + 0.05, .08)

    #left_eye
    dudraw.set_pen_color_rgb(255, 244, 25)
    dudraw.filled_ellipse(0.5 - 0.125, 0.5 + 0.05, 0.025, 0.05)

    #nose
    dudraw.set_pen_color_rgb(250, 196, 255)
    dudraw.filled_triangle(0.45, 0.45, 0.5, 0.40, 0.55, 0.45)

    #left_whiskers
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.line(0.3, 0.475, 0.375, 0.45)
    dudraw.line(0.3, 0.425, 0.375, 0.425)
    dudraw.line(0.3, 0.375, 0.375, 0.4)

    #right_whiskers
    dudraw.line(0.7, 0.475, 0.625, 0.45)
    dudraw.line(0.7, 0.425, 0.625, 0.425)
    dudraw.line(0.7, 0.375, 0.625, 0.4)

    #bowler_hat
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.filled_ellipse(0.5, 0.75, .06, 0.04)

    #hat_stripe
    dudraw.set_pen_color(dudraw.BOOK_RED)
    dudraw.filled_rectangle(0.5, 0.75, 0.06, 0.01)

    #hat_bottom
    dudraw.set_pen_color_rgb(0, 0, 0)
    dudraw.filled_rectangle(0.5, 0.72, 0.08, 0.015)

    #body
    dudraw.set_pen_color_rgb(199, 214, 213)
    dudraw.filled_ellipse(0.5, 0.15, 0.25, 0.25)
    #white_part
    dudraw.set_pen_color_rgb(255, 255, 255)
    dudraw.filled_ellipse(0.5, 0.01, 0.18, 0.30)
    
    #sun
    dudraw.set_pen_color(dudraw.YELLOW)
    dudraw.filled_circle(1, 1, 0.25)
    dudraw.set_pen_color_rgb(237, 143, 43)
    dudraw.set_pen_width(0.01)
    dudraw.circle(1, 1, 0.25)

#program
edward_the_cat()
dudraw.show(float('inf'))