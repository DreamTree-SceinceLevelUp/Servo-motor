import Servo

servo = Servo();
servo.attach(18,50);
servo.start()

servo.write(90)
servo.end()