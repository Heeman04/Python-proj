from turtle import*
speed('slowest')


# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# mainloop()



#fd(100)
#lt(60)
#fd(100)
#lt(60)
#fd(100)
#lt(60)
#fd(100)
#lt(60)
#fd(100)
#lt(60)
#fd(100)
#lt(80)

#mainloop()




fillcolor('red')
side = 7
begin_fill()
for i in range(side):
    fd(100)
    lt(360/side)
end_fill()
hideturtle()
mainloop()