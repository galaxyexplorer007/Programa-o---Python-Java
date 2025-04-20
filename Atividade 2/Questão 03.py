# 3. Sistema de Reservas de Eventos
import json
import os

class EventReservation:
    def __init__(self, filename='reservas.json', total_seats=20):
        self.filename = filename
        self.total_seats = total_seats
        self.seats = self.load_seats()

    def load_seats(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return [False] * self.total_seats

    def save_seats(self):
        with open(self.filename, 'w') as f:
            json.dump(self.seats, f, indent=4)

    def show_seats(self):
        print("Mapa de assentos:")
        for i, seat in enumerate(self.seats):
            print(f"{i+1}: {'Reservado' if seat else 'Livre'}")

    def reserve_seat(self, seat_number):
        if 0 < seat_number <= self.total_seats and not self.seats[seat_number-1]:
            self.seats[seat_number-1] = True
            self.save_seats()
            print("Reserva realizada com sucesso.")
        else:
            print("Assento inválido ou já reservado.")

    def cancel_reservation(self, seat_number):
        if 0 < seat_number <= self.total_seats and self.seats[seat_number-1]:
            self.seats[seat_number-1] = False
            self.save_seats()
            print("Reserva cancelada.")
        else:
            print("Assento inválido ou já está livre.")