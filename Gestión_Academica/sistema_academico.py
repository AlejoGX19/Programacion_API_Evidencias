import mysql.connector

class GestorSistema:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='gestion_academica'
            )
            self.cursor = self.conn.cursor()
            print("Conexión a la base de datos MySQL exitosa.")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            self.conn = None
            self.cursor = None

    def registrar_estudiante(self, nombre_completo, correo_electronico):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("INSERT INTO estudiantes (nombre_completo, correo_electronico) VALUES (%s, %s)", (nombre_completo, correo_electronico))
            self.conn.commit()
            print(f"Estudiante '{nombre_completo}' registrado con ID: {self.cursor.lastrowid}")
        except mysql.connector.Error as err:
            print(f"Error al registrar estudiante: {err}")
            self.conn.rollback()

    def registrar_curso(self, nombre_curso, descripcion, cantidad_creditos):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("INSERT INTO cursos (nombre_curso, descripcion, cantidad_creditos) VALUES (%s, %s, %s)", (nombre_curso, descripcion, cantidad_creditos))
            self.conn.commit()
            print(f"Curso '{nombre_curso}' registrado con ID: {self.cursor.lastrowid}")
        except mysql.connector.Error as err:
            print(f"Error al registrar curso: {err}")
            self.conn.rollback()

    def inscribir_estudiante_en_curso(self, id_estudiante, id_curso):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            if not self._existe_estudiante(id_estudiante):
                print(f"Error: No existe estudiante con ID {id_estudiante}.")
                return
            if not self._existe_curso(id_curso):
                print(f"Error: No existe curso con ID {id_curso}.")
                return

            self.cursor.execute("INSERT INTO inscripciones (id_estudiante, id_curso) VALUES (%s, %s)", (id_estudiante, id_curso))
            self.conn.commit()
            print(f"Estudiante con ID {id_estudiante} inscrito en el curso con ID {id_curso}.")
        except mysql.connector.Error as err:
            print(f"Error al inscribir estudiante en curso: {err}")
            self.conn.rollback()

    def _existe_estudiante(self, id_estudiante):
        if self.conn is None:
            return False
        self.cursor.execute("SELECT 1 FROM estudiantes WHERE id_estudiante = %s", (id_estudiante,))
        return self.cursor.fetchone() is not None

    def _existe_curso(self, id_curso):
        if self.conn is None:
            return False
        self.cursor.execute("SELECT 1 FROM cursos WHERE id_curso = %s", (id_curso,))
        return self.cursor.fetchone() is not None

    def listar_cursos_de_estudiante(self, id_estudiante):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("""
                SELECT c.id_curso, c.nombre_curso, c.descripcion, c.cantidad_creditos
                FROM inscripciones i
                JOIN cursos c ON i.id_curso = c.id_curso
                WHERE i.id_estudiante = %s
            """, (id_estudiante,))
            cursos_inscritos = self.cursor.fetchall()
            if cursos_inscritos:
                print(f"\nCursos del estudiante con ID {id_estudiante}:")
                for curso in cursos_inscritos:
                    print(f"  ID: {curso[0]}, Nombre: {curso[1]}, Descripción: {curso[2]}, Créditos: {curso[3]}")
            else:
                print(f"El estudiante con ID {id_estudiante} no está inscrito en ningún curso.")
        except mysql.connector.Error as err:
            print(f"Error al listar cursos del estudiante: {err}")

    def eliminar_inscripcion(self, id_estudiante, id_curso):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("DELETE FROM inscripciones WHERE id_estudiante = %s AND id_curso = %s", (id_estudiante, id_curso))
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print(f"Inscripción del estudiante con ID {id_estudiante} en el curso con ID {id_curso} eliminada.")
            else:
                print(f"No se encontró inscripción del estudiante con ID {id_estudiante} en el curso con ID {id_curso}.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar inscripción: {err}")
            self.conn.rollback()

    def listar_estudiantes(self):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("SELECT id_estudiante, nombre_completo, correo_electronico FROM estudiantes")
            estudiantes = self.cursor.fetchall()
            if estudiantes:
                print("\n--- Lista de Estudiantes ---")
                for estudiante in estudiantes:
                    print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Correo: {estudiante[2]}")
            else:
                print("No hay estudiantes registrados.")
        except mysql.connector.Error as err:
            print(f"Error al listar estudiantes: {err}")

    def listar_cursos(self):
        if self.conn is None:
            print("No hay conexión a la base de datos.")
            return
        try:
            self.cursor.execute("SELECT id_curso, nombre_curso, descripcion, cantidad_creditos FROM cursos")
            cursos = self.cursor.fetchall()
            if cursos:
                print("\n--- Lista de Cursos ---")
                for curso in cursos:
                    print(f"ID: {curso[0]}, Nombre: {curso[1]}, Descripción: {curso[2]}, Créditos: {curso[3]}")
            else:
                print("No hay cursos registrados.")
        except mysql.connector.Error as err:
            print(f"Error al listar cursos: {err}")

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos MySQL cerrada.")
        else:
            print("No hay conexión a la base de datos para cerrar.")

def menu():
    # Reemplaza con tus credenciales de MySQL
    db_host = "localhost"  
    db_user = "root"      
    db_password = ""       
    db_name = "gestion_academica" 

    gestor = GestorSistema(host=db_host, user=db_user, password=db_password, database=db_name)

    while True:
        print("\n--- Sistema de Gestión de Estudiantes y Cursos (MySQL) ---")
        print("1. Registrar estudiante")
        print("2. Registrar curso")
        print("3. Inscribir estudiante en curso")
        print("4. Listar cursos de un estudiante")
        print("5. Eliminar inscripción")
        print("6. Listar todos los estudiantes")
        print("7. Listar todos los cursos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre completo del estudiante: ")
            correo = input("Ingrese el correo electrónico del estudiante: ")
            gestor.registrar_estudiante(nombre, correo)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del curso: ")
            descripcion = input("Ingrese la descripción del curso: ")
            try:
                creditos = int(input("Ingrese la cantidad de créditos del curso: "))
                gestor.registrar_curso(nombre, descripcion, creditos)
            except ValueError:
                print("Por favor, ingrese un número válido para los créditos.")
        elif opcion == '3':
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante a inscribir: "))
                id_curso = int(input("Ingrese el ID del curso en el que inscribir: "))
                gestor.inscribir_estudiante_en_curso(id_estudiante, id_curso)
            except ValueError:
                print("Por favor, ingrese IDs numéricos válidos.")
        elif opcion == '4':
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante para listar sus cursos: "))
                gestor.listar_cursos_de_estudiante(id_estudiante)
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")
        elif opcion == '5':
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante para eliminar la inscripción: "))
                id_curso = int(input("Ingrese el ID del curso para eliminar la inscripción: "))
                gestor.eliminar_inscripcion(id_estudiante, id_curso)
            except ValueError:
                print("Por favor, ingrese IDs numéricos válidos.")
        elif opcion == '6':
            gestor.listar_estudiantes()
        elif opcion == '7':
            gestor.listar_cursos()
        elif opcion == '8':
            gestor.close()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()