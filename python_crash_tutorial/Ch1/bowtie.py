# bowtie.py
# Draw a bowtie

from turtle import *

pensize(7)
penup()
goto(-200, -100)
pendown()
fillcolor("red")
begin_fill()
goto(-200, 100)
goto(200, -100)
goto(200, 100)
goto(-200, -100)
end_fill()

exitonclick()
