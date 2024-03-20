class Car:
    def __init__(self):
        self.color = 'blue'
        self.wheel_color = 'black'
        self.tire_color = 'navy blue'
        self.steering_wheel = 'red'
        self.tinting_color = 'black'
        self.the_model_of_the_car = 'mercedes g63'
        self.wheel = 'seven'
        self.color_headlight = 'red'
    def sound(self):
        print('beep')
    def say_sound(self):
        print('beep-beep')
mers = Car()
mers.say_sound()
mers.sound()
