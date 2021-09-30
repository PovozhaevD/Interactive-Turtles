from turtle import Turtle, ontimer


class movingTurtle(Turtle):
  def__init__(self, width):
    turtle.__init__(self)
    self.width = width

    #initial setup
    self.shape("circle")
    self.shapesize(.5, .5, 1)
    self.penup()
    ontimer(self.move_self, 1)

    #variables
    self.x_spd = 4

  def move_self(self):
    self.forward(self.x_spd)
    if self.at_edge():
      self.x_spd = -self.x_spd
    ontimer(self.move_self, 1)


    def at_edge(self):
      if self.xcor() >= self.with/2 or self.xcor() <= 