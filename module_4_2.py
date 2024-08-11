def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
#inner_function() # inner_function находится в объемлющей области видимости test_function и не может быть вызвана