import matplotlib.pyplot as pl
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import random

# GRAPH MAKER
print("Version 2.3.5")
BarMode = int(input("Bar Mode?(1 = Yes, 0 = No): "))
pl.figure(figsize=(25, 25))


def Start():
    Data = []
    AD = int(input("What mode? (0 = Manual, 1 = Multiply ,2 = random mode, 3 = Changelog, 4 = Experimental 3D "
                   "feature, 5 = Advanced manual mode): "))
    X = []
    # MANUAL
    if AD == 0:
        b = int(input("How many data do you have? (ex. Answer = 2, You have 2 Data inputs!): "))
        pl.ylabel(input("Label for Y axis | (Ex. Money): "))
        pl.xlabel(input("Label for X axis - (Ex. Years): "))

        for c in range(b):
            Data.append(int(input(f'Data nr. {c + 1} is number: ')))
        if BarMode == 1:
            for c in range(b):
                X.append((input(f'Info nr. {c + 1} is: ')))

        for _ in Data:
            if BarMode == 0:
                pl.plot(Data)
            if BarMode == 1:
                pl.bar(X, Data)
        pl.show()
        Start()
    # MULTIPLY
    if AD == 1:
        b = int(input("How many data do you have? (smoothness, Do not put more than 40) : "))
        pl.ylabel(input("Label for Y axis | (Ex. Money): "))
        pl.xlabel(input("Label for X axis - (Ex. Years): "))
        First_Number = int(input("First number in data?: "))
        Number = float(
            input("Number to multiply(Every time the next number comes, basically intensity, put it lower for "
                  "there to be a hill, not a spike, How to use: Type 1.05 or another): "))
        Number1 = First_Number
        for c in range(b):
            Data.append(Number1)
            Number1 = Number * Number
        if BarMode == 1:
            for c in range(b):
                X.append((input(f'Info nr. {c + 1} is: ')))
        for _ in Data:
            if BarMode == 0:
                pl.plot(Data)
            if BarMode == 1:
                pl.bar(X, Data)
        pl.show()
        Start()
    # RANDOM MODE
    if AD == 2:
        b = int(input("How many data do you have? (ex. Answer = 2, There are 2 responses): "))
        pl.ylabel(input("Label for Y axis | (Ex. Money): "))
        pl.xlabel(input("Label for X axis - (Ex. Years): "))
        Random = input("From 0 to (Smoothness): ")
        for c in range(b):
            Data.append(random.randint(0, int(Random)))
        if BarMode == 1:
            for c in range(b):
                X.append((input(f'Info nr. {c + 1} is: ')))
        for _ in Data:
            if BarMode == 0:
                pl.plot(Data)
            if BarMode == 1:
                pl.bar(X, Data)
        pl.show()
        Start()
    # CHANGELOG
    if AD == 3:
        print("  ChangeLog:")
        print("Version 2.4.5")
        print("  Added Advanced manual mode! Now you can break graphs!")
        print("  Fixed the Changelog showing version 2.3.5 as 2.2.5!")
        print("Version 2.3.5")
        print("  Added Experimental 3D Feature(Took a lot of tinkering, ~2 hours)")
        print("  Made program repeat after you finished doing a graph")
        print("First Version with NO bugs, and i am talking about typing wrong too! (Like any other but joined "
              "together)")
        print("Version 2.0.0")
        print("  Fixed 'No' mode doing nothing")
        print("  Renamed 'No' mode to Manual")
        print("  Added Bar chart mode!(Took a lot to implement ~45 min)")
        print("  Bar chart information!(Took a lot to implement ~30 min)")
        print("Version 1.7.0")
        print("  Added ChangeLog")
        print("  Revamped some text")
        print("  1 Bug Fix")
        print("Version 1.6.5")
        print("  Added Random Mode")
        print("Version 1.5.0")
        print("  Added Multiplication mode")
        print('  Fixed "Tkinter" problem')
        print('  Added modes')
        print("Version 1.0.0")
        print("  Added Graph making")
        print("  Added Labels")
        print("  Added Data number selection")
        Start()
    # 3D FEATURE
    if AD == 4:
        fig, ax = pl.subplots(subplot_kw={"projection": "3d"})

        # Make data.
        X = np.arange(-5, 5, 0.1)
        Y = np.arange(-5, 5, 0.1)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        AA = Z = input("What do you want?(0 Black hole, 1 Collapsing shape")
        if AA == 0:
            Z = np.log(R)
        if AA == 1:
            Z = np.sin(R)

        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        pl.show()
        Start()  #
    # ADVANCED MANUAL
    if AD == 5:
        X = []
        b = int(input("How many data do you have? (ex. Answer = 2, You have 2 Data inputs!): "))
        pl.ylabel(input("Label for Y axis | (Ex. Money): "))
        pl.xlabel(input("Label for X axis - (Ex. Years): "))

        for c in range(b):
            Data.append(int(input(f'X Data nr. {c + 1} is number: ')))
        for c in range(b):
            X.append(int(input(f'Y Data nr. {c + 1} is number: ')))
        if BarMode == 1:
            for c in range(b):
                X.append((input(f'Info nr. {c + 1} is: ')))

        for _ in Data:
            if BarMode == 0:
                pl.plot(Data, X)
            if BarMode == 1:
                pl.bar(X, Data)
        pl.show()
        Start()


Start()
