a = 'sdfsdfdfsgjhdlfge[sssws12'
def element_search(a, num = None):
    if not num:
        num =  input('Enter the element: ')
    if num in a:
        print(f'{num} inside of list a')
    else:
        print(f"{num} is not element of list a")

element_search(a)
# if you did not entered the number, function will ask you element