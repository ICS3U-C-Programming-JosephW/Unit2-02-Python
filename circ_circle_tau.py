#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Feb. 28, 2025
"""
This program asks the user for the radius of a circle in cm.
It then calculates and displays the circumference using tau.
"""
import constants


def main():
    # Set tau.
    TAU = constants.TAU

    # Get the radius from the user.
    radius = float(input("Enter the radius of the circle in (cm): "))

    # Calculate the circumference.
    circumference = TAU * radius

    # Display the circumference.
    print(f"\nCircumference = {circumference} cm")


if __name__ == "__main__":
    main()
