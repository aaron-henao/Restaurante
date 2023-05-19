from restaurante.model.restaurante import Restaurante, Nomina


class ConsolaRestaurante:
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def mostrar_menu():
        print("==== Menú ====")
        print("1. Agregar mesero")
        print("2. Seleccionar día de descanso para cada mesero")
        print("3. Generar horarios")
        print("4. Calcular nómina")
        print("5. Salir")

    restaurante = Restaurante()
    nomina = Nomina(restaurante.meseros)

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del mesero: ")
            correo = input("Ingrese el correo del mesero: ")
            restaurante.agregar_mesero(nombre, correo)
            print("Mesero agregado con éxito.")
            print()

        elif opcion == "2":
            print("Seleccione el día de descanso para cada mesero:")
            for mesero in restaurante.meseros:
                while True:
                    dia_descanso = input(f"{mesero.nombre}: ")
                    if dia_descanso:
                        if dia_descanso not in dias_semana:
                            print("Día no válido. Por favor, seleccione un día de la semana.")
                        elif dia_descanso == "Lunes" or dia_descanso == "Martes" or dia_descanso == "Miércoles":
                            if mesero.dias_descanso < 3:
                                mesero.asignar_descanso_personalizado(dia_descanso)
                                break
                            else:
                                print("Ya se han asignado los descansos máximos para este día. "
                                      "Por favor, seleccione otro día.")
                        else:
                            if mesero.dias_descanso < 2:
                                mesero.asignar_descanso_personalizado(dia_descanso)
                                break
                            else:
                                print("Ya se han asignado los descansos máximos para este día. "
                                      "Por favor, seleccione otro día.")
                    else:
                        break

            print("Días de descanso personalizados asignados con éxito.")
            print()

        elif opcion == "3":
            if len(restaurante.meseros) < 8:
                print("Debe haber al menos 8 meseros registrados para generar horarios.")
            else:
                horarios_semana = restaurante.generar_horarios()

                for dia, horarios in horarios_semana.items():
                    print(dia)
                    for horario in horarios:
                        print(horario)
                    print()

                for mesero in restaurante.meseros:
                    print(f"{mesero.nombre} - Horas diarias: {mesero.horas_trabajadas}")
                print(f"Total de horas trabajadas en la semana: {restaurante.horas_trabajadas}")

                print("Horarios generados con éxito.")
                print()

        elif opcion == "4":
            salarios_meseros = nomina.calcular_salario()

            print("Salarios:")
            for mesero, salario in salarios_meseros.items():
                print(f"{mesero}: ${salario}")

            print("Nómina calculada con éxito.")
            print()

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            print()
