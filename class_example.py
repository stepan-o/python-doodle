class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is {0}".format(self.name))


class Person:
    def __init__(self, name, personality, is_sitting, robot_owned):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = robot_owned

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

    def report_status(self):
        print("Hi, my name is {0} {1}, I own {2} and I am{3}sitting."
              .format(self.personality, self.name, self.robot_owned.name    , " " if self.is_sitting else " not "))


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
r1.introduce_self()
r2.introduce_self()

p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "talkative", True, r1)
p1.report_status()
p2.report_status()


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print("Data in the head node:", n1.data)
print("And after the next node is:", n1.next.next)
print("Its data is:", n1.next.next.data)


def count_nodes(head_node):
    count = 0
    node = head_node
    while node:
        count += 1
        node = node.next
    return count


print("{0} nodes in total in the linked list.".format(count_nodes(n1)))


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("n must be greater than 0.")
        return
    else:
        return n * factorial(n - 1)


n = 6
print("{0}! = {1}".format(n, factorial(n)))


def fibonacci(num_elements, n_cur, n_m1, n_m2, cur_elem, fib_seq):
    if cur_elem == num_elements:
        return fib_seq
    else:
        n_m2 = n_m1
        n_m1 = n_cur
        n_cur = n_m1 + n_m2
        fib_seq.append(n_cur)
        cur_elem += 1
        return fibonacci(num_elements, n_cur, n_m1, n_m2, cur_elem, fib_seq)


num_el = 5  # number of elements to return
n_min2 = 1
n_min1 = 2
n_1 = 3
sequence = [n_1]
i = 0  # current count of elements

print("{0} elements of Fibonacci suquence starting with {1}:\n{2}"
      .format(num_el, n_1, fibonacci(num_el, n_1, n_min1, n_min2, i, sequence)))
