
class Container(object):
    """
    Acts as container for inserting things.
    """

    version = '0.1'


    def __init__(self, formatting=[], contents=None):
        """
        Construct a new 'Container' object.

        :param formatting: The formatting of the container
        :param contents: The contents of the container if void
        """
        self.formatting = formatting
        self.contents = contents
        
    def __repr__(self):
        """
        Represent the raw contents of the 'Container' object.
        """
        

    def __str__(self):
        """
        Represent the contents of the 'Container' class.
        """

##property file so that if formatting != None, then contents must be None

def testing():
    print([[1,1],[1,1,1]])






#testing()
