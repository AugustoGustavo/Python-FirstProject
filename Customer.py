class Customer:
    def __init__(self):

        # starting protected vars
        self._name = None
        self._telephone = None

    # define the getter and setter method below
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_telephone(self):
        return self._telephone

    def set_telephone(self, telephone):
        self._telephone = telephone
