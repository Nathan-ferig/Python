"""
This is a coding exercise.
It aims to show the use of Classes and Typing Hints in Python

It was taken from the online course:
https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/
"""

from typing import List

class Robot:
    """
    This class creates a robot.
    The robot has a name, a battery level and a list of skills
    The robot can say its name and learn new skills
    Those actions cost battery

    Incorrect Use:

    First argument must be srt

        robot = Robot(20,100,["Walk","Run"])
        robot = Robot(["Robert"],100,["Walk","Run"])

    Second argument must be an int between 0 and 100

        robot = Robot("Robert","80",["Walk","Run"])
        robot = Robot("Robert",110,["Walk","Run"])
        robot = Robot("Robert",-80,["Walk","Run"])

    Third argument must be a list of str
    
        robot = Robot("Robert",100,("Walk","Run"))
        robot = Robot("Robert",100,{'a': "Walk",'b': "Run"})

    Correct use:

        robot = Robot("Robert",100,["Walk","Run"])
    """
    
    def __init__(self,name,battery: int=100,skills: List[str]=[]):
        if battery > 100 or battery < 0: 
            raise ValueError("Battery must be an integer between 0 and 100.")
        self.__name = name
        self.__battery = battery
        self.__skills = skills
        
    @property
    def name(self):
        return self.__name
      
    @property
    def battery(self):
        return self.__battery
      
    @property
    def skills(self):
        return self.__skills
    
    def carregar(self):
        self.__battery = 100
        
    def say_name(self):
        if self.__battery > 0:
            self.__battery -= 1
            return f'BEEP BEEP BOOP. I AM {self.__name.upper()}'
        return 'Battery is low. Please, recharge and try again.'
    
    def learn_skill(self,new_skill: str,cost: int):
        if self.battery >=cost:
            self.__battery -= cost
            self.__skills.append(new_skill)
            return f'WOW! I learned {new_skill.upper()}'
        return 'Battery is low. Please, recharge and try again.'