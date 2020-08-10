# Class to create new node
class Node:
	def __init__(self, data):		
		self.data = data
		self.next = None

# Class to create a linked list
class LinkedList:
	def __init__(self):		
		self.head = None
	
	# Method to insert element in the begining of the list
	def insert_begining(self, value):		
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		print('List Insertion Success')
		return
	
	# Method to insert element after the specified number of nodes in the list
	def insert_after(self, prev, value):
		if self.head is None:
			print('You cannot insert at any intermediate position at an empty list')
			return
		new_node = Node(value)
		temp = self.head
		for i in range(1, prev):
			temp = temp.next
		new_node.next = temp.next
		temp.next = new_node
		print('List Insertion Success')
		return
	
	# Method to insert element at the last of the list
	def insert_last(self, value):
		if self.head is None:
			print('You cannot insert at the last of an empty list')
			return
		new_node = Node(value)
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
		print('List Insertion Success')
		return
	
	# Method to delete a specific element from the list
	def delete_key(self, key):
		if self.head is None:
			print('You cannot delete any key from an empty list')
			return
		temp = self.head
		
		# If element is at the starting of the list
		if temp.data == key:
			self.head = temp.next
			del temp.data
			temp.next = None
			print('Key Deletion Success')
			return
			
		# If element is at any postion in the list except starting OR If the element is not present in the list
		while temp:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next
		else:
			print('Key is not present inside the list')
			return
		prev.next = temp.next
		del temp.data
		temp.next = None
		print('Key Deletion Success')
		return
		
	# Method to delete entire linked list
	def delete_entire_list(self):
		if self.head is None:
			print('List is already empty')
			return
		temp = self.head
		while temp:
			prev = temp.next
			del temp.data
			temp = prev
		self.head = None
		print('Deletion of all keys success')
		return
		
	# Method to count number of nodes in the list	
	def count(self):
		elements = 0
		if self.head is None:
			print(f'List has {elements} elements')
			return
		temp =self.head
		while temp:
			elements += 1
			temp =temp.next
		print(f'List has {elements} elements')
		return
	
	# Method to reverse the nodes of the list
	def reverse(self):
		if self.head is None:
			print('You cannot reverse an empty list')
			return
		prev_node = None
		current_node = self.head
		next_node = None
		while current_node:
			next_node = current_node.next
			current_node.next = prev_node
			prev_node = current_node
			current_node = next_node
		self.head = prev_node
		print('List reversal success')
		return
		
	# Method to traverse the list
	def traverse(self):
		if self.head is None:
			print('List is Empty')
			return
		temp = self.head
		while temp:
			print(f'Key : {temp.data}')
			temp = temp.next
		print('List Traversal Success')
		return
		
	def convert_to_circular(self):
		if self.head is None:
			print('List is Empty')
			return
		temp = self.head		
		while self.head.next is not None:
			self.head = self.head.next
		self.head.next = temp
		print('Converted to circular list')
		return
		
# Main Function
if __name__ == '__main__':
	
	list = LinkedList()
	print('''Press 1 for insert_begining(value)
Press 2 for insert_after(prev, value)
Press 3 for insert_last(value)
Press 4 for delete_key(key)
Press 5 for delete_entire_list()
Press 6 for count()
Press 7 for reverse()
Press 8 for traverse()
Press 9 for convert_to_circular()
Press 10 for exit''')
	while True:
		choice = int(input('Enter Your Choice : '))
		if choice == 1:
			data = input('Enter Value : ')
			list.insert_begining(data)			
		elif choice == 2:
			prev = int(input('Enter the node number after which you want to insert new node : '))
			data = input('Enter Value : ')
			list.insert_after(prev, data)			
		elif choice == 3:			
			data = input('Enter Value : ')
			list.insert_last(data)			
		elif choice == 4:
			key = input('Enter Key to be deleted : ')
			list.delete_key(key)
		elif choice == 5:			
			list.delete_entire_list()			
		elif choice == 6:			
			list.count()
		elif choice == 7:
			list.reverse()
		elif choice == 8:
			list.traverse()
		elif choice == 9:
			list.convert_to_circular()
		elif choice == 10:
			break
		else:
			print('Invalid Choice')