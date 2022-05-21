import turtle
import pandas
screen = turtle.Screen()
screen.title("US STATES GAME")
screen.setup(900, 800)
screen.bgpic("./blank_states_img.gif")

# 点击鼠标 显示鼠标所在的坐标
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# screen.mainloop()

answer = screen.textinput("states game", f"write the state").capitalize()
# 读取州坐标
data = pandas.read_csv("./50_states.csv")
print(data[data.state == answer])
position_data = data[data.state == answer].to_dict()
state_info = position_data["state"][34]
position_x = position_data["x"][34]
position_y = position_data["y"][34]
print(position_x, position_y)
# 在对应坐标把answer写上去
state = turtle.Turtle()
state.penup()
state.hideturtle()
state.goto(position_x, position_y)
state.write(state_info, False, "center", ("Arial", 10, "bold"))
screen.exitonclick()
