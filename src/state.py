def can_deliver(method):
    def inner(ref):
        if ref.count_of_balls == 0:
            ref.current_state = ref.machine_empty_state_object
            print("Machine is Empty")
        else:
            method(ref)

    return inner


class GumBallMachine:
    def __init__(self, count_of_balls) -> None:
        self.count_of_balls = count_of_balls
        self.no_quarter_state_object = No_Quarter(self)
        self.has_quarter_state_object = Has_Quarter(self)
        self.machine_empty_state_object = Machine_Empty(self)
        self.current_state = self.no_quarter_state_object

    def __str__(self) -> str:
        return f"GumBallMachine({self.count_of_balls})"

    @can_deliver
    def put_quarter(self):
        self.current_state.put_quarter()

    @can_deliver
    def turn_crank(self):
        self.current_state.turn_crank()


class No_Quarter:
    def __init__(self, cntx):
        self.cntx = cntx

    def put_quarter(self):
        print("Entering Quarter into the machine and now processing")
        self.cntx.current_state = self.cntx.has_quarter_state_object

    def turn_crank(self):
        print("Mate you need to first enter qurter!!")


class Has_Quarter:
    def __init__(self, cntx):
        self.cntx = cntx

    def put_quarter(self):
        return "Machine has already a quarter. Please turn the crank"

    def turn_crank(self):
        print("Delivering the candy, please lookout for it in the shaft")
        self.cntx.count_of_balls -= 1
        # Here is the trick happening. you are changing the state. The new state's behaviour(methods) works differently.
        self.cntx.current_state = self.cntx.no_quarter_state_object


class Machine_Empty:
    def __init__(self, cntx):
        self.cntx = cntx

    def put_quarter(self):
        return "Machine is empty. Returning the qurter"

    def turn_crank(self):
        print("Delivering the candy, please lookout for it in the shaft")
        self.cntx.count_of_balls -= 1
        # Here is the trick happening. you are changing the state. The new state's behaviour(methods) works differently.
        self.cntx.current_state = self.cntx.no_quarter_state_object


# I want Gumball to behave like this

gmachine = GumBallMachine(1)
print(gmachine)
gmachine.put_quarter()  # This will update the state of Gumball
print(gmachine)
gumball = gmachine.turn_crank()  # This should return the Gumball object
print(gmachine)
gumball = gmachine.turn_crank()  # This should return none.
print(gmachine)
gumball = gmachine.turn_crank()  # This should return none.
print(gmachine)
gumball = gmachine.turn_crank()  # This should return none.
print(gmachine)
