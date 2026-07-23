from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url("https://www.python.org/robots.txt")
rp.read()
print("Can fetch /:", rp.can_fetch("*", "https://www.python.org/"))
