import os

class File(object):
    """
    Interacts with a file
    """

    version = '0.2'

    
    def __init__(self, location):
        """
        Construct a new 'File' object.

        :param location: The location of the file
        """
        self.location = location

    def create_file(self, content=""):
        """
        Create a new file at the location.

        :param content: The content to populate the new file
        """
        if (self.exists()):
            raise IOError("A file at '{}' already exists.".format(self.location))
        with open(self.location, 'w') as f:
            f.write(content)

    def delete_file(self):
        """
        Delete the file at the location.
        """
        if (not self.exists()):
            raise IOError("File at '{}' does not exist.".format(self.location))
        os.remove(self.location)

    def read_all(self):
        """
        Get all the contents of the file.

        :return: The contents of the file
        """
        if (not self.exists()):
            raise IOError("File at '{}' does not exist.".format(self.location))
        with open(self.location, 'r') as f:
            return f.read()

    def add(self, content):
        """
        Add contents to the end of the file.

        :param content: The content to be appended
        """
        if (not self.exists()):
            raise IOError("File at '{}' does not exist.".format(self.location))
        with open(self.location, 'a') as f:
            f.write(content)

    def replace_all(self, content):
        """
        Replace all contents in the file.

        :param content: The new content
        """
        if (not self.exists()):
            raise IOError("File at '{}' does not exist.".format(self.location))
        with open(self.location, 'w') as f:
            f.write(content)

    def clear(self):
        """
        Clear all contents in file.
        """
        if (not self.exists()):
            raise IOError("File at '{}' does not exist.".format(self.location))
        with open(self.location, 'w') as _:
            pass

    def exists(self):
        """
        Check if file already exists.

        :return: Returns true if file exists, false otherwise
        """
        return os.path.isfile(self.location)


def testing():
    print("\n----------------\n")
    
    f2 = File("C:\\Users\\Michael Zhang\\Documents\\testing01.txt")
    f2.create_file()
    print("Before:\n{}".format(f2.read_all()))
    
    print("\n----------------\n")
    
    f2.add("First addition\n")
    f2.add("Second addition")
    print("After:\n{}".format(f2.read_all()))
    
    print("\n----------------\n")
    
    f2.delete_file()
    f2.create_file("New file contents from initializer")
    print("Contents of file:\n{}".format(f2.read_all()))
    
    print("\n----------------\n")
    
    f2.delete_file()
    print("File exists?:", f2.exists())
    
    print("\n----------------\n")



#testing()




        
