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


def write_location(city, x, y):
    # 在对应坐标把answer写上去
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(city)


guessed_states = []
# 这里为什么是   因为起始是 0
while len(guessed_states) < 50:
    # 首字母 大写
    answer_state = screen.textinput(f"states game {len(guessed_states)} / 50 guessed", "write the state").title()
    # 读取州坐标
    data = pandas.read_csv("./50_states.csv")
    all_states = data.state.to_list()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # get the row
        state_data = data[data.state == answer_state]
        pos_x = int(state_data.x)
        pos_y = int(state_data.y)
        write_location(answer_state, pos_x, pos_y)

    # 退出的时候 保留未猜测的州信息

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("remain_to_record.csv")
        break


