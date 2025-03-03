import turtle

# 初始化设置
pen = turtle.Turtle()
pen.speed(2)  # 中等绘制速度
pen.pensize(4)  # 线条粗细

# 画头部
pen.circle(30)  # 半径30像素的圆

# 画身体
pen.right(90)   # 转向下方
pen.forward(100)  # 身体长度100像素

# 画手臂
# 回到身体中点
pen.backward(80)
# 左臂
pen.left(45)
pen.forward(60)
pen.backward(60)
# 右臂
pen.right(90)
pen.forward(60)
pen.backward(60)

# 画腿
pen.left(45)  # 恢复垂直方向
pen.forward(80)  # 回到身体底部
# 左腿
pen.left(45)
pen.forward(60)
pen.backward(60)
# 右腿
pen.right(90)
pen.forward(60)

pen.hideturtle()  # 隐藏乌龟光标
turtle.done()     # 保持窗口打开
