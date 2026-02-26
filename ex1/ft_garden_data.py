#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 16:32:52 by soraya              #+#    #+#            #
#   Updated: 2026/02/23 18:43:25 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """Molde de planta, con nombre, altura y edad"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data():
    """Función que crea plantas y las muestra con sus características"""
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    for plant in plants:
        plant.print_info()


ft_garden_data()
