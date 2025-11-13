import pytest
from order_manager import OrderManager

@pytest.fixture
def empty_order():
    return OrderManager([])

@pytest.fixture
def standard_order():
    items = [
        {'name': 'Apple', 'price': 100},
        {'name': 'Banana', 'price': 200},
        {'name': 'Orange', 'price': 150}
    ]
    return OrderManager(items)

@pytest.fixture
def single_item_order():
    return OrderManager([{'name': 'Book', 'price': 500}])



def test_total_empty(empty_order):
    assert empty_order.total() == 0

def test_total_standard(standard_order):
    assert standard_order.total() == 450

def test_total_single_item(single_item_order):
    assert single_item_order.total() == 500




def test_most_expensive_empty(empty_order):
    assert empty_order.most_expensive() is None

def test_most_expensive_standard(standard_order):
    expected = {'name': 'Banana', 'price': 200}
    assert standard_order.most_expensive() == expected

def test_most_expensive_single_item(single_item_order):
    expected = {'name': 'Book', 'price': 500}
    assert single_item_order.most_expensive() == expected




def test_apply_discount_valid_total(standard_order):
    standard_order.apply_discount(20) 
    assert standard_order.total() == pytest.approx(360)

def test_apply_discount_all_items_changed(standard_order):
    standard_order.apply_discount(10)
    
    expected_prices = {
        'Apple': 90.0,   
        'Banana': 180.0, 
        'Orange': 135.0  
    }
    
    for item in standard_order.items:
        assert item['price'] == pytest.approx(expected_prices[item['name']])




def test_apply_discount_invalid_zero(standard_order):
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        standard_order.apply_discount(0)

def test_apply_discount_invalid_negative(standard_order):
    with pytest.raises(ValueError):
        standard_order.apply_discount(-10)

def test_apply_discount_invalid_over_100(standard_order):
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        standard_order.apply_discount(101)




def test_repr_empty(empty_order):
    assert repr(empty_order) == "OrderManager(items=[])"

def test_repr_standard(standard_order):
    expected = "OrderManager(items=[Apple, Banana, Orange])"
    assert repr(standard_order) == expected