from turtle import Turtle, ontimer


class movingTurtle(Turtle):
  def __init__(self, width, p1, p2):
    Turtle.__init__(self)
    self.width = width
    self.p1 = p1
    self.p2 = p2

    #initial setup
    self.shape("circle")
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self, 1)

    #variables
    self.x_spd = 4
    self.collision_distance = 20

  def move_self(self):
    self.forward(self.x_spd)

    if self.at_edge():
      self.x_spd = -self.x_spd

    if self.check_collision(self.p1):
      print("crash")
      quit()

    if self.check_collision(self.p2):
      print("crash")
      quit()

    ontimer(self.move_self, 1)


  def at_edge(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False