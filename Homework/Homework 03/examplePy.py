class Sharps(object):
    """Create a sharp weapon"""
    def __init__(self, name, length, age, damage):
        """ Initialize name, age, and length damage attributes."""
        self.name = name
        self.age = age
        self.length = length
        self.damage = damage
    def do_damage(self, target):
        target = target - self.damage

class dagger(Sharps):
    """ makes a dagger"""
    def __init__(self, name, length, age, damage):
        """sets up a dagger"""
        super().__init__(self, name, length, age, damage)
        self.debuff = True

def dumper():
    print("json.dump all the good stuff")