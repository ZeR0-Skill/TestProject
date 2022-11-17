main = input().split()
n = int(main[0])
food_n = int(main[1])
tasks = int(main[2])


class Cell:
    def __init__(self, icon, is_food, is_snake):
        self.icon = icon
        self.is_food = is_food
        self.is_snake = is_snake


Field = [[Cell(None, False, False) for _ in range(n)] for _ in range(n)]


class Node:
    def __init__(self, x, y, icon, next, prev):
        self.x = x
        self.y = y
        self.x2 = x
        self.y2 = y
        self.icon = icon
        self.next = next
        self.prev = prev


class Snake:
    def __init__(self):
        self.head = Node(0, 0, '0', None, None)
        self.tail = self.head

    def next_step(self, step):
        if step == 'D':
            if Field[self.head.x + 1][self.head.y].is_food:
                self.new_head(Field[self.head.x + 1][self.head.y].icon, self.head.x + 1, self.head.y,)
            else:
                self.head.y2 = self.head.y
                self.head.x2 = self.head.x
                self.head.x += 1
                node = self.head.next
                while node:
                    node.x2 = node.x
                    node.y2 = node.y
                    node.x = node.prev.x2
                    node.y = node.prev.y2
                    node = node.next
        elif step == 'G':
            if Field[self.head.x - 1][self.head.y].is_food:
                self.new_head(Field[self.head.x - 1][self.head.y].icon, self.head.x - 1, self.head.y,)
            else:
                self.head.y2 = self.head.y
                self.head.x2 = self.head.x
                self.head.x -= 1
                node = self.head.next
                while node:
                    node.x2 = node.x
                    node.y2 = node.y
                    node.x = node.prev.x2
                    node.y = node.prev.y2
                    node = node.next
        elif step == 'P':
            if Field[self.head.x][self.head.y + 1].is_food:
                self.new_head(Field[self.head.x][self.head.y + 1].icon, self.head.x, self.head.y + 1,)
            else:
                self.head.y2 = self.head.y
                self.head.x2 = self.head.x
                self.head.y += 1
                node = self.head.next
                while node:
                    node.x2 = node.x
                    node.y2 = node.y
                    node.x = node.prev.x2
                    node.y = node.prev.y2
                    node = node.next
        elif step == 'L':
            if Field[self.head.x][self.head.y - 1].is_food:
                self.new_head(Field[self.head.x][self.head.y - 1].icon, self.head.x, self.head.y - 1,)
            else:
                self.head.y2 = self.head.y
                self.head.x2 = self.head.x
                self.head.y -= 1
                node = self.head.next
                while node:
                    node.x2 = node.x
                    node.y2 = node.y
                    node.x = node.prev.x2
                    node.y = node.prev.y2
                    node = node.next
        Field[self.tail.x2][self.tail.y2].icon = None
        Field[self.tail.x2][self.tail.y2].is_snake = False

    def new_head(self, icon, x, y):
        current_head = self.head
        Field[x][y].is_food = False
        self.head = Node(x, y, icon, current_head, None)
        self.head.next.prev = self.head

    def visualize_snake(self):
        node = self.head
        while node:
            Field[node.x][node.y].icon = node.icon
            Field[node.x][node.y].is_snake = True
            node = node.next


food = []

for i in range(food_n):
    food.append(input().split())

for i in food:
    Field[int(i[0])-1][int(i[1])-1].icon = int(i[2])
    Field[int(i[0])-1][int(i[1])-1].is_food = True

snake = Snake()
snake.visualize_snake()

for i in range(tasks):
    inp = input().split()
    if inp[0] == 'Z':
        if Field[int(inp[1])-1][int(inp[2])-1].is_snake:
            print(Field[int(inp[1])-1][int(inp[2])-1].icon)
        else:
            print('-1')
    else:
        snake.next_step(inp[0])
        snake.visualize_snake()
