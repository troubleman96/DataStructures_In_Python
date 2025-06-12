class ArrayOperations:
    """
    A comprehensive implementation of fundamental array operations
    including traversal, insertion, deletion, and searching algorithms.
    """
    
    def __init__(self, capacity=10):
        """
        Initialize the array with a fixed capacity
        
        Args:
            capacity (int): Maximum size of the array
        """
        self.capacity = capacity
        self.data = [None] * capacity  # Initialize array with None values
        self.size = 0  # Current number of elements in array
    
    def display(self):
        """Display the current elements in the array"""
        if self.size == 0:
            print("Array is empty")
            return
        
        print("Array elements:", end=" [")
        for i in range(self.size):
            print(self.data[i], end="")
            if i < self.size - 1:
                print(", ", end="")
        print("]")
        print(f"Size: {self.size}/{self.capacity}")
    
    # ==================== 1. ARRAY TRAVERSAL ====================
    
    def traverse(self):
        """
        Array Traversal: Access and process each element sequentially
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        print("\n=== Array Traversal ===")
        
        if self.size == 0:
            print("Cannot traverse: Array is empty")
            return
        
        print("Traversing array elements:")
        for i in range(self.size):
            print(f"Index {i}: {self.data[i]}")
        
        # Example: Calculate sum during traversal
        total = 0
        for i in range(self.size):
            if isinstance(self.data[i], (int, float)):
                total += self.data[i]
        
        print(f"Sum of numeric elements: {total}")
    
    def traverse_with_condition(self, condition_func):
        """
        Traverse array with a specific condition
        
        Args:
            condition_func: A function that takes an element and returns True/False
        """
        print("\n=== Conditional Traversal ===")
        matching_elements = []
        
        for i in range(self.size):
            if condition_func(self.data[i]):
                matching_elements.append((i, self.data[i]))
        
        if matching_elements:
            print("Elements matching condition:")
            for index, value in matching_elements:
                print(f"Index {index}: {value}")
        else:
            print("No elements match the condition")
    
    # ==================== 2. INSERTION IN ARRAY ====================
    
    def insert_at_end(self, element):
        """
        Insert element at the end of array
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        Args:
            element: Element to be inserted
        """
        print(f"\n=== Inserting {element} at end ===")
        
        # Check if array is full
        if self.size >= self.capacity:
            print("Error: Array overflow! Cannot insert element.")
            return False
        
        # Insert element at the end
        self.data[self.size] = element
        self.size += 1
        
        print(f"Successfully inserted {element} at index {self.size - 1}")
        self.display()
        return True
    
    def insert_at_position(self, element, position):
        """
        Insert element at a specific position
        Time Complexity: O(n) - due to shifting elements
        Space Complexity: O(1)
        
        Args:
            element: Element to be inserted
            position: Index where element should be inserted
        """
        print(f"\n=== Inserting {element} at position {position} ===")
        
        # Validate position
        if position < 0 or position > self.size:
            print(f"Error: Invalid position {position}. Valid range: 0 to {self.size}")
            return False
        
        # Check if array is full
        if self.size >= self.capacity:
            print("Error: Array overflow! Cannot insert element.")
            return False
        
        # Shift elements to the right to make space
        print("Shifting elements to make space...")
        for i in range(self.size, position, -1):
            self.data[i] = self.data[i - 1]
            print(f"  Moved element {self.data[i]} from index {i-1} to {i}")
        
        # Insert the new element
        self.data[position] = element
        self.size += 1
        
        print(f"Successfully inserted {element} at position {position}")
        self.display()
        return True
    
    def insert_at_beginning(self, element):
        """
        Insert element at the beginning of array
        Time Complexity: O(n) - all elements need to be shifted
        """
        return self.insert_at_position(element, 0)
    
    # ==================== 3. DELETION IN ARRAY ====================
    
    def delete_at_position(self, position):
        """
        Delete element at a specific position
        Time Complexity: O(n) - due to shifting elements
        Space Complexity: O(1)
        
        Args:
            position: Index of element to be deleted
        """
        print(f"\n=== Deleting element at position {position} ===")
        
        # Validate position
        if position < 0 or position >= self.size:
            print(f"Error: Invalid position {position}. Valid range: 0 to {self.size - 1}")
            return None
        
        # Check if array is empty
        if self.size == 0:
            print("Error: Array underflow! Cannot delete from empty array.")
            return None
        
        # Store the element to be deleted
        deleted_element = self.data[position]
        print(f"Deleting element: {deleted_element}")
        
        # Shift elements to the left to fill the gap
        print("Shifting elements to fill the gap...")
        for i in range(position, self.size - 1):
            self.data[i] = self.data[i + 1]
            print(f"  Moved element {self.data[i]} from index {i+1} to {i}")
        
        # Clear the last element and decrease size
        self.data[self.size - 1] = None
        self.size -= 1
        
        print(f"Successfully deleted {deleted_element} from position {position}")
        self.display()
        return deleted_element
    
    def delete_at_beginning(self):
        """Delete element from the beginning of array"""
        return self.delete_at_position(0)
    
    def delete_at_end(self):
        """
        Delete element from the end of array
        Time Complexity: O(1)
        """
        if self.size == 0:
            print("Error: Cannot delete from empty array")
            return None
        
        deleted_element = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        
        print(f"\n=== Deleted {deleted_element} from end ===")
        self.display()
        return deleted_element
    
    def delete_by_value(self, value):
        """
        Delete the first occurrence of a specific value
        Time Complexity: O(n)
        
        Args:
            value: Value to be deleted
        """
        print(f"\n=== Deleting first occurrence of {value} ===")
        
        # First, find the element
        position = self.linear_search(value, display_result=False)
        
        if position != -1:
            return self.delete_at_position(position)
        else:
            print(f"Element {value} not found in array")
            return None
    
    # ==================== 4. SEARCHING IN ARRAY ====================
    
    def linear_search(self, target, display_result=True):
        """
        Linear Search: Search for an element sequentially
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            target: Element to search for
            display_result: Whether to print search results
            
        Returns:
            int: Index of element if found, -1 if not found
        """
        if display_result:
            print(f"\n=== Linear Search for {target} ===")
        
        # Check each element sequentially
        for i in range(self.size):
            if display_result:
                print(f"Checking index {i}: {self.data[i]}")
            
            if self.data[i] == target:
                if display_result:
                    print(f"✓ Found {target} at index {i}")
                return i
        
        if display_result:
            print(f"✗ Element {target} not found in array")
        return -1
    
    def linear_search_all_occurrences(self, target):
        """
        Find all occurrences of a target element
        Time Complexity: O(n)
        
        Args:
            target: Element to search for
            
        Returns:
            list: List of indices where element is found
        """
        print(f"\n=== Finding all occurrences of {target} ===")
        
        indices = []
        for i in range(self.size):
            if self.data[i] == target:
                indices.append(i)
        
        if indices:
            print(f"Found {target} at indices: {indices}")
        else:
            print(f"Element {target} not found in array")
        
        return indices
    
    def binary_search(self, target, is_sorted=False):
        """
        Binary Search: Efficient search for sorted arrays
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            target: Element to search for
            is_sorted: Whether the array is already sorted
            
        Returns:
            int: Index of element if found, -1 if not found
        """
        print(f"\n=== Binary Search for {target} ===")
        
        # Create a copy for sorting if needed
        if not is_sorted:
            print("Array is not sorted. Creating sorted copy for binary search...")
            # Create index-value pairs to track original positions
            indexed_data = [(self.data[i], i) for i in range(self.size)]
            indexed_data.sort(key=lambda x: x[0])
            
            # Extract sorted values for binary search
            sorted_values = [item[0] for item in indexed_data]
            original_indices = [item[1] for item in indexed_data]
        else:
            sorted_values = [self.data[i] for i in range(self.size)]
            original_indices = list(range(self.size))
        
        print(f"Searching in sorted array: {sorted_values}")
        
        left = 0
        right = self.size - 1
        steps = 0
        
        while left <= right:
            steps += 1
            mid = (left + right) // 2
            mid_value = sorted_values[mid]
            
            print(f"Step {steps}: Checking middle index {mid}, value = {mid_value}")
            print(f"  Search range: indices {left} to {right}")
            
            if mid_value == target:
                original_index = original_indices[mid]
                print(f"✓ Found {target} at original index {original_index} (after {steps} steps)")
                return original_index
            elif mid_value < target:
                print(f"  {mid_value} < {target}, searching right half")
                left = mid + 1
            else:
                print(f"  {mid_value} > {target}, searching left half")
                right = mid - 1
        
        print(f"✗ Element {target} not found (after {steps} steps)")
        return -1
    
    def search_with_criteria(self, criteria_func):
        """
        Search elements based on custom criteria
        
        Args:
            criteria_func: Function that takes an element and returns True/False
        """
        print(f"\n=== Custom Criteria Search ===")
        
        matching_elements = []
        for i in range(self.size):
            if criteria_func(self.data[i]):
                matching_elements.append((i, self.data[i]))
        
        if matching_elements:
            print("Elements matching criteria:")
            for index, value in matching_elements:
                print(f"Index {index}: {value}")
        else:
            print("No elements match the criteria")
        
        return matching_elements


# ==================== DEMONSTRATION ====================

def demonstrate_array_operations():
    """Demonstrate all array operations with examples"""
    
    print("=" * 60)
    print("ARRAY OPERATIONS DEMONSTRATION")
    print("=" * 60)
    
    # Create an array
    arr = ArrayOperations(capacity=8)
    
    # 1. INSERTION OPERATIONS
    print("\n" + "=" * 40)
    print("1. INSERTION OPERATIONS")
    print("=" * 40)
    
    # Insert at end
    arr.insert_at_end(10)
    arr.insert_at_end(20)
    arr.insert_at_end(30)
    arr.insert_at_end(40)
    
    # Insert at specific position
    arr.insert_at_position(15, 1)  # Insert 15 at index 1
    arr.insert_at_position(5, 0)   # Insert 5 at beginning
    
    # 2. TRAVERSAL OPERATIONS
    print("\n" + "=" * 40)
    print("2. TRAVERSAL OPERATIONS")
    print("=" * 40)
    
    arr.traverse()
    
    # Conditional traversal
    arr.traverse_with_condition(lambda x: x > 20)  # Find elements > 20
    
    # 3. SEARCHING OPERATIONS
    print("\n" + "=" * 40)
    print("3. SEARCHING OPERATIONS")
    print("=" * 40)
    
    # Linear search
    arr.linear_search(20)
    arr.linear_search(100)  # Not found
    
    # Add duplicate for demonstration
    arr.insert_at_end(20)
    arr.linear_search_all_occurrences(20)
    
    # Binary search
    arr.binary_search(30)
    
    # Custom criteria search
    arr.search_with_criteria(lambda x: x % 10 == 0)  # Find multiples of 10
    
    # 4. DELETION OPERATIONS
    print("\n" + "=" * 40)
    print("4. DELETION OPERATIONS")
    print("=" * 40)
    
    # Delete at specific positions
    arr.delete_at_position(2)
    arr.delete_at_beginning()
    arr.delete_at_end()
    
    # Delete by value
    arr.delete_by_value(20)
    
    # Final state
    print("\n" + "=" * 40)
    print("FINAL ARRAY STATE")
    print("=" * 40)
    arr.display()


# Run the demonstration
if __name__ == "__main__":
    demonstrate_array_operations()