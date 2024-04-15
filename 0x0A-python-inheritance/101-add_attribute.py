#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name (str): The name of the attribute to add.
        attr_value: The value of the attribute to assign.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)

# Test the implementation
if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)  # Output: John

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] can't add new attribute
