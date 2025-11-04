import random

class Agent:
    total_agents = 0
    def __init__(self, code_name):
        self.code_name = code_name
        self._clearance_level = 0
        Agent.total_agents += 1

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")

    def get_clearance_level(self):
        return self._clearance_level

    
    def set_clearance_level(self, clearance_level):
        if 1 <= clearance_level <=10:
            self._clearance_level = clearance_level
        else:
            return "Not Valid"

    @classmethod
    def get_total_agents(cls):
        print(f"Number of active agents: {cls.total_agents}")
    


class Mission:
    def __init__(self, mission_name: str, target_location: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent


    def brief(self):
        print(f"Mission: {self.mission_name}, Target {self.target_location}, Agent: {self.assigned_agent.code_name}")


agent1 = Agent("Yemot")
agent1.set_clearance_level(11)
agent1.report()
mission1 = Mission("mashiah", "rehovot", agent1)
mission1.brief()


class FieldAgent(Agent):
    def __init__(self, code_name, region):
        super().__init__(code_name)
        self.region = region

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level} region: {self.region}") 



# agent1 = FieldAgent("Yemot", "Israel")
# agent1.set_clearance_level(5)
# agent1.report()
# mission1 = Mission("mashiah", "rehovot", agent1)
# mission1.brief()



class CyberAgent(Agent):
    def __init__(self, code_name):
        super().__init__(code_name)
        CyberAgent.dpartment = "hacking"


    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level} Department: {CyberAgent.dpartment}") 
    

list_animals = [Agent("clickol"), FieldAgent("yemot", "rehovot"), CyberAgent("shmuel")]
for i in list_animals:
    i.set_clearance_level(random.randint(1,9))
    i.report()
    a = Mission(random.choice(["aaa", "bbb","ccc"]),random.choice(["bb", "jerusalem","usa"]), i)
    a.brief()

Agent.get_total_agents()

