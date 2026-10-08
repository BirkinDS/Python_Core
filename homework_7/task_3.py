# Создайте программу, имитирующую работу клиники. Создайте базовый класс Doctor с методом treat().
# От него создайте три дочерних класса: Surgeon, Dentist и Therapist.
# В каждом дочернем классе переопределите метод treat(), чтобы каждый врач выводил сообщение о своём способе лечения.
# Создайте класс Patient, содержащий атрибуты treatment_plan - код плана лечения и doctor - назначенный пациенту врач.
# В классе Therapist реализуйте метод назначения врача пациенту.
# Если код плана лечения равен 1, пациенту назначается хирург; если код равен 2 - дантист;
# при любом другом значении - терапевт. После назначения врача необходимо сохранить
# соответствующий объект врача в patient.doctor и вызвать у него метод treat().
# Создайте пациента, задайте ему план лечения и продемонстрируйте работу программы.

# solution
class Doctor:
    def treat(self):
        pass


class Surgeon(Doctor):
    def treat(self):
        print("Хирург проводит операцию")


class Dentist(Doctor):
    def treat(self):
        print("Дантист лечит зубы")


class Therapist(Doctor):
    def treat(self):
        print("Терапевт проводит первичный осмотр")

    def assigning(self, patient):
        if patient.treatment_plan == 1:
            print("Назначен хирург")
            patient.doctor = Surgeon()
        elif patient.treatment_plan == 2:
            print("Назначен дантист")
            patient.doctor = Dentist()
        else:
            print("Назначен терапевт")
            patient.doctor = Therapist()
        patient.doctor.treat()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan
        self.doctor = None


therapist = Therapist()

patient1 = Patient(treatment_plan=1)
therapist.assigning(patient1)
print()
patient2 = Patient(treatment_plan=2)
therapist.assigning(patient2)
print()
patient3 = Patient(treatment_plan=3)
therapist.assigning(patient3)
