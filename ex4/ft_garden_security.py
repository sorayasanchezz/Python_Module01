#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 18:43:04 by soraya              #+#    #+#            #
#   Updated: 2026/02/25 16:37:59 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._heigth = 0
        self._age = 0
        print(f"Plant created: {self.name}")

    def get_heigth(self):
        print(f"{self._heigth}")

    def get_age(self):
        print(f"{self._age}")

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = new_age
        print(f"Age updated: {self._age} days [OK]")

    def describe(self):
        print(f"Current plant: {self.name} ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    # rose.set_age(-2)
    print()
    rose.describe()
