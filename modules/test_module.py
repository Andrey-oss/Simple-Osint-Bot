# Example module

def fcn(sth): # Test function for text reversing
    return sth[::-1]

# Outside function won't be displayed in the bot. Use it as helper function to do something 

class Test_module: # Name must contains CAPITALIZED NAME OF THE MODULE!
    def test_function(self, sth): # This function WILL BE DISPLAYED in the bot, because it available in class
        return f"You typed: {sth}\nReverse text: {fcn(sth)}" # Return the result of the function

    test_function.display_name = "Test" # Use this attribute for name displaying. If you don't put it, function won't be displayed
    test_function.display_markup = "Enter something for test module" # This attribute used fordisplaying text after running this function

    # Notice: function must have two attributes, else it won't work properly!
    # Also, attributes of the function shold be present after declaration of this fcn!  