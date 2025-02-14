import unittest
import coverage
import sys
import os

#required for some reason
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#wanted to put this in main but didnt work, code coverage would be 100% otherwise
from src.custom_list import CustomList
from src.custom_stack import CustomStack
from src.custom_queue import CustomQueue


cov = coverage.Coverage(
    omit=['*/tests.py', '*/*test*.py'],
    branch=True
)

#region CustomList
class TestCustomListInitialization(unittest.TestCase):
    def test_empty_initialization(self):
        custom_list = CustomList()
        self.assertEqual(custom_list.values, [])
    
    def test_value_initialization(self):
        initial_values = [1, 2, 3]
        custom_list = CustomList(initial_values)
        self.assertEqual(custom_list.values, initial_values)
    
    def test_empty_list_initialization(self):
        custom_list = CustomList([])
        self.assertEqual(custom_list.values, [])
    
    def test_single_value_initialization(self):
        custom_list = CustomList([1])
        self.assertEqual(custom_list.values, [1])
    
    def test_mixed_types_initialization(self):
        custom_list = CustomList([1, "string", 3.14, None, True])
        self.assertEqual(custom_list.values, [1, "string", 3.14, None, True])

class TestCustomListContains(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([1, "test", 3.14, None, True])

    def test_contains_integer(self):
        self.assertTrue(1 in self.custom_list) 

    def test_contains_non_existing_value(self):
        self.assertFalse("missing" in self.custom_list) 

    def test_contains_empty_list(self):
        empty_list = CustomList()
        self.assertFalse("anything" in empty_list)

class TestCustomListLength(unittest.TestCase):
    def test_empty_list_length(self):
        custom_list = CustomList()
        self.assertEqual(len(custom_list), 0)

    def test_populated_list_length(self):
        custom_list = CustomList([1, 2, 3, 4])
        self.assertEqual(len(custom_list), 4)

    def test_single_element_length(self):
        custom_list = CustomList([1])
        self.assertEqual(len(custom_list), 1)

class TestCustomListGet(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([1, "test", 3.14, None, True])
    
    def test_get_first_element(self):
        self.assertEqual(self.custom_list.get(0), 1)
    
    def test_get_middle_element(self):
        self.assertEqual(self.custom_list.get(2), 3.14)
    
    def test_get_last_element(self):
        self.assertEqual(self.custom_list.get(4), True)

    def test_get_negative_index(self):
        self.assertEqual(self.custom_list.get(-1), True)
        self.assertEqual(self.custom_list.get(-2), None)
    
    def test_get_invalid_positive_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.get(5)
    
    def test_get_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.get(-6)
    
    def test_get_from_empty_list(self):
        empty_list = CustomList()
        with self.assertRaises(IndexError):
            empty_list.get(0)

class TestCustomListDelete(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([1, "test", 3.14, None, True])
    
    def test_delete_first_element(self):
        self.custom_list.delete(0)
        self.assertEqual(self.custom_list.values, ["test", 3.14, None, True])
    
    def test_delete_middle_element(self):
        self.custom_list.delete(2)
        self.assertEqual(self.custom_list.values, [1, "test", None, True])
    
    def test_delete_last_element(self):
        self.custom_list.delete(-1)
        self.assertEqual(self.custom_list.values, [1, "test", 3.14, None])
    
    def test_delete_negative_index(self):
        self.custom_list.delete(-2)
        self.assertEqual(self.custom_list.values, [1, "test", 3.14, True])
    
    def test_delete_invalid_positive_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.delete(5)
    
    def test_delete_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.delete(-6)
    
    def test_delete_from_empty_list(self):
        empty_list = CustomList()
        with self.assertRaises(IndexError):
            empty_list.delete(0)
    
    def test_delete_all_elements(self):
        custom_list = CustomList([1])
        custom_list.delete(0)
        self.assertEqual(custom_list.values, [])

class TestCustomListInsert(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList([1, 2, 3])
    
    def test_insert_without_index(self):
        self.custom_list.insert("test")
        self.assertEqual(self.custom_list.values, [1, 2, 3, "test"])
    
    def test_insert_at_start(self):
        self.custom_list.insert("test", 0)
        self.assertEqual(self.custom_list.values, ["test", 1, 2, 3])
    
    def test_insert_at_middle(self):
        self.custom_list.insert("test", 1)
        self.assertEqual(self.custom_list.values, [1, "test", 2, 3])
    
    def test_insert_at_end(self):
        self.custom_list.insert("test", 3)
        self.assertEqual(self.custom_list.values, [1, 2, 3, "test"])
    
    def test_insert_with_negative_index(self):
        self.custom_list.insert("test", -1)
        self.assertEqual(self.custom_list.values, [1, 2, "test", 3])
    
    def test_insert_invalid_positive_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.insert("test", 4)
    
    def test_insert_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.custom_list.insert("test", -5)
#endregion

#region CustomStack
class TestCustomStackInitialization(unittest.TestCase):
    def test_empty_initialization(self):
        custom_stack = CustomStack()
        self.assertEqual(custom_stack.values, [])

class TestCustomStackPush(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()

    def test_push_single_item(self):
        self.custom_stack.push(10)
        self.assertEqual(self.custom_stack.values, [10])

    def test_push_multiple_items(self):
        self.custom_stack.push(10)
        self.custom_stack.push(20)
        self.assertEqual(self.custom_stack.values, [20, 10])

class TestCustomStackPop(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(1)

    def test_pop_single_item(self):
        self.custom_stack.pop()
        self.assertEqual(len(self.custom_stack.values), 0)

    def test_pop_from_empty_stack(self):
        empty_stack = CustomStack()
        with self.assertRaises(IndexError):
            empty_stack.pop()

class TestCustomStackPeek(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(10)
        self.custom_stack.push(20)

    def test_peek(self):
        self.assertEqual(self.custom_stack.peek(), 20)

    def test_peek_from_empty_stack(self):
        empty_stack = CustomStack()
        with self.assertRaises(IndexError):
            empty_stack.peek()

class TestCustomStackIsEmpty(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()

    def test_is_empty_on_empty_stack(self):
        self.assertTrue(self.custom_stack.is_empty())

    def test_is_empty_on_non_empty_stack(self):
        self.custom_stack.push(10)
        self.assertFalse(self.custom_stack.is_empty())

class TestCustomStackSize(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()

    def test_size_on_empty_stack(self):
        self.assertEqual(self.custom_stack.size(), 0)

    def test_size_on_non_empty_stack(self):
        self.custom_stack.push(10)
        self.custom_stack.push(20)
        self.assertEqual(self.custom_stack.size(), 2)

class TestCustomStackClear(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(10)
        self.custom_stack.push(20)

    def test_clear(self):
        self.custom_stack.clear()
        self.assertTrue(self.custom_stack.is_empty())

class TestCustomStackContains(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(10)
        self.custom_stack.push(20)

    def test_contains_existing_value(self):
        self.assertTrue(10 in self.custom_stack)

    def test_contains_non_existing_value(self):
        self.assertFalse(30 in self.custom_stack)

class TestCustomStackStr(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(10)
        self.custom_stack.push(20)

class TestCustomStackLen(unittest.TestCase):
    def setUp(self):
        self.custom_stack = CustomStack()
        self.custom_stack.push(10)
        self.custom_stack.push(20)

    def test_len(self):
        self.assertEqual(len(self.custom_stack), 2)

#endregion

#region CustomQueue
class TestCustomQueueInitialization(unittest.TestCase):
    def test_empty_initialization(self):
        custom_queue = CustomQueue()
        self.assertEqual(custom_queue.values, [])

class TestCustomQueueEnqueue(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()

    def test_enqueue_single_item(self):
        self.custom_queue.enqueue(10)
        self.assertEqual(self.custom_queue.values, [10])

    def test_enqueue_multiple_items(self):
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)
        self.assertEqual(self.custom_queue.values, [10, 20])

class TestCustomQueueDequeue(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

    def test_dequeue(self):
        self.assertEqual(self.custom_queue.dequeue(), 10)
        self.assertEqual(self.custom_queue.values, [20])

    def test_dequeue_from_empty_queue(self):
        empty_queue = CustomQueue()
        with self.assertRaises(IndexError):
            empty_queue.dequeue()

class TestCustomQueuePeek(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

    def test_peek(self):
        self.assertEqual(self.custom_queue.peek(), 10)

    def test_peek_from_empty_queue(self):
        empty_queue = CustomQueue()
        with self.assertRaises(IndexError):
            empty_queue.peek()

class TestCustomQueueIsEmpty(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()

    def test_is_empty_on_empty_queue(self):
        self.assertTrue(self.custom_queue.is_empty())

    def test_is_empty_on_non_empty_queue(self):
        self.custom_queue.enqueue(10)
        self.assertFalse(self.custom_queue.is_empty())

class TestCustomQueueSize(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()

    def test_size_on_empty_queue(self):
        self.assertEqual(self.custom_queue.size(), 0)

    def test_size_on_non_empty_queue(self):
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)
        self.assertEqual(self.custom_queue.size(), 2)

class TestCustomQueueClear(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

    def test_clear(self):
        self.custom_queue.clear()
        self.assertTrue(self.custom_queue.is_empty())

class TestCustomQueueContains(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

    def test_contains_existing_value(self):
        self.assertTrue(10 in self.custom_queue)

    def test_contains_non_existing_value(self):
        self.assertFalse(30 in self.custom_queue)

class TestCustomQueueStr(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

class TestCustomQueueLen(unittest.TestCase):
    def setUp(self):
        self.custom_queue = CustomQueue()
        self.custom_queue.enqueue(10)
        self.custom_queue.enqueue(20)

    def test_len(self):
        self.assertEqual(len(self.custom_queue), 2)
#endregion

if __name__ == '__main__':
    cov.start()

    unittest.main(exit=False)

    cov.stop()

    cov.save()

    print("\nCoverage Report:")
    cov.report()

    cov.html_report(directory='coverage_html')