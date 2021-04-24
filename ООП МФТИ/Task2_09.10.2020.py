class Vector:
    _matrica = []
    _len_mat = 0
    
    @classmethod
    def print_matrica(cls):
        return cls._matrica

    def __init__(self, str, x = 0, y = 0, z = 0):
        buff = list(str.split(','))
        dict1 = [x, y, z]
        try:
            for i in range(len(buff)):
                dict1[i] = buff[i]
        except IndexError:
            print('Введены лишние параметры. Мы работаем максимум в 3D.')

        try:
            self.__x = float(dict1[0])
            self.__y = float(dict1[1])
            self.__z = float(dict1[2])
        except ValueError:
            print('Эйб слышб, введи норм вектор')


    def __add__ (self, other):
        try:
            preobrazovanie = f'{self.__x + other.__x}, {self.__y + other.__y}, {self.__z + other.__z}'
            return Vector(preobrazovanie)
        except AttributeError:
            print('Cкладываем только векторы с векторами')

    def __radd__ (self, other):
        try:
            preobrazovanie = f'{self.__x + other.__x}, {self.__y + other.__y}, {self.__z + other.__z}'
            return Vector(preobrazovanie)
        except AttributeError:
            print('Cкладываем только векторы c векторами')

    def __sub__(self, other):
        try:
            preobrazovanie = f'{self.__x - other.__x}, {self.__y - other.__y}, {self.__z - other.__z}'
            return Vector(preobrazovanie)
        except AttributeError:
            print('Вычитаем только вектор из вектора')
    
    def __rsub__(self, other):
        try:
            preobrazovanie = f'{self.__x - other.__x}, {self.__y - other.__y}, {self.__z - other.__z}'
            return Vector(preobrazovanie)
        except AttributeError:
            print('Вычитаем только вектор из вектора')

    def __mul__(self, other): 
        """
        Скалярное произведение векторов или произведение вектора на число
        """
        try:
            preobrazovanie = self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
            return preobrazovanie
        except AttributeError:
            preobrazovanie = f'{self.__x * other}, {self.__y * other}, {self.__z * other}'
            return Vector(preobrazovanie)

    def __rmul__(self, other):
        """
        Скалярное произведение векторов или произведение вектора на число
        """
        try: 
            preobrazovanie = self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
            return preobrazovanie
        except AttributeError:
            preobrazovanie = f'{self.__x * other}, {self.__y * other}, {self.__z * other}'
            return Vector(preobrazovanie)



    def __matmul__(self, other):
        """
        Векторное произведение векторов. При неправильном импуте будет вас ругать
        """
        try:
            x = (self.__y*other.__z - other.__y*self.__z)
            y = -(self.__x*other.__z - self.__z*other.__x)
            z = (self.__x*other.__y - self.__y*other.__x)
            return Vector(f'{x},{y},{z}')
        except ValueError:
            print('Векторное произведение возможно только с векторами')

    def __rmatmul__(self, other):
        """
        Векторное произведение векторов. При неправильном импуте будет вас ругать
        """
        try:
            x = (self.__y*other.__z - other.__y*self.__z)
            y = -(self.__x*other.__z - self.__z*other.__x)
            z = (self.__x*other.__y - self.__y*other.__x)
            return Vector(f'{x},{y},{z}')
        except ValueError:
            print('Векторное произведение возможно только с векторами')

    def __pow__(self, other):
        try:
            for _ in range(other):
                self = self * self
            return self
        except Exception:
            print('Что-то пошло не так при возведении в степень. Проверьте код')

    def __abs__(self):
        return (self.__x**2 + self.__y**2 + self.__z**2)**0.5

    def __repr__(self):
        return 'Vector("{}, {}, {}")'.format(self.__x,self.__y, self.__z)
    
    def __str__(self):
        return('Vector c координатами x:{}, y:{}, z:{}'.format(self.__x,self.__y, self.__z))

    @classmethod
    def the_farest(cls, N):
        cls.matrica(N)
        the_farest = -1
        for i in range(N):
            if abs(cls._matrica[the_farest]) < abs(cls._matrica[i]):
                the_farest = i
        cls._the_farest = the_farest
        if the_farest == -1:
            print('Нет векторов')
            return
        return cls._matrica[cls._the_farest]

    @classmethod
    def matrica(cls, N):
        if not isinstance(N, int):
            print("Укажите целое число при вызове метода класса")
            return
        print('Укажите {} векторов формата "x,y,z"')
        matrica = []
        for _ in range(N):
            matrica.append(cls(str(input())))
        cls._matrica = matrica
        cls._len_mat = len(matrica)
    
    @classmethod
    def centre_of_mass(cls, N = 0):
        Vector.matrica(N)
        if Vector._matrica == []:
            print('Укажите количество векторов')

            return
        buf_x = buf_y = buf_z = 0
        for i in range(len(Vector._matrica)):
            buf_x += Vector._matrica[i].__x
            buf_y += Vector._matrica[i].__y
            buf_z += Vector._matrica[i].__z
        buf_x = buf_x/len(Vector._matrica)
        buf_y = buf_y/len(Vector._matrica)
        buf_z = buf_z/len(Vector._matrica)
        return Vector(f"{buf_x},{buf_y},{buf_z}")

    @classmethod
    def parallelogramm(vector_1, Vector_2):
        cosfi = vector_1 * Vector_2 / (abs(vector_1)*abs(Vector_2))
        return abs(vector_1)*abs(Vector_2) * (1-cosfi**2)**0.5

    @classmethod
    def parallelepiped(vector_1, Vector_2, vector_3):
        pass 
    

    @classmethod
    def max_per_tre(cls):
        pass
    
    @staticmethod
    def _find_triangle(array_of_numbers, triangle = []):
        if len(array_of_numbers) == 2:
            return triangle
        for i in range(1, len(array_of_numbers)-1):
            for k in range(i + 1, len(array_of_numbers)):
                triangle.append(f'{array_of_numbers[0]},{array_of_numbers[i]},{array_of_numbers[k]}')
        return Vector._find_triangle(array_of_numbers[1:], triangle)


    @classmethod
    def find_triangle(cls, N):
        cls.matrica(N)
        array_of_tri = cls._find_triangle([x + 1 for x in N])
        triangls = []
        for i in range(len(array_of_tri)):
            a,b,c = map(int, array_of_tri[i].split(','))
            triangls.append(Triangle(cls._matrica[a]),Triangle(cls._matrica[b]),Triangle(cls._matrica[c]))
        








class Triangle:

    def __init__(self, point_1, point_2, point_3):
        Triangle.__point_1 = point_1
        Triangle.__point_2 = point_2
        Triangle.__point_3 = point_3
        Triangle.__a = abs(point_1-point_2)
        Triangle.__b = abs(point_3-point_2)
        Triangle.__c = abs(point_1-point_3)
        Triangle._perimetr = Triangle.__a + Triangle.__b + Triangle.__c
        p = Triangle._perimetr/2
        Triangle._square = (
            p * (p - Triangle.__a) * (p - Triangle.__b) * (p - Triangle.__c)
        )**0.5
        
        

x = Vector('3, 0')
y = Vector('0, 4')
z = Vector('0,0')
Tr = Triangle(x,y,z)
print(Tr._square)

print(len(Vector.find_triangle([1,2,3,4,5,6])))

