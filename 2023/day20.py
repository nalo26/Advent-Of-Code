file = open("input.txt")
lines = file.read().splitlines()


class Network:
    def __init__(self):
        self.modules = {}
        self.button = None
        self.queue: list[Signal] = []
        self.sended = [0, 0]

    def tick(self, watch: bool = False):
        output = self.get_module("rx")
        while self.queue:
            signal = self.queue.pop(0)
            if watch and signal.destination == output and not signal.state:
                return True
            signal.destination.receive(signal)
        return False

    def create_button(self) -> "Module":
        self.button = Button("button", self)
        self.button.add_destination(self.get_module("broadcaster"))
        return self.button

    def add_module(self, module: "Module"):
        self.modules[module.name] = module

    def get_module(self, name: str) -> "Module":
        module = self.modules.get(name)
        if module is None:
            module = Dummy(name, self)
            self.add_module(module)
        return module


class Signal:
    def __init__(self, state: bool, source: "Module", destination: "Module"):
        self.state = state
        self.source = source
        self.destination = destination


class Module:
    def __init__(self, name: str, network: Network):
        self.name = name
        self.network = network
        self.destinations = []

    def add_destination(self, destination: "Module"):
        self.destinations.append(destination)

    def receive(self, signal: Signal):
        pass

    def send(self, state: bool):
        for destination in self.destinations:
            signal = Signal(state, self, destination)
            self.network.sended[int(state)] += 1
            # print("%s -%s-> %s" % (self.name, "high" if state else "low", destination.name))
            self.network.queue.append(signal)


class FlipFlop(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = False

    def receive(self, signal: Signal):
        if not signal.state:
            self.state = not self.state
            self.send(self.state)


class Conjunction(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = {}

    def add_destination(self, destination: Module):
        super().add_destination(destination)

    def add_source(self, source: Module):
        self.memory[source] = False

    def receive(self, signal: Signal):
        self.memory[signal.source] = signal.state
        if all(self.memory.values()):
            self.send(False)
        else:
            self.send(True)


class Broadcast(Module):
    def receive(self, signal: Signal):
        self.send(signal.state)


class Button(Module):
    def press(self):
        self.send(False)
        return self.network.tick()


class Dummy(Module):
    def receive(self, signal: Signal):
        pass


def create_network():
    network = Network()
    for line in lines:  # creating modules
        name = line.split(" -> ")[0]
        if name == "broadcaster":
            module = Broadcast(name, network)
        symbol, name = name[0], name[1:]
        if symbol == "%":
            module = FlipFlop(name, network)
        if symbol == "&":
            module = Conjunction(name, network)
        network.add_module(module)

    for line in lines:  # connecting modules
        source, destinations = line.lstrip("%&").split(" -> ")
        source = network.get_module(source)
        for destination in destinations.split(", "):
            destination = network.get_module(destination)
            source.add_destination(destination)
            if isinstance(destination, Conjunction):
                destination.add_source(source)

    network.create_button()
    return network


def part1():
    network = create_network()
    for _ in range(1000):
        network.button.press()

    return network.sended[0] * network.sended[1]


def part2():  # too slow!
    network = create_network()
    counter = 0
    while True:
        rx_received = network.button.press()
        counter += 1
        if rx_received:
            break
    return counter


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
