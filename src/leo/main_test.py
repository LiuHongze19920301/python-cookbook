record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

*trailing, current = [10, 9, 8, 1, 2, 3, 5]
print(trailing)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *arg in records:
    if tag == 'foo':
        do_foo(*arg)
    else:
        do_bar(*arg)


# 递归实现
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
