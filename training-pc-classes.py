## My own test class program

#######################################################################################################
#            Computer Inventory Details Program             #
#######################################################################################################


#######################################################################################################
#            Main Class             #
#######################################################################################################


class Computer:
	num_of_pcs = 0

	def __init__(self, num, make, model, hdd_size, hdd_type, ram_size, ram_type, os_brand, os_version, os_model,
			os_arch):
		self.num = num
		self.make = make
		self.model = model
		self.hdd_size = hdd_size
		self.hdd_type = hdd_type
		self.ram_size = ram_size
		self.ram_type = ram_type
		self.os_brand = os_brand
		self.os_version = os_version
		self.os_model = os_model
		self.os_arch = os_arch

		Computer.num_of_pcs += 1

	def specs(self):
		print("---------------------------------")
		print("Specifications of computer #", self.num)
		print("Make:   ", self.make, self.model)
		print("Storage:", self.hdd_size, "GB", self.hdd_type)
		print("RAM:    ", self.ram_size, "GB", self.ram_type)
		print("OS:     ", self.os_brand, self.os_version, self.os_model, self.os_arch, "bit")
		print("---------------------------------\n")
		return (" ")


#######################################################################################################
#            List of pc details and dictionary            #
#######################################################################################################


comp_1 = Computer(1, 'Lenovo', 'Tiny', 240, 'Solid State Drive', 8, 'DDR4', 'Windows', '10', 'Pro', '64')
comp_2 = Computer(2, 'Lenovo', 'Think Pad', 500, 'Hard Disk Drive', 4, 'DDR3', 'Windows', '7', 'Pro', '64')
comp_3 = Computer(3, 'HP', '800G1', 512, 'Solid State Drive', 16, 'DDR4', 'Windows', '10', 'Pro', '64')

comp_list = {"1": comp_1,
	"2": comp_2,
	'3': comp_3}

#######################################################################################################
#            Computer details             #
#######################################################################################################


print("Number of computers we have in inventory:", Computer.num_of_pcs)
print("To see a certain computer's specs, type in a number between 0 and", Computer.num_of_pcs)
print("To exit the program, type 'quit'\n")
print(" ")

#######################################################################################################
#            The While loop for viewing the specs of dictionary            #
#######################################################################################################


while True:

	ui = input("Enter the computer number: ")
	print("\n")

	if ui == "quit":
		break

	elif ui == "all":
		pass

	elif ui == "":
		print("Please enter a valid number.\n")
		print(" ")

	elif ui in comp_list:
		print(comp_list[ui].specs())

	else:
		print("We do not have " + ui + " computers. Try again.\n")
		print(" ")
