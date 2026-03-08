from queue import PriorityQueue

class Customer:
    def __init__(self, id, name, priority, arrival_time, finish_time=0):
        self.id = id
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time
        self.finish_time = finish_time

    def __repr__(self):
        return f'Customer({self.id}, {self.name}, {self.priority}, {self.arrival_time}, {self.finish_time})'


class Store:
    def __init__(self, name):
        self.name = name
        self.queue = PriorityQueue()
        self.served_customers = []
        self.num_served = 0

    def __repr__(self):
        return f'Store({self.name}, Queue Size: {self.queue.qsize()}, Served: {self.num_served})'

    def add_customer(self, customer):
        self.queue.put((customer.priority, customer.arrival_time, customer))

    def serve_customer(self):
        if not self.queue.empty():
            _, _, customer = self.queue.get()
            self.served_customers.append(customer)
            self.num_served += 1
            return customer
        return None

    def find_customer(self, id):
        for priority, arrival_time, customer in list(self.queue.queue):
            if customer.id == id:
                return customer
        for customer in self.served_customers:
            if customer.id == id:
                return customer
        print("Customer not found")
        return None

    def promote_customer(self, id):
        temp_queue = PriorityQueue()
        found = False
        while not self.queue.empty():
            priority, arrival_time, customer = self.queue.get()
            if customer.id == id:
                if customer.priority < 3:
                    customer.priority += 1
                    found = True
                else:
                    print("Customer already at highest priority")
            temp_queue.put((customer.priority, customer.arrival_time, customer))
        self.queue = temp_queue
        if not found:
            print("Customer not found")

    def export_queue(self):
        return [customer for _, _, customer in list(self.queue.queue)]

    def export_history(self):
        return self.served_customers


