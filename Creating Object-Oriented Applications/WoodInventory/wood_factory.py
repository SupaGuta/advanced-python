"""This module creates Plywood or Lumber subclass objects using a 
factory method defined in the Wood superclass."""

class Wood:
    """This class creates a subclass object using a factory method."""

    def factory(form):
        """Create Plywood or Lumber subclasses."""

        class Plywood(Wood):
            """This class displays plywood text."""

            def display(self):
                print("This is new plywood.")

        class Lumber(Wood):
            """This class displays lumber text."""

            def display(self):
                print("This is new lumber.")

        # Test the form attribute and run appropriate subclass.
        if (form == "Plywood"):
            return Plywood()
        elif (form == "Lumber"):
            return Lumber()

# Create plywood and lumber products.
plywood1 = Wood.factory("Plywood")
lumber1 = Wood.factory("Lumber")

plywood1.display()
lumber1.display()