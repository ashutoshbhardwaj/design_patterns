import abc


class AHandler(abc.ABC):
    successor: None

    @abc.abstractmethod
    def set_successor(self, sucessor):
        pass

    @abc.abstractmethod
    def handle_request(self, request):
        pass


class Handler(AHandler):
    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        print("Inside Handler")
        if self.successor is not None:
            return self.successor.handle_request(request)
        else:
            return f"Request could not be handled by any handler"


class General(Handler):
    def handle_request(self, request):
        import pdb

        # pdb.set_trace()
        print("Inside General")
        print(request.type)
        if request.type == "general":
            print("Hi, This is chintu, I'll take care of your general adhoc request")
        else:
            super().handle_request(request)


class Plumber(Handler):
    def handle_request(self, request):
        print("Inside Plumber")
        print(request.type)
        if request.type == "plumbing":
            print("Hi, This is Sonu, I'll take care of your plumbing request")
        else:
            super().handle_request(request)


class Electrician(Handler):
    def handle_request(self, request):
        print("Inside Electician")
        print(request.type)
        if request.type == "wiring":
            print("Hi, This is Monu, I'll take care of your wiring request")
        else:
            super().handle_request(request)


class Request:
    def __init__(self, type) -> None:
        self.type = type


def main():
    import pdb

    # pdb.set_trace()
    # Create objects of Handlers
    handy_man = General()
    plumber = Plumber()
    electrician = Electrician()
    # Set the hierarchy of handlers
    handy_man.set_successor(plumber)
    plumber.set_successor(electrician)
    requests = [Request("plumbing"), Request("wiring"), Request("general")]
    for request in requests:
        handy_man.handle_request(request)


if __name__ == "__main__":
    main()
