class MultiInstanceObject:
    pass


"""class a:
    def __init__(self, main, secondary):
        self.main = main
        self.secondary = secondary
    
    def confirm_self(self):
        foo = MultiInstanceObject(self.main, self.secondary)

        main_variables = vars(self.main)
        secondary_variables = vars(self.secondary)

        main_functions = [func for func in dir(self.main) if callable(getattr(self.main, func)) and not func.startswith("__")]
        secondary_functions = [func for func in dir(self.secondary) if callable(getattr(self.secondary, func)) and not func.startswith("__")]
        
        my_variables_names = list(set(main_variables) | set(secondary_variables))
        my_functions_names = list(set(main_functions) | set(secondary_functions))

        my_variables = dict()
        my_functions = dict()

        for i in range(len(my_variables_names)):
            try:
                getattr(self.main, my_variables_names[i])
            except Exception:
                my_variables[my_variables_names[i]] = getattr(self.secondary, my_variables_names[i])
            else:
                my_variables[my_variables_names[i]] = getattr(self.main, my_variables_names[i])
        for i in range(len(my_functions_names)):
            try:
                getattr(self.main, my_functions_names[i])
            except Exception:
                my_functions[my_functions_names[i]] = getattr(self.secondary, my_functions_names[i])
            else:
                my_functions[my_functions_names[i]] = getattr(self.main, my_functions_names[i])

        for i in range(len(my_variables_names)):
            setattr(foo, str(my_variables_names[i]), my_variables[my_variables_names[i]])
        for i in range(len(my_functions_names)):
            setattr(foo, str(my_functions_names[i]), my_functions[my_functions_names[i]])

        return foo"""

def SetMultiInstanceByTwoObject(main, secondary):
    foo = MultiInstanceObject()

    main_variables = vars(main)
    secondary_variables = vars(secondary)

    main_functions = [func for func in dir(main) if callable(getattr(main, func)) and not func.startswith("__")]
    secondary_functions = [func for func in dir(secondary) if callable(getattr(secondary, func)) and not func.startswith("__")]
        
    my_variables_names = list(set(main_variables) | set(secondary_variables))
    my_functions_names = list(set(main_functions) | set(secondary_functions))

    my_variables = dict()
    my_functions = dict()

    for i in range(len(my_variables_names)):
        try:
            getattr(main, my_variables_names[i])
        except Exception:
            my_variables[my_variables_names[i]] = getattr(secondary, my_variables_names[i])
        else:
            my_variables[my_variables_names[i]] = getattr(main, my_variables_names[i])
    for i in range(len(my_functions_names)):
        try:
            getattr(main, my_functions_names[i])
        except Exception:
            my_functions[my_functions_names[i]] = getattr(secondary, my_functions_names[i])
        else:
            my_functions[my_functions_names[i]] = getattr(main, my_functions_names[i])

    for i in range(len(my_variables_names)):
        setattr(foo, str(my_variables_names[i]), my_variables[my_variables_names[i]])
    for i in range(len(my_functions_names)):
        setattr(foo, str(my_functions_names[i]), my_functions[my_functions_names[i]])

    return foo