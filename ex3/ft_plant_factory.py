#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/23 18:43:15 by soraya              #+#    #+#            #
#   Updated: 2026/02/23 18:43:17 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age}) days")


if __name__ == "__main__":

    list_spec = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    final_list = []
    total_plants = 0

    """
    Loop that creates all the plants in list_specs, adds in new list with
    the append metod while printing and counting all plants created
    """

    print("=== Plant Factory Output ===")

    for i in list_spec:
        name, height, age = i
        tmp = Plant(name, height, age)
        final_list.append(tmp)
        tmp.print_info()
        total_plants += 1

    print()
    print(f"Total plants created: {total_plants}")
